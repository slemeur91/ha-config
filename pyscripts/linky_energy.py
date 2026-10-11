# ═══════════════════════════════════════════════════════════════════════════
#  Fichier      : /config/pyscript/linky_energy.py
#  Intégration  : pyscript (HACS)
#
#  Expose le service Home Assistant :
#    pyscript.linky_update   – réimporte les 7 derniers jours de consommation
#                               et de coût Linky avec les VRAIES dates Enedis.
#
#  Pourquoi ce script ?
#    Le capteur MQTT sensor.linky_..._base_consumption ne se met à jour
#    qu'une fois par jour, tôt le matin, avec la valeur finalisée de la veille
#    (Enedis ne fournit que des données J-1). Home Assistant construit ses
#    statistiques journalières à partir de l'horodatage du CHANGEMENT D'ÉTAT,
#    pas de la date réelle de consommation → décalage d'un jour dans les
#    statistiques long terme.
#
#    Ce script relit les attributs `dailyweek` / `daily` / `dailyweek_HP` du
#    capteur sensor.linky_..._consumption (qui contiennent les VRAIES dates
#    Enedis pour chacun des 7 derniers jours) et réécrit les statistiques
#    long terme de base_consumption (kWh) et base_consumption_cost (EUR)
#    avec la date exacte de consommation, en repartant du dernier cumul déjà
#    enregistré (comme pour l'historique importé manuellement).
#
#  Auto-guérison n°1 – double compilation native :
#    L'entité MQTT Linky embarque elle-même un state_class natif (total /
#    total_increasing), que Home Assistant continue parfois de compiler en
#    parallèle de ce script (double moteur), même après exclusion via
#    recorder.yaml. Cela peut ponctuellement injecter un point corrompu
#    (sum=0, "reset" détecté à tort) à une heure arbitraire. À chaque
#    exécution, ce script corrige automatiquement tout point à sum=0 en le
#    maintenant à plat sur le dernier cumul connu valide.
#
#  Auto-guérison n°2 – données Enedis publiées en retard :
#    Enedis/MyElectricalData publie parfois un jour avec un retard de
#    plusieurs jours (valeur à 0 dans `dailyweek` en attendant). Si ce
#    script importait ce 0 tel quel et le considérait comme "définitif", la
#    vraie valeur ne serait jamais réimportée une fois publiée par Enedis.
#    Pour éviter ça, à chaque exécution, ce script recalcule entièrement le
#    cumul des 7 derniers jours à partir d'une ancre fiable (le dernier
#    point antérieur à la fenêtre de 7 jours) et réécrit tout jour dont la
#    valeur enregistrée ne correspond plus à la valeur désormais publiée
#    par Enedis. Les jours sortis de cette fenêtre de 7 jours avant d'avoir
#    reçu leur vraie valeur restent malheureusement irrécupérables (Enedis
#    ne fournit pas d'historique journalier au-delà de cette fenêtre glissante
#    via cet attribut).
# ═══════════════════════════════════════════════════════════════════════════

from datetime import datetime
import inspect
import logging

log = logging.getLogger(__name__)

# ────────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────────
SOURCE_SENSOR    = "sensor.linky_22217944914302_consumption"
TARGET_KWH_ID    = "sensor.linky_22217944914302_base_consumption"
TARGET_COST_ID   = "sensor.linky_22217944914302_base_consumption_cost"
KWH_NAME         = "Linky 22217944914302 base consumption"
COST_NAME        = "Linky 22217944914302 base consumption cost"
PRICE_PER_KWH    = 0.2016   # € / kWh – doit correspondre à consumption_price_base dans config.yaml
LOOKBACK_POINTS  = 60       # nombre de points récents inspectés pour l'auto-guérison / la fenêtre glissante
CORRECTION_EPSILON = 0.01   # écart minimal (kWh ou EUR) pour considérer un point comme à corriger
# ─────────────────────────────────────────────────


def _to_utc_dt(value):
    """Normalise une valeur 'start' issue de get_last_statistics (float ts, str ou datetime) en datetime UTC."""
    import homeassistant.util.dt as dt_util

    if value is None:
        return None
    if isinstance(value, (int, float)):
        return dt_util.utc_from_timestamp(value)
    if isinstance(value, str):
        return dt_util.parse_datetime(value)
    return value


