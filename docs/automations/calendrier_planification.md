# Calendrier & Planification

[← Retour README](../../README.md)


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
