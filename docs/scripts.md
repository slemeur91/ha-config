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

**Rôle :** Supprime toutes les entités orphelines du registre HA (service fourni par l'intégration Spook).

**Fonctionnement :**
1. Appelle `homeassistant.delete_all_orphaned_entities`.

---

### `script.reload_pyscript` — Reload pyscript
> [📄 Voir le YAML](../scripts/reload_pyscript.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Recharge l'intégration pyscript sans redémarrer HA.

**Fonctionnement :**
1. Appelle `pyscript.reload`.

---

## Automatisation

### `script.gestion_du_reveil` — Gestion du Réveil
> [📄 Voir le YAML](../scripts/gestion_du_reveil.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déclenche le réveil musical et envoie un mail de confirmation.

**Fonctionnement :**
1. Si `input_select.sonos_action` est déjà en REVEIL → déclenche directement l'automation SONOS.
2. Sinon → positionne l'action sur REVEIL (déclenchement par trigger d'état).
3. Envoie mail "Réveil".

**Entités utilisées :** `input_select.sonos_action`

---

## HiFi

### `script.allumer_eteindre_amplificateur_rotel` — Allumer/Éteindre Amplificateur ROTEL
> [📄 Voir le YAML](../scripts/allumer_eteindre_amplificateur_rotel.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Allume ou éteint l'amplificateur ROTEL et sélectionne son entrée vidéo, en pilotant les boutons IR/réseau et en vérifiant l'état via la présence réseau (`device_tracker`). Appelé par "Gestion de la HiFi" via `script.turn_on` (fire-and-forget).

**Paramètres :**
- `action` : `"on"` ou `"off"`

**Fonctionnement :**
1. `action: "off"` → répète (presse `button.rotel_off` + délai 30s) jusqu'à ce que `device_tracker.slm_rotel_slm_rotel` passe à "not_home" (ampli éteint).
2. `action: "on"` → répète (sélectionne l'entrée selon `input_select.hifi_source` : Zappiti→video1, BluRay→video2, slm-media4→video3 + délai 30s) jusqu'à ce que `device_tracker.slm_rotel_slm_rotel` passe à "home" (ampli allumé).

**Entités utilisées :** `button.rotel_off`, `button.rotel_video1/2/3`, `device_tracker.slm_rotel_slm_rotel`, `input_select.hifi_source`

---

### `script.allumer_eteindre_apple_tv_salon` — Allumer/Éteindre Apple TV du Salon
> [📄 Voir le YAML](../scripts/allumer_eteindre_apple_tv_salon.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Allume ou éteint l'Apple TV du salon, appelé par "Gestion de la HiFi" (branche extinction, `action: "off"`, et branche allumage/SOURCE, `action: "on"`) via `script.turn_on` (fire-and-forget).

**Paramètres :**
- `action` : `"on"` ou `"off"`

**Fonctionnement :**
1. `action: "off"` → si l'appareil semble disponible (media_player ni off/standby/unavailable, ET media_player.is_on, ET remote.is_on depuis au moins 5 s), rafraîchit l'état des entités (`homeassistant.update_entity`) puis envoie la commande `suspend` via `remote.send_command`. Cette garde réduit, sans l'éliminer totalement, les échecs dus à un état HA obsolète par rapport à la connexion réelle (protocole Companion de pyatv) ; erreur résiduelle ignorée (`continue_on_error`) pour ne jamais bloquer l'automatisation appelante.
2. `action: "on"` → recharge l'intégration (`homeassistant.reload_config_entry` sur `remote.apple_tv_du_salon`), attend 8 s, puis appelle `media_player.turn_on` (avec une branche de repli désactivée par défaut qui réessaie 6 fois avec un délai de 5 s entre chaque tentative).

**Entités utilisées :** `media_player.apple_tv_du_salon`, `remote.apple_tv_du_salon`

---

### `script.sonos_radio_sur_la_suite_parentale` — SONOS Radio sur la Suite parentale
> [📄 Voir le YAML](../scripts/sonos_radio_sur_la_suite_parentale.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance la radio sur la Suite parentale avec sélection horaire et repli.

**Fonctionnement :**
1. Entre 4h et 20h30 → Voltage ; sinon → Évasion FM Essonne (radio de nuit).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Évasion FM Essonne via Radio Browser.

**Entités utilisées :** `media_player.suite_parentale`

---

### `script.sonos_radio_sur_le_garage` — SONOS Radio sur le Garage
> [📄 Voir le YAML](../scripts/sonos_radio_sur_le_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance Voltage sur le Garage avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos.
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.garage`

---

### `script.sonos_radio_sur_le_salon` — SONOS Radio sur le Salon
> [📄 Voir le YAML](../scripts/sonos_radio_sur_le_salon.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance Voltage sur le Salon avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos (FV:2/37).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.salon`

---

## iOS

### `script.ios_alarme_activation_absent` — iOS - Alarme Activation (Absent)
> [📄 Voir le YAML](../scripts/ios_alarme_activation_absent.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Arme l'alarme en mode absent.

**Fonctionnement :**
1. Appelle `alarm_control_panel.alarm_arm_away` sur `alarm_control_panel.alarme`.

---

### `script.ios_alarme_desactivation` — iOS - Alarme Désactivation
> [📄 Voir le YAML](../scripts/ios_alarme_desactivation.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Désarme l'alarme.

**Fonctionnement :**
1. Appelle `alarm_control_panel.alarm_disarm` sur `alarm_control_panel.alarme`.

---

### `script.ios_porte_du_garage` — iOS - Porte du Garage
> [📄 Voir le YAML](../scripts/ios_porte_du_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Toggle de la porte du garage (Somfy RTS via RFPlayer).

**Fonctionnement :**
1. Appelle `cover.toggle` sur `cover.rts_4_portal`.

---

### `script.ios_serrure_de_l_entree_deverrouiller` — iOS - Serrure de l'Entrée déverrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_de_l_entree_deverrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déverrouille la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle `lock.unlock` sur `lock.serrure_de_l_entree`.

---

### `script.ios_serrure_de_l_entree_verrouiller` — iOS - Serrure de l'Entrée verrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_de_l_entree_verrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Verrouille la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle `lock.lock` sur `lock.serrure_de_l_entree`.

---

### `script.ios_serrure_du_garage_deverrouiller` — iOS - Serrure du Garage déverrouiller
> [📄 Voir le YAML](../scripts/ios_serrure_du_garage_deverrouiller.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déverrouille la serrure Nuki du garage.

**Fonctionnement :**
1. Appelle `lock.unlock` sur `lock.serrure_du_garage`.

---

## Notifications

### `script.notification_ha` — Notification HA
> [📄 Voir le YAML](../scripts/notification_ha.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'une notification persistante Home Assistant.

**Paramètres :**
- `message_type` : type du message
- `message_ha` : contenu du message
- `notification_id` (optionnel) : identifiant permettant de mettre à jour ou de dismiss la notification ensuite (`persistent_notification.dismiss`)

**Fonctionnement :**
1. Envoie une notification persistante via `notify.persistent_notification` avec le type en titre et le message en corps.
2. Si `notification_id` est fourni, il est transmis pour permettre la mise à jour ou la suppression ciblée de la notification.

---

### `script.notification_mail` — Notification Mail
> [📄 Voir le YAML](../scripts/notification_mail.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'un mail de notification.

**Paramètres :**
- `message_type` : type (Information, Alerte, Chauffage Etage, Chauffage RDC…)
- `message_mail` : corps du message

**Fonctionnement :**
1. Appelle `smtp.send_message` ciblant `notify.email_slemeur_slm_srv_dscloud_me` avec le type en objet (`[HA] {{ message_type }}`) et le message en corps.

**Mode :** queued, max 10

---

### `script.notification_sms` — Notification SMS
> [📄 Voir le YAML](../scripts/notification_sms.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'un message via Telegram.

**Paramètres :**
- `message_type` : type du message
- `message_sms` : corps du message

**Fonctionnement :**
1. Appelle `telegram_bot.send_message` avec le type en titre et le message en corps.

---

### `script.notification_telephone` — Notification Téléphone
> [📄 Voir le YAML](../scripts/notification_telephone.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'une notification push sur l'iPhone.

**Paramètres :**
- `message_type` : type du message
- `message_ha` : contenu du message
- `notification_id` (optionnel) : tag permettant de remplacer/regrouper une notification précédente sur l'iPhone

**Fonctionnement :**
1. Envoie une notification push via `notify.mobile_app_iphone_de_sylvain_le_meur` avec le type en titre et le message en corps.
2. Si `notification_id` est fourni, il est transmis en tant que `tag` pour permettre le remplacement ciblé de la notification.

**Entités utilisées :** `notify.mobile_app_iphone_de_sylvain_le_meur`

---

### `script.notification_snapshot_du_portier` — Notification Snapshot du Portier
> [📄 Voir le YAML](../scripts/notification_snapshot_du_portier.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Capture un snapshot du portier et l'envoie par mail avec le message et le type fournis en paramètres.

**Paramètres :**
- `message_type` : type du message (ex : "Portier")
- `message_mail` : corps du message (ex : "Appuis sur la sonnette")

**Fonctionnement :**
1. Capture une image de `camera.exterieur_slm_portier` dans `/media/Snapshots/portier.jpg`.
2. Envoie un mail `[HA] {{ message_type }}` via `smtp.send_message` (`notify.email_slemeur_slm_srv_dscloud_me`) avec l'image en pièce jointe (`media_source`) et le message en corps.

**Note :** L'ancienne capture vers `/config/www/`, l'ancien envoi via `notify.email` et la notification push iPhone sont conservés dans la séquence mais désactivés (`enabled: false`).

**Entités utilisées :** `camera.exterieur_slm_portier`, `notify.email_slemeur_slm_srv_dscloud_me`

---

### `script.notification_snapshot_des_cameras` — Notification Snapshot des Caméras
> [📄 Voir le YAML](../scripts/notification_snapshot_des_cameras.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Capture les images des 7 caméras et du portier, et les envoie par mail en cas d'alerte.

**Fonctionnement :**
1. Capture en parallèle les caméras `slm_camera1` à `slm_camera7` et `slm_portier` (8 snapshots, dans `/media/Snapshots/`).
2. Envoie un mail `[HA] Alerte` via `smtp.send_message` avec toutes les images en pièces jointes (`media_source`).

**Entités utilisées :** `camera.slm_camera1` à `camera.slm_camera7`, `camera.exterieur_slm_portier`, `notify.email_slemeur_slm_srv_dscloud_me`

---

### `script.notification_vocale` — Notification Vocale
> [📄 Voir le YAML](../scripts/notification_vocale.yaml)

**Statut :** Finalisé

**Rôle :** Diffusion d'un message TTS en overlay (announce) sur les enceintes SONOS actives, sans interrompre une lecture en cours.

**Paramètres :**
- `message_vocal` : texte à synthétiser

**Fonctionnement :**
1. Selon le mode SONOS actif :
   - COUCHE → diffuse sur tous les membres du groupe Suite parentale (`group_members`), volume d'annonce 40.
   - REVEIL / autre → diffuse sur tous les membres du groupe Salon, volume d'annonce 60, + Garage si TéléTravail (volume 40).
2. Chaque diffusion utilise `media_player.play_media` avec `announce: true` et `media_content_id: media-source://tts/tts.google_translate_fr_fr?message=...`.
3. Sonos gère nativement la baisse du volume en cours et sa restauration après l'annonce.

**Entités utilisées :**
- `input_select.sonos` / `input_select.calendrier`
- `media_player.salon` / `media_player.suite_parentale` / `media_player.garage`
- `tts.google_translate_fr_fr`

---

## Scripts Pyscript

> Les scripts pyscript sont dans `/config/pyscript/` et chargés par l'intégration **pyscript** (HACS). Ce ne sont pas des entités `script.*` : ils ne sont pas comptés dans les 20 scripts ci-dessus.
> Sources : [`pyscripts/gazpar_energy.py`](../pyscripts/gazpar_energy.py) | [`pyscripts/surveillance_station_recording.py`](../pyscripts/surveillance_station_recording.py)
