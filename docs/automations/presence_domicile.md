# Présence & Domicile

[← Retour README](../../README.md)

---

## `automation.gestion_du_domicile_en_fonction_de_la_presence` — Gestion du Domicile en fonction de la Présence

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.presence_action`

**Fonctionnement :**
1. **Présent** → SONOS ON, réactive volets, allume prises (hotte, four, terrasse, Apple).
2. **Réveil** → déverrouille garage, lumières si avant l'aube, prises, machine à café, volets.
3. **Arrivée** → déverrouille garage, lumière entrée si sombre, purificateur → passe en Présent.
4. **Extinction/Couché** → éteint HiFi, verrouille serrures, éteint lumières/prises ; Couché → veilleuses, store pergola si armé, SONOS COUCHE.

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

## `automation.gestion_de_la_presence_dans_les_pieces` — Présence dans les Pièces

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Capteurs Aqara FP2 (Suite parentale, Bureau, Chambre) — avec délai 5 min

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

## `automation.planification_de_l_agenda` — Planification de l'Agenda

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Minuit (00:00:00)
- Changement de `input_boolean.alarme`
- Appui sur `input_button.planification_agenda`

**Fonctionnement :**
1. Si changement alarme + calendrier=Absent → maintient ou bascule vers Repos.
2. Sinon → lit l'agenda du jour, extrait les mots-clés.
3. Positionne `input_select.calendrier`, `chauffage_action`, `calendrier_action` selon les événements.
4. Active/désactive le mode HorsGel selon saison, température et présence.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.calendrier_action` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |
| `input_button.planification_agenda` | input_button | — |
