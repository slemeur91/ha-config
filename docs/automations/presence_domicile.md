# Présence & Domicile

[← Retour README](../../README.md)


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
