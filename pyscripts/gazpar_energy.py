# ════════════════════════════════════════════════════════════════════════════
#  Fichier   : /config/pyscript/gazpar_energy.py
#  Intégration : pyscript (HACS)
#
#  Expose deux services Home Assistant :
#    pyscript.gazpar_import_all   – import complet de tout l'historique
#    pyscript.gazpar_update       – mise à jour des UPDATE_DAYS derniers jours
#
#  Sources fusionnées (priorité décroissante) :
#    daily > weekly > monthly > yearly
#
#  Chaque point de statistique :
#    start = end_date du period à 23:00 heure locale → UTC
#    state = end_index_m3  (index absolu du compteur en m³)
#    sum   = end_index_m3  (même valeur – cumul depuis l'installation)
# ════════════════════════════════════════════════════════════════════════════

import calendar
from datetime import datetime, timedelta
import logging

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────────
SOURCE_SENSOR = "sensor.gazpar_cheptainville_card"
TARGET_ID     = "sensor.gazpar_cheptainville_energie"
SENSOR_NAME   = "GAZPAR Cheptainville Énergie"
UNIT          = "m³"
UPDATE_DAYS   = 7   # nb de jours relus lors d'un update incrémental
# ─────────────────────────────────────────────────

FRENCH_MONTHS = {
    "Janvier": 1, "Février": 2, "Mars": 3, "Avril": 4,
    "Mai": 5, "Juin": 6, "Juillet": 7, "Août": 8, "Aout": 8,
    "Septembre": 9, "Octobre": 10, "Novembre": 11, "Décembre": 12, "Decembre": 12,
}

# Priorité : plus le chiffre est petit, plus la source est précise
GRANULARITY = {"daily": 1, "weekly": 2, "monthly": 3, "yearly": 4}


# ── Parseurs de dates ─────────────────────────────────────────────────────────

def _parse_date(s):
    """'DD/MM/YYYY' → datetime naïf."""
    return datetime.strptime(s.strip(), "%d/%m/%Y")


def _parse_weekly_end(time_period):
    """'Du DD/MM/YYYY au DD/MM/YYYY' → datetime de fin."""
    # ex : "Du 27/04/2026 au 03/05/2026"
    parts = time_period.split(" au ")
    return datetime.strptime(parts[1].strip(), "%d/%m/%Y")


def _parse_monthly_end(time_period):
    """'Mois YYYY' (français) → dernier jour du mois."""
    # ex : "Avril 2026", "Décembre 2025"
    parts = time_period.strip().split(" ")
    month = FRENCH_MONTHS.get(parts[0])
    if month is None:
        raise ValueError(f"Mois inconnu : {parts[0]}")
    year = int(parts[1])
    last_day = calendar.monthrange(year, month)[1]
    return datetime(year, month, last_day)


def _parse_yearly_end(time_period):
    """'YYYY' → 31 décembre de l'année."""
    return datetime(int(time_period.strip()), 12, 31)


# ── Fusion de toutes les sources ──────────────────────────────────────────────

