# Snapshots (3)

[← Retour README](../../README.md)

---

## `automation.notification_de_slm_camera5` — Notification de slm-camera5
> [📄 Voir le YAML](../../automations/notification_de_slm_camera5.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Occupation détectée par `binary_sensor.personne_person_occupancy`

**Conditions :**
- iPhone de Sylvain hors de la zone domicile, ou alarme armée (absent ou nuit)

**Fonctionnement :**
1. Si l'occupation est toujours détectée → lance `script.notification_snapshot_de_slm_camera5` (capture image + vidéo de slm-camera5, envoi par mail) avec le type 'slm-camera5' et le message 'Détection sur slm-camera5'.

**Entités principales :**
- `binary_sensor.personne_person_occupancy` : détection d'occupation
- `device_tracker.iphone_de_sylvain_le_meur`, `alarm_control_panel.alarme` : conditions d'absence / alarme
- `script.notification_snapshot_de_slm_camera5` : capture et envoi du mail

---

## `automation.notification_de_slm_camera6` — Notification de slm-camera6
> [📄 Voir le YAML](../../automations/notification_de_slm_camera6.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Occupation détectée par `binary_sensor.personne_person_occupancy`

**Conditions :**
- iPhone de Sylvain hors de la zone domicile, ou alarme armée (absent ou nuit)

**Fonctionnement :**
1. Si l'occupation est toujours détectée → lance `script.notification_snapshot_de_slm_camera6` (capture image + vidéo de slm-camera6, envoi par mail) avec le type 'slm-camera6' et le message 'Détection sur slm-camera6'.

**Entités principales :**
- `binary_sensor.personne_person_occupancy` : détection d'occupation
- `device_tracker.iphone_de_sylvain_le_meur`, `alarm_control_panel.alarme` : conditions d'absence / alarme
- `script.notification_snapshot_de_slm_camera6` : capture et envoi du mail

---

## `automation.notification_du_portier` — Notification du Portier

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Sonnette du portier (`binary_sensor.exterieur_slm_portier_visiteur` → on) — **actif**
- Présence devant le portier (`binary_sensor.exterieur_slm_portier_personne` → on) — désactivé
- Mouvement devant le portier (`binary_sensor.exterieur_slm_portier_mouvement_2`) — désactivé

**Fonctionnement :**
1. Selon le déclencheur, compose la variable `message_portier` : "Appuis sur la sonnette", "Présence devant le portier" ou "Mouvement devant le portier".
2. Appelle `script.notification_snapshot_du_portier` via `script.turn_on` (fire-and-forget) avec le type et le message.

**Entités utilisées :** `binary_sensor.exterieur_slm_portier_visiteur`, `binary_sensor.exterieur_slm_portier_personne`, `binary_sensor.exterieur_slm_portier_mouvement_2`, `script.notification_snapshot_du_portier`
