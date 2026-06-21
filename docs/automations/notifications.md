# Notifications (8)

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
- Hebdomadaire (selon configuration)

**Fonctionnement :**
1. Envoie un mail récapitulatif des appareils dont la batterie est sous le seuil d'alerte.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_batterie_remplacee` — Batterie Remplacée
> [📄 Voir le YAML](../../automations/notification_de_batterie_remplacee.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_increased` (niveau en hausse significative)

**Fonctionnement :**
1. Crée une notification persistante suggérant de marquer la batterie comme remplacée.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_defaut_du_refrigerateur` — Notification de défaut du réfrigérateur
> [📄 Voir le YAML](../../automations/notification_de_defaut_du_refrigerateur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de température frigo ou congélateur
- Déconnexion réseau de l'interface du réfrigérateur (`device_tracker.samsung_refrigerator`)

**Fonctionnement :**
1. Si frigo hors [2-4°C] OU congélateur hors [-20 à -18°C] OU interface réseau absente → SMS d'alerte.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_l_horloge` — Notification de l'Horloge
> [📄 Voir le YAML](../../automations/notification_de_l_horloge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Toutes les heures (time_pattern)

**Conditions :** Après 10h30

**Fonctionnement :**
1. Compose le message vocal selon l'heure (midi, minuit, 1h, 21h, ou formule générique).
2. Lance `script.notification_vocale`.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_des_alertes` — Notification des Alertes
> [📄 Voir le YAML](../../automations/notification_des_alertes.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Température/luminosité armoire de brassage et grenier
- Détecteurs d'eau (SdB, Cuisine, Cellier)
- Serveurs réseau (slm-disk3, slm-disk4, ZappitiNAS, Livebox)
- Brouillage RF (`binary_sensor.jamming_0_detector`)
- Détecteurs de fumée (Séjour, Cellier, Étage) — montée et descente

**Fonctionnement :**
1. Chaque alerte compose un message via un `input_boolean` garde-fou anti-doublon.
2. Fuite d'eau → ferme/ouvre automatiquement la vanne d'arrivée d'eau.
3. Si message → notifie via vocal + mail + SMS.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.temperature_armoire` | input_boolean | Garde-fou alerte température |
| `input_boolean.luminosite_armoire` | input_boolean | Garde-fou alerte luminosité |
| `input_boolean.luminosite_grenier` | input_boolean | Garde-fou alerte grenier |
| `input_boolean.fuite_sdb` | input_boolean | Garde-fou fuite SdB |
| `input_boolean.fuite_cuisine` | input_boolean | Garde-fou fuite Cuisine |
| `input_boolean.fuite_cellier` | input_boolean | Garde-fou fuite Cellier |
| `input_boolean.brouillage_reseau` | input_boolean | Garde-fou brouillage RF |
| `input_boolean.etat_zapittinas` | input_boolean | État NAS ZappitiNAS |
| `input_boolean.detection_fumee` | input_boolean | Garde-fou détection de fumée |

---

## `automation.notification_des_poubelles` — Notification des Poubelles
> [📄 Voir le YAML](../../automations/notification_des_poubelles.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.poubelles` (déclenché par calendrier permanent)

**Fonctionnement :**
1. Compose le message selon l'option (Sortir/Rentrer Marron/Verte/Jaune).
2. Notification vocale + SMS.
3. Remet le sélecteur à "Aucune".

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.poubelles` | input_select | Sortir Marron, Rentrer Marron, Sortir Jaune, Rentrer Jaune, Sortir Verte, Rentrer Verte, Aucune |
