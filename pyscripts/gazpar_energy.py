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
#  Trois statistiques sont écrites, une ligne par heure, du premier jour de
#  données jusqu'à la dernière heure terminée :
#    - TARGET_M3_ID   (m³)  : index du compteur
#    - TARGET_KWH_ID  (kWh) : énergie cumulée (energy_kwh GRDF)
#    - TARGET_COST_ID (EUR) : coût cumulé (kWh × prix), statistique externe
#
#  Pour chaque jour : valeur de la veille de 00:00 à 22:00, valeur du jour à
#  23:00 ; les jours sans relevé (et aujourd'hui) gardent la dernière valeur
#  connue → conso 0 en attendant la publication GRDF (J-2 / J-3).
#
#  m³ et kWh sont aussi compilés nativement par HA à partir des capteurs en
#  direct. Pour que HA reparte sans écart après le script :
#    - les valeurs sont ancrées sur l'état actuel du capteur en direct
#      (la dernière ligne écrite a state = état du capteur) ;
#    - sum = state + décalage, où le décalage est celui de la dernière ligne
#      déjà enregistrée (sum − state), propre à chaque statistique.
# ════════════════════════════════════════════════════════════════════════════

import calendar
from datetime import datetime, timedelta
import inspect
import logging

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────────
SOURCE_SENSOR  = "sensor.gazpar_cheptainville_card"

TARGET_M3_ID   = "sensor.gazpar_cheptainville_energie"   # capteur modèle en m³
M3_NAME        = "GAZPAR Cheptainville Énergie"

TARGET_KWH_ID  = "sensor.gazpar_cheptainville_energy"    # capteur MQTT en kWh
KWH_NAME       = "GAZPAR Cheptainville Énergie (kWh)"

TARGET_COST_ID = "gazpar:cheptainville_cost"              # statistique externe
COST_SOURCE    = "gazpar"                                 # = préfixe de TARGET_COST_ID
COST_NAME      = "GAZPAR Cheptainville Coût"
PRICE_ENTITY   = "input_number.prix_manuel_du_kwh_gaz"    # €/kWh
COST_START_DATE = "2026-10-16"   # 1er jour valorisé (AAAA-MM-JJ) ; None = tout l'historique

DEFAULT_FACTOR = 11.2   # kWh/m³ si le relevé n'a pas de coefficient de conversion
UPDATE_DAYS    = 7      # nb de jours relus lors d'un update incrémental
LOOKBACK_ROWS  = 400    # lignes horaires relues pour retrouver l'ancre du coût
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
    parts = time_period.split(" au ")
    return datetime.strptime(parts[1].strip(), "%d/%m/%Y")


def _parse_monthly_end(time_period):
    """'Mois YYYY' (français) → dernier jour du mois."""
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


