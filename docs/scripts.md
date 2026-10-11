# 📜 Scripts (21)

[← Retour README](../README.md)

---

## ⚠️ Appel de script depuis une automatisation : deux comportements distincts

- **Appel direct** (`action: script.<id>`, avec `data:` classique) — Le script s'exécute **dans le contexte de l'automatisation appelante**. Si le script plante (erreur non gérée), l'erreur remonte et **fait planter l'automatisation appelante aussi**, sauf si `continue_on_error: true` est ajouté sur l'étape.

  ```yaml
  action: script.notification_sms
  data:
    message_type: Alerte
    message_sms: "{{ message_alerte }}"
  ```

- **Appel via `script.turn_on`** (avec `target: entity_id:` et `data: variables:`) — Le script est lancé en **tâche de fond indépendante** (fire-and-forget). Une erreur à l'intérieur du script **n'impacte pas** l'automatisation appelante, qui continue normalement.

  ```yaml
  action: script.turn_on
  target:
    entity_id: script.notification_sms
  data:
    variables:
      message_type: Alerte
      message_sms: "{{ message_alerte }}"
  ```

À privilégier : `script.turn_on` pour les scripts annexes (notifications, actions secondaires) afin qu'un échec ponctuel ne bloque jamais le flux principal de l'automatisation. L'appel direct reste pertinent quand on veut justement que l'échec du script soit traité par l'automatisation appelante (ou avec `continue_on_error: true` si on veut ignorer l'erreur sans changer de méthode d'appel).

---

## Administration

### `script.delete_all_orphaned_entities` — Delete all orphaned entities
> [📄 Voir le YAML](../scripts/delete_all_orphaned_entities.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Nettoie le registre des entités en supprimant toutes les entités orphelines (sans intégration active).

**Fonctionnement :**
1. Appelle homeassistant.delete_all_orphaned_entities.

**Entités principales :**
- homeassistant.delete_all_orphaned_entities : service de nettoyage appelé

---

### `script.reload_pyscript` — Reload pyscript
> [📄 Voir le YAML](../scripts/reload_pyscript.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Recharge l'intégration pyscript sans redémarrer HA.

**Fonctionnement :**
1. Appelle pyscript.reload pour recharger tous les scripts Python.

**Entités principales :**
- pyscript.reload : service appelé

---

## Automatisation

### `script.gestion_du_reveil` — Gestion du Réveil
> [📄 Voir le YAML](../scripts/gestion_du_reveil.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déclenche le réveil musical SONOS et envoie un mail de confirmation.

**Fonctionnement :**
1. Si input_select.sonos_action est déjà en REVEIL → déclenche directement l'automation SONOS.
2. Sinon → positionne l'action sur REVEIL (ce qui déclenchera l'automation via trigger).
3. Envoie un mail d'information "Réveil".

**Entités principales :**
- input_select.sonos_action : sélecteur d'action SONOS
- automation.gestion_des_sonos : automatisation déclenchée
- script.notification_mail : envoi du mail

---

## HiFi

### `script.allumer_eteindre_amplificateur_rotel` — Allumer/Éteindre Amplificateur ROTEL
> [📄 Voir le YAML](../scripts/allumer_eteindre_amplificateur_rotel.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Allume ou éteint l'amplificateur ROTEL et sélectionne son entrée vidéo, en pilotant les boutons de l'ampli et en vérifiant l'état atteint via sa présence réseau (device_tracker ou ping). Appelé par 'Gestion de la HiFi' (branche extinction avec action: 'off', branche SOURCE avec action: 'on') via script.turn_on (fire-and-forget).

**Paramètres :**
- action : 'on' ou 'off'

**Fonctionnement :**
1. action 'off' → répète le cycle suivant jusqu'à ce que l'ampli ne soit plus détecté sur le réseau (device_tracker.slm_rotel_slm_rotel à 'not_home' OU binary_sensor.192_168_51_55 à 'off') : 3 appuis sur button.rotel_off espacés de 3s, attente de 20s, rafraîchissement forcé du ping (homeassistant.update_entity), attente de 10s.
2. action 'on' → même cycle, avec 3 appuis sur l'entrée vidéo correspondant à input_select.hifi_source ('Zappiti' → button.rotel_video1, 'BluRay' → button.rotel_video2, 'slm-media4' → button.rotel_video3), jusqu'à ce que l'ampli soit détecté (device_tracker à 'home' OU ping à 'on').
3. continue_on_error : une erreur sur une étape n'interrompt pas le script.

**Limite :** chaque boucle s'arrête au plus tard après 5 cycles (environ 3 min 30). Si l'état réseau attendu n'est toujours pas atteint, une entrée est écrite dans le journal (logbook) au nom de l'ampli, au lieu de boucler indéfiniment.

**Entités principales :**
- button.rotel_off, button.rotel_video1/2/3 : commandes de l'ampli (extinction / sélection d'entrée)
- device_tracker.slm_rotel_slm_rotel, binary_sensor.192_168_51_55 (ping) : présence réseau de l'ampli, utilisée pour vérifier l'état atteint
- input_select.hifi_source : source sélectionnée, détermine l'entrée vidéo activée

---

### `script.allumer_eteindre_apple_tv_salon` — Allumer/Éteindre Apple TV du Salon
> [📄 Voir le YAML](../scripts/allumer_eteindre_apple_tv_salon.yaml)

**Statut :** Finalisé — plus appelé par 'Gestion de la HiFi' | **Evolution :** Aucune

**Rôle :** Allume ou éteint l'Apple TV du Salon en fiabilisant la commande (rechargement de l'intégration puis vérification de l'état atteint). Dans 'Gestion de la HiFi', l'appel à ce script est actuellement désactivé au profit d'un `media_player.turn_on` / `turn_off` direct ; le script reste disponible pour un appel manuel.

**Paramètres :**
- action : 'on' ou 'off'

**Fonctionnement :**
1. Recharge l'intégration Apple TV, puis attend (jusqu'à 20s) que remote.apple_tv_du_salon repasse à 'on' (= connexion pyatv rétablie) au lieu d'un délai fixe.
2. action 'off' → envoie 'suspend' via remote.send_command (contourne le garde power_state de media_player.turn_off), puis attend jusqu'à 15s que media_player passe à 'off'.
3. action 'on' → appelle media_player.turn_on, puis attend jusqu'à 20s que media_player quitte l'état 'off'.
4. Si l'état attendu n'est pas atteint, une entrée logbook est créée pour rendre l'échec visible (au lieu d'un échec totalement silencieux).

