# Chauffage

[← Retour README](../../README.md)

---

## `automation.gestion_du_chauffage_de_l_etage` — Chauffage de l'Étage

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
