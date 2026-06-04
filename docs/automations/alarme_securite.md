# Alarme & Sécurité

[← Retour README](../../README.md)


---

## `automation.alarme` — Gestion de l'Alarme
> [📄 Voir le YAML](../../automations/gestion_de_l_alarme.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `alarm_control_panel.alarme` : désarmé → armé (absent/nuit) — id: Activation
- `alarm_control_panel.alarme` : armé → désarmé — id: Désactivation
- `input_button.alarme_activee` / `input_button.alarme_desactivee`

**Fonctionnement :**
1. Activation (absent) → domicile Absent/Vacances, enregistrement caméras 1/2/4, flag alarme ON.
2. Activation (nuit) → domicile Nuit, stop enregistrement caméras 1/2/4, flag ON.
3. Désactivation → domicile Présent, stop enregistrement 1/2/4, flag OFF.
4. Tous cas → réactive volets, enregistrement caméras 3/5/6/7, met à jour presence_action.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.alarme` | input_boolean | on/off |
| `input_select.domicile` | input_select | Absent, Présent, Nuit, Vacances |
| `input_select.presence_action` | input_select | Présent, Couché, Réveil, Extinction, Arrivée |
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_button.alarme_activee` | input_button | — |
| `input_button.alarme_desactivee` | input_button | — |
| `input_button.volets_reactivation` | input_button | — |

---

## `automation.alarme_declenchement` — Alarme Déclenchement
> [📄 Voir le YAML](../../automations/alarme_declenchement.yaml) | [📄 Script pyscript](../../pyscripts/surveillance_station_recording.py)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `alarm_control_panel.alarme` → triggered
- Détection mouvement / ouverture porte-fenêtre
- Fin de `timer.alarme_declenchement`

**Fonctionnement :**
1. Déclenchement → reset compteur, SMS+mail+vocal, enregistrement caméras 1/2/4, snapshots.
2. Timer → incrémente compteur, nouveaux snapshots, relance timer (1 min).
3. Compteur > 8 ou alarme armée → notifications fin d'alerte, stop enregistrement si nuit.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_alarme` | counter | Max 10 cycles |
| `timer.alarme_declenchement` | timer | 1 minute |

---

## `automation.alarme_sabotage` — Alarme Sabotage
> [📄 Voir le YAML](../../automations/alarme_sabotage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `binary_sensor.boitier` → ON (sabotage boîtier)
- Fin de `timer.alarme_sabotage`

**Fonctionnement :**
1. Sabotage → reset compteur, SMS+mail+vocal, enregistrement caméras 1/2/4, snapshots.
2. Timer → incrémente compteur, snapshots, relance timer.
3. Compteur > 8 ou alarme armée → notifications fin, stop si nuit.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_sabotage` | counter | Max 10 cycles |
| `timer.alarme_sabotage` | timer | 1 minute |