def _build_metadata(statistic_id, name, unit, unit_class):
    """Construit le StatisticMetaData commun aux imports et aux corrections."""
    from homeassistant.components.recorder.statistics import StatisticMetaData

    extra_meta = {}
    try:
        from homeassistant.components.recorder.statistics import StatisticMeanType
        extra_meta["mean_type"] = StatisticMeanType.NONE
    except ImportError:
        pass

    meta_kwargs = dict(
        statistic_id=statistic_id, source="recorder", name=name,
        unit_of_measurement=unit, has_mean=False, has_sum=True,
        **extra_meta,
    )
    try:
        if unit_class:
            return StatisticMetaData(unit_class=unit_class, **meta_kwargs)
        return StatisticMetaData(**meta_kwargs)
    except TypeError:
        return StatisticMetaData(**meta_kwargs)


async def _get_recent_stats(statistic_id, number):
    """Récupère jusqu'à `number` des derniers points enregistrés, triés du plus ancien au plus récent.

    get_last_statistics a changé de signature selon les versions de HA :
    fonction synchrone (à exécuter dans l'executor du recorder) sur les
    anciennes versions, coroutine directement awaitable sur les plus
    récentes. On détecte le bon mode automatiquement.
    """
    from homeassistant.components.recorder.statistics import get_last_statistics

    if inspect.iscoroutinefunction(get_last_statistics):
        result = await get_last_statistics(hass, number, statistic_id, True, {"sum", "state"})
    else:
        from homeassistant.components.recorder import get_instance

        result = await get_instance(hass).async_add_executor_job(
            get_last_statistics, hass, number, statistic_id, True, {"sum", "state"}
        )

    rows = result.get(statistic_id) or []
    parsed = [{"start": _to_utc_dt(r["start"]), "sum": r.get("sum")} for r in rows]
    parsed.sort(key=lambda r: r["start"])
    return parsed


async def _self_heal_zero(statistic_id, name, unit, unit_class, points):
    """Corrige tout point à sum=0 (double-compilation native, horaire arbitraire) trouvé
    parmi `points`. Renvoie (points_corrigés, nombre_corrigé) ; `points` est modifié en
    cohérence pour que l'étape suivante travaille sur des données saines.
    """
    from homeassistant.components.recorder.statistics import async_import_statistics

    if not points:
        return points, 0

    last_good_sum = None
    to_fix = []

    for p in points:
        if p["sum"] not in (None, 0) or last_good_sum is None:
            last_good_sum = p["sum"]
            continue
        to_fix.append(p)

    if not to_fix:
        return points, 0

    metadata = _build_metadata(statistic_id, name, unit, unit_class)
    stats = []
    for p in to_fix:
        p["sum"] = last_good_sum  # corrige en mémoire pour l'étape suivante
        stats.append({"start": p["start"], "state": round(last_good_sum, 3), "sum": round(last_good_sum, 3)})

    await async_import_statistics(hass, metadata, stats)
    log.warning(
        "LINKY: %d point(s) corrompu(s) (sum=0, double compilation native) corrigé(s) "
        "sur %s en maintenant le cumul à %.3f : %s",
        len(stats), statistic_id, last_good_sum,
        [s["start"].isoformat() for s in stats],
    )

    return points, len(stats)