**Entités principales :**
- media_player.apple_tv_du_salon : état vérifié, cible de l'allumage
- remote.apple_tv_du_salon : cible du rechargement et de la commande d'extinction

---

### `script.sonos_radio_sur_la_suite_parentale` — SONOS Radio sur la Suite parentale
> [📄 Voir le YAML](../scripts/sonos_radio_sur_la_suite_parentale.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance la radio sur la suite parentale avec sélection automatique selon l'heure et repli.

**Fonctionnement :**
1. Entre 4h et 20h30 → lance Voltage ; sinon → lance Évasion FM Essonne (radio de nuit).
2. Attend 5 secondes.
3. Si la lecture n'a pas démarré → repli sur le flux direct Évasion FM Essonne via Radio Browser.

**Entités principales :**
- media_player.suite_parentale : enceinte SONOS ciblée

---

### `script.sonos_radio_sur_le_garage` — SONOS Radio sur le Garage
> [📄 Voir le YAML](../scripts/sonos_radio_sur_le_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance la radio Voltage sur l'enceinte du garage avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via les favoris Sonos.
2. Attend 5 secondes.
3. Si la lecture n'a pas démarré → repli sur le flux direct Radio Browser.

**Entités principales :**
- media_player.garage : enceinte SONOS ciblée

---

### `script.sonos_radio_sur_le_salon` — SONOS Radio sur le Salon
> [📄 Voir le YAML](../scripts/sonos_radio_sur_le_salon.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance la radio Voltage sur l'enceinte du salon avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via les favoris Sonos.
2. Attend 5 secondes.
3. Si la lecture n'a pas démarré → repli sur le flux direct Radio Browser.

**Entités principales :**
- media_player.salon : enceinte SONOS ciblée

---

## iOS

### `script.ios_alarme_activation_absent` — iOS - Alarme Activation (Absent)
> [📄 Voir le YAML](../scripts/ios_alarme_activation_absent.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour armer l'alarme en mode absent.

**Fonctionnement :**
1. Appelle alarm_control_panel.alarm_arm_away sur alarm_control_panel.alarme.

**Entités principales :**
- alarm_control_panel.alarme : panneau d'alarme piloté

---

### `script.ios_alarme_desactivation` — iOS - Alarme Désactivation
> [📄 Voir le YAML](../scripts/ios_alarme_desactivation.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour désarmer l'alarme.

**Fonctionnement :**
1. Appelle alarm_control_panel.alarm_disarm sur alarm_control_panel.alarme.

**Entités principales :**
- alarm_control_panel.alarme : panneau d'alarme piloté

---

### `script.ios_porte_du_garage` — iOS - Porte du Garage
> [📄 Voir le YAML](../scripts/ios_porte_du_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour ouvrir ou fermer la porte du garage.

**Fonctionnement :**
1. Déclenche cover.toggle sur cover.rts_4_portal (Somfy RTS).

**Entités principales :**
- cover.rts_4_portal : porte de garage pilotée

---

### `script.ios_serrure_de_l_entree_deverrouiller` — iOS - Serrure de l'Entrée déverrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_de_l_entree_deverrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour déverrouiller la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle lock.unlock sur lock.serrure_de_l_entree.

**Entités principales :**
- lock.serrure_de_l_entree : serrure pilotée

---

### `script.ios_serrure_de_l_entree_verrouiller` — iOS - Serrure de l'Entrée verrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_de_l_entree_verrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour verrouiller la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle lock.lock sur lock.serrure_de_l_entree.

**Entités principales :**
- lock.serrure_de_l_entree : serrure pilotée

---

### `script.ios_serrure_du_garage_deverrouiller` — iOS - Serrure du Garage déverrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_du_garage_deverrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Action rapide iOS pour déverrouiller la serrure Nuki du garage.

**Fonctionnement :**
1. Appelle lock.unlock sur lock.serrure_du_garage.

**Entités principales :**
- lock.serrure_du_garage : serrure pilotée

---

## Notifications

### `script.notification_ha` — Notification HA
> [📄 Voir le YAML](../scripts/notification_ha.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'une notification persistante Home Assistant.

**Paramètres :**
- `message_type` : type du message
- `message_corp` : contenu du message
- `message_id` (optionnel) : identifiant permettant de mettre à jour ou de dismiss la notification ensuite (`persistent_notification.dismiss`). Si absent, calculé automatiquement via MD5 de `message_type ~ message_corp` pour éviter les doublons.

**Fonctionnement :**
1. Calcule `message_id_final` : utilise `message_id` s'il est fourni, sinon génère un hash MD5 de `message_type ~ message_corp`.
2. Envoie une notification persistante via `notify.persistent_notification` avec le type en titre, le message en corps, et `notification_id: message_id_final` pour permettre la mise à jour ou la suppression ciblée.

---

### `script.notification_mail` — Notification Mail
> [📄 Voir le YAML](../scripts/notification_mail.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoie un mail de notification.

**Paramètres :**
- message_type : type du message (Information, Alerte, Chauffage, etc.)
- message_corp : corps du message

**Fonctionnement :**
1. Envoie un mail via l'action smtp.send_message sur notify.email_slemeur_slm_srv_dscloud_me, avec '[HA] ' suivi du type en objet et le message en corps.

**Entités principales :**
- notify.email_slemeur_slm_srv_dscloud_me : entité de notification SMTP utilisée (action smtp.send_message)

---

### `script.notification_sms` — Notification SMS
> [📄 Voir le YAML](../scripts/notification_sms.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoie un message Telegram (SMS).

**Paramètres :**
- message_type : type du message
- message_corp : corps du message

**Fonctionnement :**
1. Envoie un message via telegram_bot.send_message avec le type en titre et le message en corps.

**Entités principales :**
- telegram_bot.send_message : service utilisé pour l'envoi

---

### `script.notification_telephone` — Notification Téléphone
> [📄 Voir le YAML](../scripts/notification_telephone.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'une notification push sur l'iPhone.

**Paramètres :**
- `message_type` : type du message
- `message_corp` : contenu du message
- `message_id` (optionnel) : tag permettant de remplacer/regrouper une notification précédente sur l'iPhone. Si non fourni, calculé automatiquement à partir de `message_type` et `message_corp` (hash) pour éviter les doublons.

**Fonctionnement :**
1. Calcule `message_id_final` : utilise `message_id` si fourni, sinon génère un hash MD5 de `message_type ~ message_corp`.
2. Envoie une notification push via `notify.mobile_app_iphone_de_sylvain_le_meur` avec le type en titre, le message en corps, et `message_id_final` en tant que `tag` pour permettre le remplacement ciblé.

**Entités utilisées :** `notify.mobile_app_iphone_de_sylvain_le_meur`

---

### `script.notification_snapshot_du_portier` — Notification Snapshot du Portier
> [📄 Voir le YAML](../scripts/notification_snapshot_du_portier.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Capture un snapshot du portier et l'envoie par mail avec le message et le type fournis en paramètres. Appelé par 'Notification du Portier' via script.turn_on.

**Paramètres :**
- message_type : type du message (ex : 'Portier')
- message_corp : corps du message (ex : 'Appuis sur la sonnette')

**Fonctionnement :**
1. Capture une image du flux haute résolution du portier (camera.exterieur_slm_portier_high_resolution_channel) dans /media/Snapshots/portier.jpg.
2. Envoie un mail '[HA] ' suivi du type, avec l'image en pièce jointe et le message en corps (via smtp.send_message).

**Entités principales :**
- camera.exterieur_slm_portier_high_resolution_channel : flux capturé
- notify.email_slemeur_slm_srv_dscloud_me (smtp.send_message) : envoi du mail

---

### `script.notification_snapshot_des_cameras` — Notification Snapshot des Caméras
> [📄 Voir le YAML](../scripts/notification_snapshot_des_cameras.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Capture les images des 7 caméras et du portier, et les envoie par mail en cas d'alerte. Appelé par 'Alarme Déclenchement' et 'Alarme Sabotage' via script.turn_on.

**Fonctionnement :**
1. Capture en parallèle les caméras slm_camera1 à slm_camera7 et le portier (8 snapshots, dans /media/Snapshots/).
2. Envoie un mail '[HA] Alerte' avec les 8 images en pièces jointes (smtp.send_message, médias locaux Snapshots/).

**Entités principales :**
- camera.slm_camera1 à camera.slm_camera7, camera.exterieur_slm_portier : caméras capturées
- notify.email_slemeur_slm_srv_dscloud_me (smtp.send_message) : envoi du mail

---

### `script.notification_vocale` — Notification Vocale
> [📄 Voir le YAML](../scripts/notification_vocale.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Diffuse un message TTS en overlay (announce) sur les enceintes SONOS actives selon le mode en cours, sans interrompre une lecture en cours.

**Paramètres :**
- message_corp : texte à synthétiser

**Fonctionnement :**
1. Selon le mode SONOS actif :
   - COUCHE → diffuse sur tous les membres du groupe Suite parentale (group_members), volume d'annonce 40.
   - REVEIL / autre → diffuse sur tous les membres du groupe Salon (group_members), volume d'annonce 60, + Garage (volume d'annonce 40) uniquement si le calendrier est en TéléTravail ET que les SONOS sont en mode ON.
2. Chaque diffusion utilise media_player.play_media avec announce: true et media_content_id: media-source://tts/tts.google_translate_fr_fr?message=...&language=fr&cache=true.
3. Sonos gère nativement la baisse du volume en cours, la lecture de l'annonce, puis la restauration — aucune action de restauration explicite n'est nécessaire.

**Entités principales :**
- media_player.suite_parentale, media_player.salon, media_player.garage : enceintes SONOS ciblées
- input_select.sonos, input_select.calendrier : sélecteurs de mode

---

## Scripts Pyscript

> Les scripts pyscript sont dans `/config/pyscript/` et chargés par l'intégration **pyscript** (HACS). Ce ne sont pas des entités `script.*` : ils ne sont pas comptés dans les 21 scripts ci-dessus. 3 fichiers exposent 4 services.

| Service | Rôle | Appelé par | Source |
|---|---|---|---|
| `pyscript.gazpar_import_all` | Import complet des statistiques GAZPAR (journalier, hebdomadaire, mensuel, annuel). À lancer une seule fois, à la main. | Manuel | [`pyscripts/gazpar_energy.py`](../pyscripts/gazpar_energy.py) |
| `pyscript.gazpar_update` | Réimporte les derniers jours de GAZPAR : données réelles, et valeurs à 0 pour les jours pas encore remontés. | `Gestion des Statistiques journalières de GAZPAR – Réécriture` | [`pyscripts/gazpar_energy.py`](../pyscripts/gazpar_energy.py) |
| `pyscript.linky_update` | Relit les 7 derniers jours du capteur Linky et réimporte, à la date exacte de consommation, les statistiques long terme de `base_consumption` (kWh) et `base_consumption_cost` (EUR). Idempotent : corrige les points à 0 et les valeurs Enedis publiées en retard. | `Gestion des Statistiques journalières du Linky – Réécriture` | [`pyscripts/linky_energy.py`](../pyscripts/linky_energy.py) |
| `pyscript.surveillance_station_recording` | Démarre ou arrête l'enregistrement des caméras dans Synology Surveillance Station. | `Gestion de l'Alarme`, `Alarme Déclenchement`, `Alarme Sabotage` | [`pyscripts/surveillance_station_recording.py`](../pyscripts/surveillance_station_recording.py) |