def _to_float(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# ── Fusion de toutes les sources ──────────────────────────────────────────────

def _collect_all_entries(attrs):
    """
    Fusionne daily[], weekly[], monthly[], yearly[] des attributs du capteur,
    puis complète avec des entrées « filler » (conso = 0) pour chaque jour
    compris entre la dernière donnée réelle et hier inclus.

    Retourne une liste de dicts triée par end_date croissant :
      { end_date, end_index_m3, start_index_m3, energy_kwh, factor,
        granularity, source }
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
                "energy_kwh":     _to_float(entry.get("energy_kwh"), 0.0),
                "factor":         _to_float(entry.get("converter_factor_kwh/m3")),
                "granularity":    new_g,
                "source":         source_key,
            }

    parsers = [
        ("daily",   _parse_date),
        ("weekly",  _parse_weekly_end),
        ("monthly", _parse_monthly_end),
        ("yearly",  _parse_yearly_end),
    ]
    for source_key, parser in parsers:
        for entry in attrs.get(source_key, []):
            try:
                _add(parser(entry["time_period"]), entry, source_key)
            except Exception as e:
                log.warning("GAZPAR %s parse error '%s': %s",
                            source_key, entry.get("time_period"), e)

    # ── Fillers : jours sans relevé journalier entre le dernier daily et hier ──
    if merged:
        yesterday = today - timedelta(days=1)

        daily_keys = [k for k, v in merged.items() if v["source"] == "daily"]
        last_daily = max(daily_keys) if daily_keys else max(merged.keys())
        last_index = merged[last_daily]["end_index_m3"]
        filler_count = 0

        cursor = last_daily + timedelta(days=1)
        while cursor <= yesterday.date():
            existing = merged.get(cursor)
            if existing is None or existing["source"] != "daily":
                merged[cursor] = {
                    "end_date":       datetime(cursor.year, cursor.month, cursor.day),
                    "end_index_m3":   last_index,
                    "start_index_m3": last_index,
                    "energy_kwh":     0.0,
                    "factor":         None,
                    "granularity":    1,
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


# ── Calcul de l'énergie d'une entrée ──────────────────────────────────────────

def _kwh_increment(entry, prev_index):
    """
    kWh à attribuer au jour de fin de l'entrée.
      - daily  : energy_kwh GRDF + rattrapage d'un éventuel trou d'index
                 depuis l'entrée précédente (jours non couverts) ;
      - weekly / monthly / yearly : écart d'index depuis l'entrée précédente
        × coefficient de conversion (évite le double comptage quand une
        période longue chevauche des périodes plus courtes déjà comptées) ;
      - filler : 0.
    """
    if entry["source"] == "filler":
        return 0.0
    factor = entry["factor"] or DEFAULT_FACTOR
    if entry["source"] == "daily":
        gap = max(0.0, entry["start_index_m3"] - prev_index)
        return entry["energy_kwh"] + gap * factor
    return max(0.0, entry["end_index_m3"] - prev_index) * factor


# ── Frise horaire commune aux trois statistiques ──────────────────────────────

def _build_timeline(entries):
    """
    Une ligne par heure, du premier jour de données jusqu'à la dernière heure
    terminée : { start (UTC), day (datetime local naïf), m3, kwh }.
      - jour avec relevé : valeur de la veille de 00:00 à 22:00,
        valeur du jour à 23:00 ;
      - jours sans relevé (et aujourd'hui) : dernière valeur connue.
    `kwh` est un cumul relatif (0 au début de l'historique).
    """
    import homeassistant.util.dt as dt_util

    if not entries:
        return []

    by_day = {}
    for e in entries:
        by_day[e["end_date"].date()] = e

    one_h     = timedelta(hours=1)
    last_hour = dt_util.utcnow().replace(minute=0, second=0, microsecond=0) - one_h
    day       = min(by_day.keys())
    index     = by_day[day]["start_index_m3"]
    cum_kwh   = 0.0
    timeline  = []

    while True:
        day_start = datetime(day.year, day.month, day.day)
        t     = dt_util.as_utc(dt_util.as_local(day_start))
        if t > last_hour:
            break
        t_end = dt_util.as_utc(dt_util.as_local(day_start + timedelta(days=1)))

        start_index = index
        start_kwh   = cum_kwh
        entry = by_day.get(day)
        if entry is not None:
            cum_kwh += _kwh_increment(entry, index)
            index    = entry["end_index_m3"]

        # Bornes en UTC : gère les jours de 23 h / 25 h (changement d'heure)
        while t < t_end and t <= last_hour:
            is_last = t + one_h >= t_end
            timeline.append({
                "start": t,
                "day":   day_start,
                "m3":    index if is_last else start_index,
                "kwh":   cum_kwh if is_last else start_kwh,
            })
            t += one_h

        day += timedelta(days=1)

    return timeline


# ── Accès au recorder ─────────────────────────────────────────────────────────

def _build_metadata(statistic_id, source, name, unit, unit_class):
    try:
        from homeassistant.components.recorder.statistics import StatisticMetaData
    except ImportError:
        from homeassistant.components.recorder.models import StatisticMetaData

    extra_meta = {}
    try:
        from homeassistant.components.recorder.statistics import StatisticMeanType
        extra_meta["mean_type"] = StatisticMeanType.NONE
    except ImportError:
        pass

    meta_kwargs = dict(
        statistic_id=statistic_id, source=source, name=name,
        unit_of_measurement=unit, has_mean=False, has_sum=True,
        **extra_meta,
    )
    # unit_class obligatoire depuis HA 2026.11, y compris à None (ex. EUR)
    try:
        return StatisticMetaData(unit_class=unit_class, **meta_kwargs)
    except TypeError:
        return StatisticMetaData(**meta_kwargs)


def _to_utc_dt(value):
    import homeassistant.util.dt as dt_util

    if value is None:
        return None
    if isinstance(value, (int, float)):
        return dt_util.utc_from_timestamp(value)
    if isinstance(value, str):
        return dt_util.parse_datetime(value)
    return value


async def _get_recent_stats(statistic_id, number):
    """Derniers points enregistrés {start, state, sum}, du plus ancien au plus récent."""
    from homeassistant.components.recorder.statistics import get_last_statistics

    if inspect.iscoroutinefunction(get_last_statistics):
        result = await get_last_statistics(hass, number, statistic_id, True, {"sum", "state"})
    else:
        from homeassistant.components.recorder import get_instance

        result = await get_instance(hass).async_add_executor_job(
            get_last_statistics, hass, number, statistic_id, True, {"sum", "state"}
        )

    rows = result.get(statistic_id) or []
    parsed = [
        {"start": _to_utc_dt(r["start"]), "state": r.get("state"), "sum": r.get("sum")}
        for r in rows
    ]
    parsed.sort(key=lambda r: r["start"])
    return parsed


def _live_value(entity_id):
    entity = hass.states.get(entity_id)
    if entity is None:
        return None
    return _to_float(entity.state)


def _first_index_since(timeline, since):
    if since is None:
        return 0
    for i in range(len(timeline)):
        if timeline[i]["day"] >= since:
            return i
    return len(timeline)


# ── Écriture des statistiques ─────────────────────────────────────────────────

async def _write_native(statistic_id, name, unit, unit_class, timeline, key, since, label):
    """
    Statistique également compilée par HA (m³, kWh). Les valeurs sont ancrées
    sur l'état actuel du capteur : la dernière ligne a state = état du capteur,
    et sum garde le décalage (sum − state) de la dernière ligne enregistrée.
    """
    from homeassistant.components.recorder.statistics import async_import_statistics

    live = _live_value(statistic_id)
    if live is None:
        log.warning("GAZPAR %s – %s indisponible, statistique non réécrite", label, statistic_id)
        return 0

    last_rows = await _get_recent_stats(statistic_id, 1)
    offset = 0.0
    if last_rows and last_rows[-1]["sum"] is not None and last_rows[-1]["state"] is not None:
        offset = last_rows[-1]["sum"] - last_rows[-1]["state"]

    final = timeline[-1][key]
    stats = []
    for p in timeline[_first_index_since(timeline, since):]:
        value = round(live - (final - p[key]), 3)
        stats.append({"start": p["start"], "state": value, "sum": round(value + offset, 3)})

    if not stats:
        return 0

    metadata = _build_metadata(statistic_id, "recorder", name, unit, unit_class)
    await async_import_statistics(hass, metadata, stats)
    log.info(
        "GAZPAR %s – %s : %d ligne(s) [%s → %s], dernière valeur %.3f %s (décalage sum %.3f)",
        label, statistic_id, len(stats),
        stats[0]["start"].isoformat(), stats[-1]["start"].isoformat(),
        stats[-1]["state"], unit, offset,
    )
    return len(stats)


async def _write_cost(timeline, since, label):
    """
    Coût cumulé (statistique externe, seul écrivain). En mise à jour, repart
    du coût déjà enregistré juste avant la fenêtre, pour ne pas recalculer
    l'historique avec le prix actuel. Rien n'est écrit avant COST_START_DATE :
    les jours antérieurs n'ont pas de coût.
    """
    from homeassistant.components.recorder.statistics import async_add_external_statistics

    price = _live_value(PRICE_ENTITY)
    if price is None:
        log.warning("GAZPAR %s – prix %s indisponible, coût non réécrit", label, PRICE_ENTITY)
        return 0

    cost_start_i = 0
    if COST_START_DATE:
        cost_start_i = _first_index_since(timeline, datetime.strptime(COST_START_DATE, "%Y-%m-%d"))

    start_i = max(_first_index_since(timeline, since), cost_start_i)
    anchor  = None
    ref_kwh = 0.0

    if start_i > cost_start_i:
        prev = timeline[start_i - 1]
        rows = await _get_recent_stats(TARGET_COST_ID, LOOKBACK_ROWS)
        for r in rows:
            if r["start"] is not None and r["start"].timestamp() == prev["start"].timestamp():
                anchor  = r["sum"]
                ref_kwh = prev["kwh"]

    if anchor is None:
        # Pas d'ancre (premier passage) : depuis COST_START_DATE, en partant de 0
        start_i = cost_start_i
        anchor  = 0.0
        ref_kwh = timeline[start_i - 1]["kwh"] if start_i > 0 else 0.0

    stats = []
    for p in timeline[start_i:]:
        value = round(anchor + (p["kwh"] - ref_kwh) * price, 3)
        stats.append({"start": p["start"], "state": value, "sum": value})

    if not stats:
        return 0

    metadata = _build_metadata(TARGET_COST_ID, COST_SOURCE, COST_NAME, "EUR", None)
    await async_add_external_statistics(hass, metadata, stats)
    log.info(
        "GAZPAR %s – %s : %d ligne(s) [%s → %s], cumul %.3f EUR (prix %.4f €/kWh)",
        label, TARGET_COST_ID, len(stats),
        stats[0]["start"].isoformat(), stats[-1]["start"].isoformat(),
        stats[-1]["sum"], price,
    )
    return len(stats)


async def _do_import(attrs, since=None, label=""):
    all_entries = _collect_all_entries(attrs)

    by_source = {}
    for e in all_entries:
        by_source.setdefault(e["source"], 0)
        by_source[e["source"]] += 1
    log.info("GAZPAR %s – sources disponibles : %s", label, by_source)

    timeline = _build_timeline(all_entries)
    if not timeline:
        log.info("GAZPAR: aucune entrée à importer %s", label)
        return 0

    n_m3   = await _write_native(TARGET_M3_ID, M3_NAME, "m³", "volume",
                                 timeline, "m3", since, label)
    n_kwh  = await _write_native(TARGET_KWH_ID, KWH_NAME, "kWh", "energy",
                                 timeline, "kwh", since, label)
    n_cost = await _write_cost(timeline, since, label)

    log.info("GAZPAR %s – lignes écrites : m³=%d, kWh=%d, coût=%d",
             label, n_m3, n_kwh, n_cost)
    return n_m3


# ── Services exposés à HA ─────────────────────────────────────────────────────

@service
async def gazpar_import_all():
    """
    Service : pyscript.gazpar_import_all
    Import complet : daily + weekly + monthly + yearly, pour m³, kWh et coût.
    À lancer une fois après une mise à jour du script ou une reprise d'historique.
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
        message         = f"{count} heures réécrites (m³, kWh et coût).",
        notification_id = "gazpar_import_all",
    )


@service
async def gazpar_update():
    """
    Service : pyscript.gazpar_update
    Réimporte les UPDATE_DAYS derniers jours (m³, kWh et coût) jusqu'à la
    dernière heure terminée.
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
        "GAZPAR update – fenêtre : %s → dernière heure terminée  (UPDATE_DAYS=%d)",
        since.date(), UPDATE_DAYS,
    )
    await _do_import(attrs, since=since, label=f"(update {since.date()}→maintenant)")
