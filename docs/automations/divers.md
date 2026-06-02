# Divers

[← Retour README](../../README.md)

---

## `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire`

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Hebdomadaire (selon configuration)

**Fonctionnement :**
1. Envoie un mail récapitulatif des appareils dont la batterie est sous le seuil.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Changement de `sensor.gazpar_cheptainville_card`

**Conditions :** Sensor disponible

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données dans les statistiques HA.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_de_la_boite_aux_lettres` — Boîte aux Lettres

**Statut :** En production | **Evolution :** Aucune

**Déclencheurs :** Changement de `sensor.p100_boite_aux_lettres_device_posture`

**Fonctionnement :**
1. `input_boolean.courrier_en_attente` ON → désactive, message "boîte vidée".
2. Flag OFF → active, message "colis/courrier déposé".
3. Mail + SMS.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.courrier_en_attente` | input_boolean | on/off |

---

## `automation.nouvelle_automatisation_2` — Température Réfrigérateur

Voir [Alertes & Notifications](alertes_notifications.md).
