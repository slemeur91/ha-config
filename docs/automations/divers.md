# Divers

[← Retour README](../../README.md)

---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR – Mise à jour statistiques journalières

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.gazpar_cheptainville_card` (nouvelles données via Gazpar2MQTT)

**Conditions :** Sensor non indisponible / inconnu

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données de consommation gaz dans les statistiques long-terme de HA.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_de_la_boite_aux_lettres` — Gestion de la Boîte aux Lettres

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

## `automation.correction_tuya` — Correction Tuya

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant

**Fonctionnement :**
1. Attend 5 minutes (initialisation Tuya).
2. Force l'activation du switch USB de la multiprise garage.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` — Notification Mail Hebdomadaire Batteries

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Hebdomadaire (selon configuration)

**Fonctionnement :**
1. Envoie un mail récapitulatif des appareils dont la batterie est sous le seuil d'alerte.

**Entrées utilisées :** Aucune entrée helper.