def _collect_all_entries(attrs):
    """
    Fusionne daily[], weekly[], monthly[], yearly[] des attributs du capteur,
    puis complète avec des entrées « filler » (conso = 0) pour chaque jour
    compris entre la dernière donnée réelle et hier inclus.

    Règles :
    - Une seule entrée par date (clé = date du jour de fin de période).
    - En cas de conflit, la source la plus granulaire gagne (daily > weekly > …).
    - Les périodes dont la date de fin est dans le futur sont ignorées.
    - Les fillers ont priorité 5 (plus basse que yearly=4) :
      si une vraie donnée arrive plus tard pour ce jour, elle écrase le filler.

    Retourne une liste de dicts triée par end_date croissant :
      { end_date, end_index_m3, start_index_m3, granularity, source }
    """
    now   = datetime.now()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    merged = {}   # date.date() → dict

    def _add(end_date, entry, source_key):
        if end_date >= today:         # jour en cours ou futur → ignoré
            return
        key = end_date.date()
        new_g = GRANULARITY[source_key]
        existing = merged.get(key)
        if existing is None or new_g < existing["granularity"]:
            merged[key] = {
                "end_date":       end_date,
                "end_index_m3":   float(entry["end_index_m3"]),
                "start_index_m3": float(entry["start_index_m3"]),
                "granularity":    new_g,
                "source":         source_key,
            }

    # ── Daily ────────────────────────────────────────────────────────────────
    for entry in attrs.get("daily", []):
        try:
            _add(_parse_date(entry["time_period"]), entry, "daily")
        except Exception as e:
            log.warning("GAZPAR daily parse error '%s': %s", entry.get("time_period"), e)

    # ── Weekly ───────────────────────────────────────────────────────────────
    for entry in attrs.get("weekly", []):
        try:
            _add(_parse_weekly_end(entry["time_period"]), entry, "weekly")
        except Exception as e:
            log.warning("GAZPAR weekly parse error '%s': %s", entry.get("time_period"), e)

    # ── Monthly ──────────────────────────────────────────────────────────────
    for entry in attrs.get("monthly", []):
        try:
            _add(_parse_monthly_end(entry["time_period"]), entry, "monthly")
        except Exception as e:
            log.warning("GAZPAR monthly parse error '%s': %s", entry.get("time_period"), e)

    # ── Yearly ───────────────────────────────────────────────────────────────
    for entry in attrs.get("yearly", []):
        try:
            _add(_parse_yearly_end(entry["time_period"]), entry, "yearly")
        except Exception as e:
            log.warning("GAZPAR yearly parse error '%s': %s", entry.get("time_period"), e)

    # ── Fillers : jours sans relevé journalier entre le dernier daily et hier ──
    #
    # La référence est la dernière DATE DAILY (pas weekly/monthly).
    # Ex : dernier daily = 30/04, weekly couvre jusqu'au 03/05, today = 04/05
    #   → fillers pour 01/05, 02/05 et 03/05
    #   (les weekly/monthly pour ces dates sont remplacés par les fillers,
    #    plus granulaires ; les vrais daily ne sont jamais écrasés)
    if merged:
        yesterday = today - timedelta(days=1)

        # Chercher la dernière date avec une vraie donnée daily
        daily_keys = [k for k, v in merged.items() if v["source"] == "daily"]
        last_daily = max(daily_keys) if daily_keys else max(merged.keys())
        last_index = merged[last_daily]["end_index_m3"]
        filler_count = 0

        cursor = last_daily + timedelta(days=1)
        while cursor <= yesterday.date():
            existing = merged.get(cursor)
            # Écraser weekly/monthly/yearly mais pas une vraie donnée daily
            if existing is None or existing["source"] != "daily":
                merged[cursor] = {
                    "end_date":       datetime(cursor.year, cursor.month, cursor.day),
                    "end_index_m3":   last_index,
                    "start_index_m3": last_index,
                    "granularity":    1,     # même priorité que daily
                    "source":         "filler",
                }
                filler_count += 1
            cursor += timedelta(days=1)

        if filler_count:
            log.info(
                "GAZPAR: %d jour(s) sans relevé → fillers à 0 ajoutés "
                "(index figé à %.0f m³, depuis %s)",
                filler_count, last_index, last_daily,
            )

    return sorted(merged.values(), key=lambda x: x["end_date"])


# ── Construction des objets StatisticData ─────────────────────────────────────

def _build_stat_objects(entries, since=None):
    """
    Convertit la liste fusionnée en objets StatisticData.

    state = end_index_m3   (index absolu du compteur → valeur toujours croissante)
    sum   = end_index_m3   (même valeur, utilisée par HA pour calculer la conso)

    Compatible TypedDict (HA 2024+, dict) et dataclass (HA ≤ 2023).
    """
    import homeassistant.util.dt as dt_util

    try:
        from homeassistant.components.recorder.statistics import StatisticData  # HA >= 2023
    except ImportError:
        from homeassistant.components.recorder.models import StatisticData      # HA 2022.x

    results = []
    for entry in entries:
        end_date = entry["end_date"]
        if since and end_date < since:
            continue

        local_dt = end_date.replace(hour=23, minute=0, second=0, microsecond=0)
        utc_dt   = dt_util.as_utc(dt_util.as_local(local_dt))

        meter_reading = entry["end_index_m3"]   # index absolu en m³

        results.append(StatisticData(
            start = utc_dt,
            state = meter_reading,   # lecture instantanée du compteur
            sum   = meter_reading,   # cumul depuis l'installation
        ))

    # HA 2024+ → TypedDict (dict) ; HA ≤ 2023 → dataclass
    if results and isinstance(results[0], dict):
        results.sort(key=lambda x: x["start"])
    else:
        results.sort(key=lambda x: x.start)

    return results


# ── Import vers HA Recorder ───────────────────────────────────────────────────

