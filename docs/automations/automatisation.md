# Automatisation (14)

[← Retour README](../../README.md)

---

## `automation.gestion_de_l_activation_de_l_arrosage` — Gestion de l'activation de l'Arrosage
> [📄 Voir le YAML](../../automations/gestion_de_l_activation_de_l_arrosage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_select.arrosage` passe à "Actif"
- `timer.arrosage_timer` se termine

**Fonctionnement :**
1. Timer terminé → ferme la vanne, remet le sélecteur à "Inactif", envoie un mail de confirmation.
2. Activation → vérifie la pluviométrie (Netatmo) : arrête si précipitations > 2 mm aujourd'hui ou en cours.
3. Sinon, ouvre la vanne, lance le timer, envoie un mail de déclenchement.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.arrosage` | input_select | Actif, Inactif |
| `timer.arrosage_timer` | timer | Durée configurée |

---

## `automation.gestion_de_l_activation_de_l_imprimante_canon_mf650c` — Gestion de l'Activation de l'Imprimante Canon MF650C
> [📄 Voir le YAML](../../automations/gestion_de_l_activation_de_l_imprimante_canon_mf650c.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `device_tracker.slm_imp1_slm_imp1` passe à "home"
- `device_tracker.slm_imp1_slm_imp1` passe à "not_home"

**Fonctionnement :**
1. Imprimante détectée à la maison → active l'intégration Canon MF650C Series.
2. Imprimante absente → désactive l'intégration (évite les erreurs de connexion).

**Entités principales :**
- `device_tracker.slm_imp1_slm_imp1` : présence réseau de l'imprimante
- Intégration Canon MF650C Series

---

## `automation.gestion_de_la_charge_batterie_de_l_ipad` — Gestion de la Charge Batterie de l'iPad
> [📄 Voir le YAML](../../automations/gestion_de_la_charge_batterie_de_l_ipad.yaml)

**Statut :** En cours — inopérante en l'état, en attente d'une nouvelle prise pilotée pour l'iPad | **Evolution :** Prise en compte du capteur batterie (en fonction de l'application kiosk) pour affiner le pilotage de la charge. Les actions d'extinction et d'allumage de la prise sont à saisir à l'arrivée de la nouvelle prise : les blocs `if`/`then` des deux branches sont actuellement vides.

**Déclencheurs :**
- Le 1er de chaque mois à 1h00 (déclencheur template, aucun déclenchement les autres jours) — id: monthly
- `sensor.ipad_battery_level` passe sous 20% — id: low

**Fonctionnement prévu :**
1. Le 1er du mois à 1h00 → éteindre la prise de l'iPad (si elle est allumée), pour forcer un cycle de décharge/recharge mensuel.
2. Batterie < 20% → allumer la prise de l'iPad (si elle n'est pas déjà allumée).

**État réel :** les deux branches ne contiennent aucune condition ni aucune action ; l'automatisation se déclenche mais ne pilote aucune prise.

**Entités principales :**
- Prise de l'iPad : à définir (nouvelle prise en attente)
- `sensor.ipad_battery_level` : niveau de batterie de l'iPad

---

