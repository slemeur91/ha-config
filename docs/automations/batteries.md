# Batteries (4)

[← Retour README](../../README.md)

---

## `automation.notification_appareils_en_batterie_faible` — Notification Batterie Faible
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_threshold` (batterie passée sous le seuil)
- `battery_notes_battery_threshold` (batterie revenue au-dessus du seuil)

**Fonctionnement :**
1. Batterie faible → crée une notification persistante (appareil, niveau, type de pile).
2. Batterie OK → supprime la notification persistante.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_appareils_en_batterie_faible_hebdomadaire` — Vérification Hebdomadaire Batteries
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible_hebdomadaire.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Chaque vendredi à 19h00

**Fonctionnement :**
1. Lance `battery_notes.check_battery_low` pour forcer une vérification complète.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` — Notification Mail Hebdomadaire Batteries
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible_mail_hebdomadaire.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque vendredi à 19h00

**Fonctionnement :**
1. Parcourt les capteurs de l'intégration Battery Notes et retient ceux dont l'attribut `battery_low` est vrai (nom de l'appareil, niveau, type et quantité de piles).
2. S'arrête sans rien envoyer si aucun appareil n'est en batterie faible.
3. Sinon, compose la liste et envoie un mail récapitulatif (type 'Batteries') via `script.notification_mail`.

**Entités principales :**
- Intégration `battery_notes` : source des niveaux de batterie
- `script.notification_mail` : envoi du mail récapitulatif

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_batterie_remplacee` — Batterie Remplacée
> [📄 Voir le YAML](../../automations/notification_de_batterie_remplacee.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_increased` (niveau de batterie en hausse significative)

**Fonctionnement :**
1. Appelle `script.notification_ha` (fire-and-forget via `script.turn_on`) avec un message adapté selon le type de batterie : rechargeable ("rechargée") ou pile ("remplacée"), mentionnant le niveau avant/après.
2. `message_id` stable par appareil (`battery_increased-device_id-source_entity_id`) pour éviter les doublons si l'évènement se répète.

**Entités principales :** `script.notification_ha`, événement `battery_notes_battery_increased`