async def _do_import(attrs, since=None, label=""):
    """Fusionne toutes les sources et appelle async_import_statistics."""
    try:
        from homeassistant.components.recorder.statistics import (
            async_import_statistics, StatisticMetaData,
        )
    except ImportError:
        from homeassistant.components.recorder.statistics import async_import_statistics
        from homeassistant.components.recorder.models import StatisticMetaData

    # mean_type requis depuis HA 2025.x, obligatoire en 2026.11
    extra_meta = {}
    try:
        from homeassistant.components.recorder.statistics import StatisticMeanType
        extra_meta["mean_type"] = StatisticMeanType.NONE
    except ImportError:
        pass

    # unit_class requis depuis HA 2025.x, obligatoire en 2026.11
    # "volume" correspond à m³ dans la nomenclature HA
    try:
        metadata = StatisticMetaData(
            statistic_id        = TARGET_ID,
            source              = "recorder",
            name                = SENSOR_NAME,
            unit_of_measurement = UNIT,
            has_mean            = False,
            has_sum             = True,
            unit_class          = "volume",
            **extra_meta,
        )
    except TypeError:
        # HA plus ancien : unit_class non supporté
        metadata = StatisticMetaData(
            statistic_id        = TARGET_ID,
            source              = "recorder",
            name                = SENSOR_NAME,
            unit_of_measurement = UNIT,
            has_mean            = False,
            has_sum             = True,
            **extra_meta,
        )

    # Fusion de toutes les sources
    all_entries = _collect_all_entries(attrs)

    # Log récapitulatif par source (sur le jeu COMPLET avant filtre since)
    by_source = {}
    for e in all_entries:
        by_source.setdefault(e["source"], 0)
        by_source[e["source"]] += 1
    log.info("GAZPAR %s – sources disponibles : %s", label, by_source)

    stats = _build_stat_objects(all_entries, since=since)

    if not stats:
        log.info("GAZPAR: aucune entrée à importer %s", label)
        return 0

    def _start(s):
        return s["start"] if isinstance(s, dict) else s.start

    # Table date_str → source pour le log détaillé
    # (pyscript n'accepte pas les expressions génératrices, on utilise une boucle)
    date_to_source = {}
    for e in all_entries:
        date_to_source[e["end_date"].strftime("%Y-%m-%d")] = e["source"]

    # Log détaillé de chaque entrée (visible dans Journaux en filtrant "GAZPAR")
    for stat in stats:
        date_str  = _start(stat).strftime("%Y-%m-%d")
        src_label = date_to_source.get(date_str, "?")
        state_val = stat["state"] if isinstance(stat, dict) else stat.state
        log.debug(
            "  → %s  [%s]  idx=%.2f",
            date_str, src_label, state_val,
        )

    await async_import_statistics(hass, metadata, stats)

    # Décompte réelles vs fillers parmi les entrées effectivement importées
    filler_count_imp = 0
    real_count_imp   = 0
    for stat in stats:
        src = date_to_source.get(_start(stat).strftime("%Y-%m-%d"), "?")
        if src == "filler":
            filler_count_imp += 1
        else:
            real_count_imp += 1

    log.info(
        "GAZPAR %s – %d importée(s) : %d réelle(s) + %d filler(s)  [%s → %s]",
        label, len(stats), real_count_imp, filler_count_imp,
        _start(stats[0]).strftime("%Y-%m-%d"),
        _start(stats[-1]).strftime("%Y-%m-%d"),
    )
    return len(stats)


# ── Services exposés à HA ─────────────────────────────────────────────────────

@service
async def gazpar_import_all():
    """
    Service : pyscript.gazpar_import_all
    Import complet : daily + weekly + monthly + yearly.
    À appeler une seule fois depuis Outils développeur → Services.
    """
    entity = hass.states.get(SOURCE_SENSOR)
    if entity is None:
        log.error("GAZPAR: capteur source '%s' introuvable", SOURCE_SENSOR)
        persistent_notification.create(
            title           = "GAZPAR – Erreur import",
            message         = f"Capteur {SOURCE_SENSOR} introuvable.",
            notification_id = "gazpar_error",
        )
        return

    attrs = dict(entity.attributes)
    log.info(
        "GAZPAR import_all – sources : daily=%d, weekly=%d, monthly=%d, yearly=%d",
        len(attrs.get("daily", [])),
        len(attrs.get("weekly", [])),
        len(attrs.get("monthly", [])),
        len(attrs.get("yearly", [])),
    )

    count = await _do_import(attrs, since=None, label="(import complet)")

    persistent_notification.create(
        title           = "GAZPAR – Import historique terminé",
        message         = f"{count} statistiques injectées dans {TARGET_ID}.",
        notification_id = "gazpar_import_all",
    )


@service
async def gazpar_update():
    """
    Service : pyscript.gazpar_update
    Réimporte les UPDATE_DAYS derniers jours : données réelles + fillers à 0
    pour les jours non encore remontés par Gazpar.
    Appelé automatiquement par l'automation dès que le capteur source change.
    """
    entity = hass.states.get(SOURCE_SENSOR)
    if entity is None:
        log.error("GAZPAR: capteur source '%s' introuvable", SOURCE_SENSOR)
        return

    attrs = dict(entity.attributes)
    since = (
        datetime.now()
        .replace(hour=0, minute=0, second=0, microsecond=0)
        - timedelta(days=UPDATE_DAYS)
    )
    log.info(
        "GAZPAR update – fenêtre : %s → hier  (UPDATE_DAYS=%d)",
        since.date(), UPDATE_DAYS,
    )
    await _do_import(attrs, since=since, label=f"(update {since.date()}→hier)")