## `automation.gestion_de_la_livebox_w7_desactivation_du_wifi` — Gestion de la Livebox W7 : désactivation du WiFi
> [📄 Voir le YAML](../../automations/gestion_de_la_livebox_w7_desactivation_du_wifi.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant
- `switch.livebox_w7_wifi` passe à "on"

**Fonctionnement :**
1. Démarrage HA → attend 3 minutes puis éteint le Wi-Fi.
2. Si la Livebox le réactive d'elle-même après un redémarrage/coupure → éteint immédiatement.

**Entités principales :**
- `switch.livebox_w7_wifi` : Wi-Fi de la Livebox W7 (redondant avec le Wi-Fi principal, non utilisé)

---

## `automation.gestion_de_la_presence_dans_les_pieces` — Gestion de la Présence dans les Pièces
> [📄 Voir le YAML](../../automations/gestion_de_la_presence_dans_les_pieces.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Capteurs Aqara FP2 (Suite parentale, Bureau, Chambre) avec délai 5 min

**Fonctionnement :**
1. Présence ON → sélectionne "Présent" dans l'input_select de la pièce.
2. Présence OFF → sélectionne "Absent".

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.presence_suite_parentale` | input_select | Présent, Absent |
| `input_select.presence_bureau` | input_select | Présent, Absent |
| `input_select.presence_chambre` | input_select | Présent, Absent |

---

## `automation.gestion_de_la_qualite_de_l_air` — Gestion de la Qualité de l'Air
> [📄 Voir le YAML](../../automations/gestion_de_la_qualite_de_l_air.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Tout changement de valeur de l'un des 6 capteurs : PM2.5 (moniteur Xiaomi, purificateur Mi Air, Dyson Salon), PM10, VOC et NO2 du Dyson

**Correction du 11/10/2026 :** les déclencheurs étaient des `numeric_state` avec `above: 0`, qui ne s'activaient qu'au passage de 0 à une valeur positive (donc jamais pour le moniteur Xiaomi, le Mi Air et le VOC, qui ne retombent pas à 0). Les seuils sont désormais réévalués à chaque nouvelle mesure.

**Conséquence :** un purificateur allumé à la main alors que l'air est propre est éteint dès la mesure suivante.

**Fonctionnement :**
1. Si seuils de pollution dépassés (PM2.5 > 40, PM10 > 60, VOC > 6 ou NO2 > 6) → allume les purificateurs (Mi Air + Dyson Salon) s'ils sont éteints, active le flag purification.
2. Si tous les seuils sont en dessous des valeurs basses (PM2.5 < 35 — le moniteur Xiaomi étant aussi accepté s'il est indisponible —, PM10 < 45, VOC < 4, NO2 < 4) → éteint les purificateurs, coupe les prises du purificateur et du ventilateur si l'alarme est active et que la purification était en cours, désactive le flag purification.

**Entités principales :**
- `fan.zhimi_m1_6186_air_purifier` / `fan.salon` : purificateurs Mi Air et Dyson
- `input_boolean.purification` : flag état purification
- `sensor.salon_volatile_organic_compounds_index` / `sensor.salon_nitrogen_dioxide_index` : qualité air Dyson

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.purification` | input_boolean | on/off |

---

## `automation.gestion_des_statistiques_journalieres_de_gazpar_reecriture` — GAZPAR – Gestion des statistiques journalières (Réécriture)
> [📄 Voir le YAML](../../automations/gestion_des_statistiques_journalieres_de_gazpar_reecriture.yaml) | [📄 Script pyscript](../../pyscripts/gazpar_energy.py)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.gazpar_cheptainville_card` (nouvelles données via Gazpar2MQTT)

**Conditions :** Sensor non indisponible / inconnu

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données de consommation gaz dans les statistiques long-terme de HA.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_des_statistiques_journalieres_du_linky_reecriture` — LINKY – Gestion des statistiques journalières (Réécriture)
> [📄 Voir le YAML](../../automations/gestion_des_statistiques_journalieres_du_linky_reecriture.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.linky_22217944914302_consumption` (nouvelles données reçues)

**Conditions :** Sensor non indisponible / inconnu

**Fonctionnement :**
1. Lance `pyscript.linky_update` pour réimporter les statistiques long-terme (base_consumption / base_consumption_cost) avec les vraies dates Enedis (correction du décalage J-1).

**Entités principales :**
- `sensor.linky_22217944914302_consumption`, `pyscript.linky_update`

---

## `automation.gestion_du_domicile_en_fonction_de_la_presence` — Gestion du Domicile en fonction de la Présence
> [📄 Voir le YAML](../../automations/gestion_du_domicile_en_fonction_de_la_presence.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.presence_action` (Présent / Réveil / Arrivée / Extinction / Couché)

**Fonctionnement :**
1. Présent → lance les SONOS en mode ON (sauf s'ils sont en REVEIL), arrête la climatisation (`input_button.climatisation_stop`), éteint la prise de l'entrée, allume les prises habituelles (hotte, four, alimentation Apple, terrasse).
2. Réveil → déverrouille la serrure du garage, allume escalier/palier/cuisine/séjour s'il fait encore sombre (jusqu'à 30 min après le lever du soleil), allume les prises habituelles + purificateur + ventilateur + machine à café, éteint la prise de l'entrée, arrête la climatisation.
3. Arrivée → déverrouille la serrure du garage, allume l'entrée si période sombre, allume les prises purificateur + ventilateur, puis bascule en mode Présent.
4. Extinction / Couché → éteint la HiFi, verrouille les deux serrures, éteint les lumières et prises non essentielles (garage, bureau, Apple, terrasse, hotte, four, TV suite parentale) ; les lumières des pièces de vie ne sont éteintes que si l'alarme est armée (absent) ou si la pièce est notée Absent.
   - Alarme armée (absent) : éteint en plus les lumières de circulation et des salles d'eau, ouvre le store pergola s'il n'est pas complètement ouvert, coupe les prises purificateur/ventilateur si aucune purification n'est en cours.
   - Couché : allume les veilleuses (entrée, escalier, palier, suite parentale) avant 02:00 ou après le coucher du soleil, allume la prise de l'entrée, lance les SONOS en mode COUCHE puis remonte le volume suite parentale + salle d'eau après 10 s.

**Entités principales :**
- `input_select.presence_action` : commande entrante (alimentée par `Gestion de l'Alarme`)
- `lock.serrure_de_l_entree` / `lock.serrure_du_garage` : verrouillage automatique
- `input_select.sonos_action` / `input_select.hifi_action` : coordination AV
- `input_button.climatisation_stop` : arrêt de la climatisation
- `cover.store_pergola` : ouverture automatique en cas d'absence
- `switch.machine_a_cafe_100_automatique` : démarrage café au réveil

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.presence_action` | input_select | Présent, Couché, Réveil, Extinction, Arrivée |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.sonos` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.hifi_action` | input_select | ON, SOURCE, OFF |
| `input_boolean.purification` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |
| `input_button.volets_reactivation` | input_button | — |

---

## `automation.gestion_du_poele_et_de_la_climatisation` — Poêle & Climatisation
> [📄 Voir le YAML](../../automations/gestion_du_poele_et_de_la_climatisation.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.poele_status` stable depuis 30 min (tout état)
- `sensor.poele_status` passe à OFF (immédiat)
- `sensor.poele_smoke_temperature` passe sous 78°C
- Changement d'état d'une des 4 climatisations, stable depuis 5 min
- Changement de `input_boolean.alarme`

**Fonctionnement :**
1. Gère le flag `input_boolean.poele` : l'active quand le poêle passe en Ignition ; une fois actif, éteint `climate.poele` si le poêle est en Stand-by et pas encore éteint, puis désactive le flag quand le status vaut OFF.
2. Gère le flag `input_boolean.climatisation` : active si une climatisation tourne, désactive si toutes sont éteintes.
3. Si le flag climatisation est actif, qu'une climatisation tourne encore et que l'alarme est armée (absent) → éteint les climatisations une par une.
4. Si alarme désarmée → rallume le contacteur de la climatisation.
5. Si tout est éteint (poêle OFF + clim OFF + alarme armed_away) → coupe le contacteur de la climatisation.

**Entités principales :**
- `sensor.poele_status` : état du poêle à granulés
- `climate.climatisation_*` : 4 unités de climatisation
- `switch.contacteur_de_la_climatisation` : alimentation physique de la clim
- `input_boolean.poele` / `input_boolean.climatisation` : flags d'état

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.poele` | input_boolean | on/off |
| `input_boolean.climatisation` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |

---

## `automation.gestion_du_poste_de_teletravail` — Gestion du poste de télétravail
> [📄 Voir le YAML](../../automations/gestion_du_poste_de_teletravail.yaml)

**Statut :** En test

**Remplace :** l'événement « Moniteur ON/OFF » (7h40–21h) de l'agenda TéléTravail, neutralisé.

- **Début** : première présence dans le bureau (FP2), en TéléTravail, entre 6h et 20h, si la session du jour n'a pas démarré → écran allumé, Garage sur le favori Sonos VOLTAGE (volume base -0.04), session = on.
- **Fin** : l'écran consomme moins de 10 W pendant 10 min (ordi éteint ou débranché, écran en veille), session en cours → écran coupé, Garage arrêté. La session reste à on : pas de relance automatique le soir.
- **Minuit** : garde-fou, si la session est on → écran coupé, Garage arrêté ; puis session = off pour le lendemain.

**Indisponibilité :** aucune opération si l'écran (LocalTuya) ou le Garage est indisponible ; la fin ignore un passage sous 10 W qui vient d'un état indisponible/inconnu (redémarrage HA, coupure LocalTuya).

**Entités :** `binary_sensor.presence_sensor_fp2_b226_presence_sensor_1`, `switch.bureau_multiprise_du_bureau_4_moniteur`, `sensor.prise_du_bureau_power`, `media_player.garage`, `input_boolean.session_de_teletravail`, `input_select.calendrier`, `input_number.volume_sonos_base`

---

## `automation.gestion_du_soleil` — Gestion du Soleil
> [📄 Voir le YAML](../../automations/gestion_du_soleil.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Lever et coucher du soleil
- Température extérieure franchit un seuil (< 7°C ou > 20°C)
- Changement de l'indice UV ou de la condition météo journalière

**Fonctionnement :**
1. Envoie un mail d'information au lever et au coucher du soleil.
2. Recalcule en parallèle le compteur soleil (3 critères : température > 20°C, UV > 4, condition = Ensoleillé).
3. Active `input_boolean.volets_soleil` si le compteur atteint au moins 2 critères, le désactive sinon.
4. Positionne `input_select.volets_mode` selon la température : Hiver si < 7°C, Été si > 23°C.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_soleil` | counter | Incrément 1 |
| `input_boolean.volets_soleil` | input_boolean | on/off |
| `input_select.volets_mode` | input_select | Été, Hiver |

---

## `automation.gestion_emplacement_sylvain_domicile_absent` — Gestion emplacement Sylvain Domicile/Absent
> [📄 Voir le YAML](../../automations/gestion_emplacement_sylvain_domicile_absent.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- L'iPhone de Sylvain entre dans la zone Domicile (immédiat) — id: Entrée
- L'iPhone de Sylvain a quitté la zone Domicile depuis 30 minutes — id: Sortie

**Fonctionnement :**
1. Entrée → ramène l'intervalle d'actualisation de l'alarme Somfy Protexial à 15 s et rallume les prises 2/3/4 de la multiprise du séjour ainsi que la prise de la Sonos Beam de la suite parentale.
2. Sortie → passe l'intervalle d'actualisation Somfy Protexial à 3600 s (allège les requêtes vers la centrale en cas d'absence), éteint ces mêmes prises, puis déclenche `MAJ Auto Prises LL/SL (Zigbee2MQTT)`.

**Entités principales :**
- `device_tracker.iphone_de_sylvain_le_meur` : localisation de Sylvain
- `number.reseau_somfy_protexial_intervalle_dactualisation` : fréquence d'interrogation de l'alarme
- `switch.multiprise_du_sejour_2` / `_3` / `_4`, `switch.suite_parentale_multiprise_de_la_suite_parentale_2_sonos_beam` : prises coupées en cas d'absence
- `automation.maj_auto_prises_ll_sl_zigbee2mqtt` : déclenchée au départ

---

## `automation.planification_de_l_agenda` — Planification de l'Agenda
> [📄 Voir le YAML](../../automations/planification_de_l_agenda.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque jour à 00:15
- Changement de `input_boolean.alarme` — id: Désactivation Alarme
- Appui sur `input_button.planification_agenda`
- Changement de `input_select.volets_mode` (Été / Hiver)

**Fonctionnement (deux blocs exécutés en parallèle) :**
1. Calendrier, si déclenché par l'alarme et que `input_select.calendrier_action` vaut Absent → `input_select.calendrier` passe à Absent si l'alarme est active, à Repos sinon.
2. Calendrier, autres déclencheurs → interroge `calendar.agenda` pour la journée, extrait les résumés d'événements, puis selon les mots-clés :
   - Absent / Vacance(s) → `chauffage_action` et `calendrier_action` = Absent ; `calendrier` = Absent si l'alarme est armée (absent), sinon Repos ;
   - TéléTravail → les trois sélecteurs = TéléTravail ;
   - jour non travaillé (`binary_sensor.workday_sensor` à off), ARTT ou Congé(s) → les trois sélecteurs = Repos ;
   - sinon → Travail.
   Dans chaque cas, active le sous-calendrier correspondant (`calendar.agenda_absent` / `_teletravail` / `_we_ferie_repos` / `_travail`) et désactive les trois autres, puis envoie un mail avec le mode retenu.
3. HorsGel → activé si l'une des conditions est vraie : (période du 16 avril au 14 octobre ET `input_select.volets_mode` = Eté), OU température extérieure > 22°C, OU (alarme armée absent ET calendrier = Absent). Désactivé sinon. Lorsqu'il est activé et que l'alarme est armée (absent), met aussi `input_select.domicile` à Vacances (calendrier Absent) ou Absent.

**Entités principales :**
- `calendar.agenda` : source de la planification journalière
- `input_select.calendrier` / `input_select.calendrier_action` / `input_select.chauffage_action` : modes actifs
- `binary_sensor.workday_sensor` : jour travaillé ou non
- `input_boolean.chauffage_horsgel` : activation du mode hors-gel global
- `input_select.domicile` : mis à jour en cas d'absence

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.calendrier_action` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |
| `input_button.planification_agenda` | input_button | — |
