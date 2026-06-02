# Calendrier & Planification

[← Retour README](../../README.md)

Voir aussi [Présence & Domicile](presence_domicile.md) pour `automation.chauffage_statut_journee_selon_agenda`.

---

## `automation.notification_des_poubelles` — Notification des Poubelles

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Changement de `input_select.poubelles`

**Fonctionnement :**
1. Compose le message selon l'option sélectionnée.
2. Notification vocale + SMS.
3. Remet le sélecteur à "Aucune".

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.poubelles` | input_select | Sortir Marron, Rentrer Marron, Sortir Jaune, Rentrer Jaune, Sortir Verte, Rentrer Verte, Aucune |

---

## `automation.planification_de_l_agenda` — Planification de l'Agenda

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Minuit (00:00:00)
- Changement de `input_boolean.alarme`
- Appui sur `input_button.planification_agenda`

**Fonctionnement :**
1. Si alarme + calendrier=Absent → maintient ou bascule vers Repos.
2. Lit le calendrier du jour, extrait les mots-clés (Absent, TéléTravail, Congé, ARTT).
3. Positionne `input_select.calendrier`, `chauffage_action`, `calendrier_action`.
4. Active/désactive les calendriers associés.
5. Gère le mode HorsGel selon saison, température et présence.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.calendrier_action` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_select.chauffage_action` | input_select | WE, TéléTravail, Travail, Absent, Repos |
| `input_boolean.chauffage_horsgel` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |
| `input_button.planification_agenda` | input_button | — |
