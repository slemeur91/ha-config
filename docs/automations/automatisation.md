# Automatisation (11)

[← Retour README](../../README.md)


---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR – Mise à jour statistiques journalières
> [📄 Voir le YAML](../../automations/gazpar_mise_a_jour_statistiques_journalieres.yaml) | [📄 Script pyscript](../../pyscripts/gazpar_energy.py)

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

## `automation.gestion_de_la_boite_aux_lettres` — Gestion de la Boîte aux Lettres
> [📄 Voir le YAML](../../automations/gestion_de_la_boite_aux_lettres.yaml)

**Statut :** En production | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.p100_boite_aux_lettres_device_posture`

**Fonctionnement :**
1. `input_boolean.courrier_en_attente` ON → désactive le flag, compose "boîte vidée".
2. Flag OFF → active le flag, compose "colis/courrier déposé".
3. Envoie mail + SMS.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.courrier_en_attente` | input_boolean | on/off |

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
- Capteurs PM2.5 (moniteur Xiaomi, purificateur Mi Air, Dyson Salon), PM10, VOC, NO2
- Attribut PM2.5 du moniteur Xiaomi passe sous 0 (détection indisponibilité appareil)

**Fonctionnement :**
1. Seuils dépassés (PM2.5 > 40, PM10 > 60, VOC > 6 ou NO2 > 6) → allume les purificateurs (Mi Air + Dyson Salon) s'ils sont éteints, active le flag purification.
2. Tous les seuils en dessous des valeurs basses → éteint les purificateurs, coupe les switches physiques si alarme armée, désactive le flag.

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
1. Calcule `horsgel_etage` (HorsGel global, portes/velux ouverts, mode Absent).
2. Ajuste consignes (Bureau, Chambre, Suite parentale, SdE, SdB) selon mode (Confort/Réduit/TéléTravail).
3. Met à jour `input_boolean.chauffage_horsgel_etage` et envoie mail si changement.
4. Applique consignes aux 5 thermostats Z-Wave, lance timer si mise à jour.
5. Calcul hystérésis → pilote switch chaudière.

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
1. Calcule `horsgel_rdc` (HorsGel global, portes ouvertes, mode Absent).
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
- Changement de `input_select.presence_action`

**Fonctionnement :**
1. **Présent** → SONOS ON, réactive volets, allume prises (hotte, four, terrasse, Apple).
2. **Réveil** → déverrouille serrure garage, lumières si avant l'aube, prises, machine à café, volets.
3. **Arrivée** → déverrouille serrure garage, lumière entrée si sombre, purificateur → passe en Présent.
4. **Extinction/Couché** → éteint HiFi, verrouille serrures, éteint lumières/prises ; Couché → veilleuses, store pergola si alarme armée, SONOS COUCHE.

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
- `sensor.poele_status` (avec ou sans délai 30 min)
- `sensor.poele_smoke_temperature` < 78°C
- Changement climatisations (délai 5 min)
- Changement `input_boolean.alarme`

**Fonctionnement :**
1. Gère flag `input_boolean.poele` (allumage/stand-by/extinction).
2. Gère flag `input_boolean.climatisation`.
3. Alarme armée-absent → éteint toutes les climatisations.
4. Alarme désarmée → rallume contacteur climatisation.
5. Tout éteint + absent → coupe contacteur.

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

## `automation.planification_de_l_agenda` — Planification de l'Agenda
> [📄 Voir le YAML](../../automations/planification_de_l_agenda.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Minuit (00:00:00)
- Changement de `input_boolean.alarme`
- Appui sur `input_button.planification_agenda`

**Fonctionnement :**
1. Si déclenché par changement alarme + calendrier = Absent → maintient ou bascule vers Repos.
2. Sinon → interroge le calendrier du jour, extrait les mots-clés (Absent/Vacances, TéléTravail, ARTT/Congé, jour non travaillé).
3. Positionne `input_select.calendrier`, `chauffage_action`, `calendrier_action` selon les événements trouvés.
4. Active/désactive les calendriers associés.
5. Gère le mode HorsGel selon la période de l'année (mai–oct), la température extérieure ou le mode absent.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.calendrier_action` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |
| `input_button.planification_agenda` | input_button | — |
