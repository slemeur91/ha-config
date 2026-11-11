# Chauffage (4)

[← Retour README](../../README.md)

## 🔥 Principe du chauffage

Le chauffage repose sur une **chaudière à gaz Chappée Luna Platinium** qui alimente deux circuits distincts.

| | Rez-de-chaussée | Étage |
|---|---|---|
| **Émetteurs** | Plancher chauffant (basse température) | Radiateurs (haute température) |
| **Régulation** | Module **EMO Life** | 5 têtes thermostatiques **Z-Wave** (Bureau, Chambre, Salle de bain, Salle d'eau, Suite parentale) |
| **Commande de la chaudière** | Par le module EMO Life | Contacteur **EnOcean** (`switch.switch_de_la_chaudiere_switch`) |
| **Pilotage depuis HA** | Thermostat `climate.cellier` : marche/arrêt et consigne de température uniquement | Consignes des 5 têtes thermostatiques et contacteur de la chaudière |
| **Automatisation** | [`Gestion du Chauffage du RDC`](#automationgestion_du_chauffage_du_rdc--chauffage-du-rdc) | [`Gestion du Chauffage de l'Etage`](#automationgestion_du_chauffage_de_l_etage--chauffage-de-létage) |

**Chaîne de commande du RDC :** le module EMO Life est relié à **Amazon Alexa**, qui ne sait piloter que la marche/arrêt et la température. Home Assistant atteint Alexa via l'add-on **Homebridge** et son plugin **[Homebridge Alexa Smart Home](https://github.com/joeyhage/homebridge-alexa-smarthome)** :

```
Home Assistant → Homebridge (plugin Alexa Smart Home) → Alexa → module EMO Life → chaudière (plancher chauffant)
```

**Chaîne de commande de l'étage :** chaque tête thermostatique Z-Wave régule son radiateur ; l'automatisation compare températures et consignes des 5 pièces et allume ou coupe la chaudière via le contacteur EnOcean.

```
Home Assistant → Z-Wave JS UI → 5 têtes thermostatiques
Home Assistant → EnOcean MQTT → contacteur EnOcean → chaudière (radiateurs)
```

**Planification :** les deux automatisations ci-dessous gèrent l'ensemble. Les calendriers de l'intégration **[Local Agenda](../hacs.md)** modifient les modes de chauffage (travail, télétravail, week-end, absence…), auxquels les automatisations réagissent pour appliquer les consignes.

---

## `automation.gestion_de_l_integration_daikin_selon_le_contacteur_de_la_climatisation` — Gestion de l'intégration Daikin selon le Contacteur de la Climatisation
> [📄 Voir le YAML](../../automations/gestion_de_l_integration_daikin_selon_le_contacteur_de_la_climatisation.yaml)

**Déclencheurs :**
- `switch.contacteur_de_la_climatisation` passe à OFF
- `switch.contacteur_de_la_climatisation` passe à ON
- Démarrage de Home Assistant (resynchronisation)

**Fonctionnement :**
- Contacteur OFF → désactive toutes les entrées de l'intégration Daikin (les unités ne sont plus alimentées, évite les erreurs de connexion).
- Contacteur ON → réactive toutes les entrées de l'intégration Daikin.

**Entités principales :**
- `switch.contacteur_de_la_climatisation` : alimentation physique de la clim
- Intégration `daikin` (4 unités)

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

## `automation.gestion_du_chauffage_de_l_etage` — Chauffage de l'Étage
> [📄 Voir le YAML](../../automations/gestion_du_chauffage_de_l_etage.yaml)

**Statut :** Finalisé | **Evolution :** Robustesse — la commande du switch chaudière est envoyée dès que son état n'est pas déjà celui voulu (« différent de on » / « différent de off ») au lieu d'exiger exactement off / on : un état `unknown` (après redémarrage de HA ou de la passerelle EnOcean) ne bloque plus la commande. Ajout d'un déclencheur au retour du switch chaudière (passage de `unavailable`/`unknown` à `on`/`off` stable 15 s) pour recalculer et renvoyer la commande perdue pendant une coupure de la passerelle EnOcean ou un redémarrage.

Précédente : Correction — `binary_sensor.do_bureau` et `binary_sensor.do_suite_parental` (Somfy Protexial) ont un état principal (on/off) qui ne reflète pas fiablement l'ouverture réelle (il peut rester bloqué sur une valeur alors que l'attribut `Door open` bascule correctement entre `open`/`closed`, cas déjà observé sur `binary_sensor.do_suite_parental`). Leur vérification "porte ouverte" teste désormais l'attribut `Door open` plutôt que l'état principal du binary_sensor. Les 3 velux (`cover.velux_*`) n'ont pas cet attribut et gardent donc leur vérification d'état classique (`open`/`closed`).

**Déclencheurs :**
- Changement de `input_boolean.chauffage_horsgel`, `input_select.chauffage_mode_etage`, `input_select.chauffage_action`
- Fin de `timer.chauffage_timer_etage`
- Changement de température courante d'un des 5 thermostats Z-Wave de l'étage
- Changement d'état des velux ou des détecteurs de portes (avec délai 5 min)
- Retour du switch chaudière après indisponibilité (`unavailable`/`unknown` → `on`/`off` depuis 15 s)

**Fonctionnement :**
1. Calcule en parallèle la variable `horsgel_etage` (vrai si mode HorsGel global, portes (attribut `Door open`)/velux ouverts, ou mode Absent) et ajuste les consignes de chaque pièce selon le mode (Confort / Réduit / TéléTravail).
2. Met à jour `input_boolean.chauffage_horsgel_etage` et envoie un mail si changement de mode.
3. Applique la consigne calculée à chacun des 5 thermostats Z-Wave (Bureau, Chambre, Suite parentale, SdE, SdB) ; si au moins un thermostat a été mis à jour, démarre le timer de vérification.
4. Calcule avec hystérésis si la chaudière doit chauffer (comparaison température courante vs consigne sur les 5 zones) et pilote le switch chaudière en conséquence.

**Entités principales :**
- `climate.chauffage_du_bureau/chambre/suite_parentale/salle_d_eau/salle_de_bain_nodeid_*` : thermostats Z-Wave
- `switch.switch_de_la_chaudiere_switch` : commande chaudière
- `timer.chauffage_timer_etage` : délai de vérification
- `counter.chauffage_compteur_etage` / `counter.chauffage_compteur_etage_action` : logique de décision
- `binary_sensor.do_bureau`, `binary_sensor.do_suite_parental` (attribut `Door open`) et `cover.velux_de_la_chambre/salle_de_bain/salle_d_eau` (état) : détecteurs d'ouverture

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
