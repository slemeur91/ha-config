# Divers

[← Retour README](../../README.md)


---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR – Mise à jour statistiques journalières
> [📄 Voir le YAML](../../automations/gazpar_mise_a_jour_statistiques_journalieres.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.gazpar_cheptainville_card` (nouvelles données via Gazpar2MQTT)

**Conditions :** Sensor non indisponible / inconnu

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données de consommation gaz dans les statistiques long-terme de HA.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.depot_courrier_p100_unique` — 📬 Dépôt courrier — P100 unique
> [📄 Voir le YAML](../../automations/depot_courrier_p100_unique.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.p100_boite_aux_lettres_orientation` passe à ON

**Fonctionnement :**
1. Attend 4 s pour confirmer le signal (déduplication).
2. Active `input_boolean.courrier_en_attente`.
3. Notification vocale + SMS "courrier déposé".

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.courrier_en_attente` | input_boolean | on/off |

---

## `automation.ouverture_porte_p100_unique` — 🔓 Ouverture porte — P100 unique
> [📄 Voir le YAML](../../automations/ouverture_porte_p100_unique.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `binary_sensor.p100_boite_aux_lettres_contact` passe à ON

**Fonctionnement :**
1. Attend 5 s puis vérifie la fraîcheur du signal (déduplication).
2. `input_boolean.courrier_en_attente` ON → désactive le flag, compose "boîte vidée".
3. Flag OFF → compose "colis déposé".
4. Notification vocale + SMS.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.courrier_en_attente` | input_boolean | on/off |

---

## `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` — Notification Mail Hebdomadaire Batteries
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible_mail_hebdomadaire.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Hebdomadaire (selon configuration)

**Fonctionnement :**
1. Envoie un mail récapitulatif des appareils dont la batterie est sous le seuil d'alerte.

**Entrées utilisées :** Aucune entrée helper.
