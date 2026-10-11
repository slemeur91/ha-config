# Automatisation (20)

[← Retour README](../../README.md)

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

## `automation.gestion_du_cycle_du_lave_linge` — Gestion du Cycle du Lave Linge
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_lave_linge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_lave_linge` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_lave_linge` passe de En marche à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.multiprise_de_la_salle_de_bain_power_1` repasse sous 5 W pendant 5 min (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_lave_linge_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_lave_linge` : état de l'appareil
- `sensor.multiprise_de_la_salle_de_bain_power_1` / `_energy_1` : puissance / énergie
- `input_boolean.cycle_lave_linge_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_lave_linge_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_lave_linge_conso_au_debut` / `_a_la_ffin` : index d'énergie au début/fin du dernier cycle

---

## `automation.gestion_du_cycle_du_lave_vaisselle` — Gestion du Cycle du Lave Vaisselle
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_lave_vaisselle.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_lave_vaisselle` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_lave_vaisselle` passe de En marche à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.prise_du_lave_vaisselle_power` repasse sous 3 W pendant 5 min (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_lave_vaisselle_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_lave_vaisselle` : état de l'appareil
- `sensor.prise_du_lave_vaisselle_power` / `_energy` : puissance / énergie
- `input_boolean.cycle_lave_vaisselle_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_lave_vaisselle_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_lave_vaisselle_conso_au_debut` / `_a_la_ffin` : index d'énergie au début/fin du dernier cycle

---

## `automation.gestion_du_cycle_du_seche_linge` — Gestion du Cycle du Sèche Linge
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_seche_linge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_seche_linge` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_seche_linge` passe de En marche ou Anti-froissage à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.multiprise_de_la_salle_de_bain_power_2` repasse sous 3 W pendant 30s (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_seche_linge_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_seche_linge` : état de l'appareil
- `sensor.multiprise_de_la_salle_de_bain_power_2` / `_energy_2` : puissance / énergie
- `input_boolean.cycle_seche_linge_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_seche_linge_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_seche_linge_conso_au_debut` / `_a_la_ffin` : index d'énergie au début/fin du dernier cycle

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

**Statut :** En cours — inopérante en l'état | **Evolution :** Prise en compte du capteur batterie (en fonction de l'application kiosk) pour affiner le pilotage de la charge. Les actions d'extinction et d'allumage de la prise sont à (re)saisir : les blocs `if`/`then` des deux branches sont actuellement vides.

**Déclencheurs :**
- Tous les jours à 1h00 (restreint au 1er du mois par une condition template) — id: monthly
- `sensor.ipad_battery_level` passe sous 20% — id: low

**Fonctionnement prévu :**
1. Le 1er du mois à 1h00 → éteindre la prise de l'iPad (si elle est allumée), pour forcer un cycle de décharge/recharge mensuel.
2. Batterie < 20% → allumer la prise de l'iPad (si elle n'est pas déjà allumée).

**État réel :** les deux branches ne contiennent aucune condition ni aucune action ; l'automatisation se déclenche mais ne pilote pas la prise.

**Entités principales :**
- `switch.prise_de_l_ipad` : alimentation de l'iPad (non référencée dans les actions actuelles)
- `sensor.ipad_battery_level` : niveau de batterie de l'iPad

---