async def _reconcile_window(statistic_id, name, unit, unit_class, points, day_dates, day_values):
    """Recalcule le cumul des jours présents dans `day_dates`/`day_values` (les 7 derniers
    jours connus par le capteur source) à partir d'une ancre fiable antérieure à cette
    fenêtre, et réécrit tout jour dont la valeur enregistrée ne correspond plus à la
    valeur désormais publiée par Enedis (cas typique : Enedis avait publié 0 en attendant,
    puis a corrigé la valeur quelques jours plus tard). Renvoie (n_nouveaux, n_corrigés).
    """
    import homeassistant.util.dt as dt_util
    from homeassistant.components.recorder.statistics import async_import_statistics

    day_points = []
    for date_str, value in zip(day_dates, day_values):
        day = datetime.strptime(date_str, "%Y-%m-%d")
        local_dt = day.replace(hour=23, minute=0, second=0, microsecond=0)
        utc_dt = dt_util.as_utc(dt_util.as_local(local_dt))
        day_points.append((utc_dt, float(value)))
    day_points.sort(key=lambda x: x[0])

    if not day_points:
        return 0, 0

    existing = {p["start"]: p["sum"] for p in points}
    window_start = day_points[0][0]
    anchors = [s for s in existing if s < window_start]

    if not anchors:
        log.warning(
            "LINKY: aucune ancre trouvée avant la fenêtre du %s pour %s – import ignoré "
            "(attendu : l'historique a déjà été importé manuellement).",
            window_start.date(), statistic_id,
        )
        return 0, 0

    cumulative = existing[max(anchors)]
    stats = []
    n_new = 0
    n_corrected = 0

    for utc_dt, value in day_points:
        cumulative += value
        new_sum = round(cumulative, 3)
        recorded = existing.get(utc_dt)
        if recorded is None:
            n_new += 1
            stats.append({"start": utc_dt, "state": new_sum, "sum": new_sum})
        elif abs(recorded - new_sum) > CORRECTION_EPSILON:
            n_corrected += 1
            stats.append({"start": utc_dt, "state": new_sum, "sum": new_sum})
            log.warning(
                "LINKY: correction rétroactive du %s sur %s – cumul %.3f → %.3f "
                "(donnée Enedis probablement publiée en retard puis corrigée).",
                utc_dt.date(), statistic_id, recorded, new_sum,
            )

    if not stats:
        return 0, 0

    metadata = _build_metadata(statistic_id, name, unit, unit_class)
    stats.sort(key=lambda s: s["start"])
    await async_import_statistics(hass, metadata, stats)

    for s in stats:
        log.debug("  → %s  cumul=%.3f", s["start"].date(), s["sum"])

    return n_new, n_corrected


@service
async def linky_update():
    """
    Service : pyscript.linky_update
    Relit les 7 derniers jours (dailyweek / daily) du capteur source et
    réimporte, avec la date exacte de consommation, les statistiques
    long terme manquantes pour base_consumption (kWh) et
    base_consumption_cost (EUR).

    Idempotent et auto-guérissant :
      - tout point à sum=0 laissé par une double compilation native est
        corrigé automatiquement ;
      - tout jour de la fenêtre glissante des 7 derniers jours dont la
        valeur Enedis a été corrigée après coup (publiée en retard) est
        réécrit automatiquement avec le bon cumul.
    """
    entity = hass.states.get(SOURCE_SENSOR)
    if entity is None:
        log.error("LINKY: capteur source '%s' introuvable", SOURCE_SENSOR)
        return

    attrs = dict(entity.attributes)
    dates = attrs.get("dailyweek", [])
    kwh = attrs.get("dailyweek_HP", []) or attrs.get("daily", [])

    if not dates or not kwh or len(dates) != len(kwh):
        log.warning("LINKY: attributs dailyweek/daily absents ou incohérents")
        return

    # dailyweek / daily sont ordonnés du plus récent (hier) au plus ancien (J-7)
    # → on inverse pour traiter chronologiquement
    dates = list(reversed(dates))
    kwh = list(reversed(kwh))
    cost = [round(float(v) * PRICE_PER_KWH, 3) for v in kwh]

    kwh_points = await _get_recent_stats(TARGET_KWH_ID, LOOKBACK_POINTS)
    kwh_points, n_healed_kwh = await _self_heal_zero(TARGET_KWH_ID, KWH_NAME, "kWh", "energy", kwh_points)
    n_new_kwh, n_corrected_kwh = await _reconcile_window(
        TARGET_KWH_ID, KWH_NAME, "kWh", "energy", kwh_points, dates, kwh,
    )

    cost_points = await _get_recent_stats(TARGET_COST_ID, LOOKBACK_POINTS)
    cost_points, n_healed_cost = await _self_heal_zero(TARGET_COST_ID, COST_NAME, "EUR", None, cost_points)
    n_new_cost, n_corrected_cost = await _reconcile_window(
        TARGET_COST_ID, COST_NAME, "EUR", None, cost_points, dates, cost,
    )

    log.info(
        "LINKY update – kWh: %d nouveau(x)/%d corrigé(s)/%d guéri(s) ; "
        "coût: %d nouveau(x)/%d corrigé(s)/%d guéri(s) [source: %s]",
        n_new_kwh, n_corrected_kwh, n_healed_kwh,
        n_new_cost, n_corrected_cost, n_healed_cost,
        dates[-1] if dates else "?",
    )
