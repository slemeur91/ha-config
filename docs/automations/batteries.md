# Batteries

[← Retour README](../../README.md)

---

## `automation.notification_appareils_en_batterie_faible` — Notification Batterie Faible

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

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Chaque vendredi à 19h00

**Fonctionnement :**
1. Lance `battery_notes.check_battery_low` pour forcer une vérification complète.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_batterie_remplacee` — Batterie Remplacée

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_increased` (niveau en hausse significative)

**Fonctionnement :**
1. Crée une notification persistante suggérant de marquer la batterie comme remplacée.

**Entrées utilisées :** Aucune entrée helper.