## `automation.gestion_de_la_climatisation_start_en_boost_stop` — Gestion de la Climatisation — Start en Boost / Stop
> [📄 Voir le YAML](../../automations/gestion_de_la_climatisation_start_en_boost_stop.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Appui sur `input_button.climatisation_boost_start`
- Appui sur `input_button.climatisation_stop`

**Fonctionnement :**
1. Boost : pour chacune des 4 clim (Chambre, Suite parentale, Bureau, Séjour), l'allume si éteinte puis (re)lance le préréglage "boost" (même si déjà en boost), en parallèle.
2. Stop : éteint chaque clim encore allumée parmi les 4, en parallèle.

**Entités principales :**
- `climate.climatisation_de_la_chambre`, `climate.climatisation_de_la_suite_parentale`, `climate.climatisation_du_bureau`, `climate.climatisation_du_sejour`
- `input_button.climatisation_boost_start`, `input_button.climatisation_stop`

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

## `automation.gestion_du_chauffage_de_l_etage` — Chauffage de l'Étage
> [📄 Voir le YAML](../../automations/gestion_du_chauffage_de_l_etage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_boolean.chauffage_horsgel`, `input_select.chauffage_mode_etage`, `input_select.chauffage_action`
- Fin de `timer.chauffage_timer_etage`
- Température courante des 5 thermostats Z-Wave
- Changement velux ou portes (délai 5 min)

**Fonctionnement :**
1. Calcule `horsgel_etage` (HorsGel global, portes via attribut `Door open`/velux ouverts, mode Absent).
2. Ajuste consignes (Bureau, Chambre, Suite parentale, SdE, SdB) selon mode (Confort/Réduit/TéléTravail).
3. Met à jour `input_boolean.chauffage_horsgel_etage` et envoie mail si changement.
4. Applique consignes aux 5 thermostats Z-Wave, lance timer si mise à jour.
5. Calcul hystérésis → pilote switch chaudière.

> **Note :** `binary_sensor.do_bureau` et `binary_sensor.do_suite_parental` (Somfy Protexial) sont détectés via l'attribut `Door open` (`open`/`closed`) et non leur état principal, car celui-ci peut rester bloqué sur une valeur incorrecte.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.chauffage_mode_etage` | input_select | Confort, Réduit, HorsGel |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.chauffage_horsgel_etage` | input_boolean | on/off |
| `timer.chauffage_timer_etage` | timer | — |
| `counter.chauffage_compteur_etage` | counter | — |
| `counter.chauffage_compteur_etage_action` | counter | — |
| `input_number.chauffage_consigne_horsgel_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_confort_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_confort_chambre_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_reduit_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_reduit_chambre_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_sdb_etage` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_bureau` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_chambre` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_suiteparentale` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_sdb` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_sde` | input_number | min:0, max:30, step:0.5, unit:°C |

---

## `automation.gestion_du_chauffage_du_rdc` — Chauffage du RDC
> [📄 Voir le YAML](../../automations/gestion_du_chauffage_du_rdc.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_boolean.chauffage_horsgel`, `input_select.chauffage_mode_rdc`, `input_select.chauffage_action`
- Capteurs portes RDC (délai 5 min)

**Fonctionnement :**
1. Calcule `horsgel_rdc` (HorsGel global, portes RDC via attribut `Door open` des `binary_sensor.do_*`, mode Absent).
2. Ajuste consigne RDC selon mode (Confort+/Confort/Réduit).
3. Met à jour `input_boolean.chauffage_horsgel_rdc`, envoie mail.
4. Applique consigne au thermostat du cellier (RDC).

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.chauffage_mode_rdc` | input_select | Confort+, Confort, Réduit, HorsGel |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.chauffage_horsgel_rdc` | input_boolean | on/off |
| `input_number.chauffage_consigne_horsgel_rdc` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_confort_rdc` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_confort_rdc_2` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_consigne_reduit_rdc` | input_number | min:0, max:30, step:0.5, unit:°C |
| `input_number.chauffage_rdc` | input_number | min:0, max:30, step:0.5, unit:°C |

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

## `automation.maj_auto_prises_ll_sl_zigbee2mqtt` — MAJ Auto Prises LL/SL (Zigbee2MQTT)
> [📄 Voir le YAML](../../automations/maj_auto_prises_ll_sl_zigbee2mqtt.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_lave_linge` en Veille depuis 30 s — id: LL veille
- `sensor.etat_seche_linge` en Veille depuis 30 s — id: SL veille
- Toutes les 5 minutes
- Déclenchement manuel par `Gestion emplacement Sylvain Domicile/Absent` au départ du domicile

**Fonctionnement :**
1. Force une relecture MQTT (équivalent du bouton 'MAJ' de l'interface Zigbee2MQTT) des 4 canaux de puissance (`power_1` à `power_4`) de la Multiprise de la Salle de bain et de la Multiprise du Séjour, en parallèle sur les deux multiprises.
2. Contourne le bug Zigbee2MQTT qui empêche parfois la puissance de redescendre à 0 W toute seule (ce qui fausse la détection de fin de cycle du lave-linge et du sèche-linge).

**Entités principales :**
- `sensor.etat_lave_linge` / `sensor.etat_seche_linge` : états des appareils
- Topics MQTT `zigbee2mqtt/Multiprise de la Salle de bain/get` et `zigbee2mqtt/Multiprise du Séjour/get`

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

---

