# 📜 Scripts (16)

[← Retour README](../README.md)

---

## Notifications

### `script.notification_mail`
Envoi d'un mail de notification.

**Paramètres :**
- `message_type` : type (Information, Alerte, Chauffage Etage, Chauffage RDC…)
- `message_mail` : corps du message

**Fonctionnement :**
1. Appelle `notify.email` avec le type en objet et le message en corps.

**Destinataire :** [votre-email@domaine.fr]

---

### `script.notification_sms`
Envoi d'un message via Telegram.

**Paramètres :**
- `message_type` : type du message
- `message_sms` : corps du message

**Fonctionnement :**
1. Appelle `telegram_bot.send_message` avec le type en titre et le message en corps.

**Bot :** [Votre bot Telegram]

---

### `script.notification_vocale`
Diffusion d'un message TTS sur les enceintes SONOS actives.

**Paramètres :**
- `message_vocal` : texte à synthétiser

**Fonctionnement :**
1. Selon le mode SONOS actif (COUCHE → Suite parentale / REVEIL → Salon+Suite+SdE / autre → Salon+Garage si TéléTravail) :
   - Snapshot de l'état des enceintes
   - Mise en pause si lecture en cours
   - Volume à 60% (40% Garage en TéléTravail)
   - Synthèse vocale via `tts.google_translate_fr_fr`
   - Attente fin de diffusion (timeout 2 min)
   - Restauration état précédent

**Entités utilisées :**
- `input_select.sonos` : détermination des enceintes cibles
- `input_select.calendrier` : mode TéléTravail
- `media_player.salon` / `media_player.suite_parentale` / `media_player.salle_d_eau` / `media_player.garage`
- `tts.google_translate_fr_fr`

---

### `script.notification_snapshot`
Capture et envoi par mail des images de 6 caméras.

**Fonctionnement :**
1. Capture en parallèle les caméras 1, 2, 3, 4, 6 et le portier.
2. Envoie un mail avec toutes les images en pièces jointes.

**Entités utilisées :**
- `camera.slm_camera1` / `camera.slm_camera2` / `camera.slm_camera3` / `camera.slm_camera4` / `camera.slm_camera6` / `camera.slm_portier`

---

## SONOS Radio

### `script.sonos_radio_sur_le_salon`
Lance Voltage sur le Salon avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos (FV:2/37).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.salon`

---

### `script.sonos_radio_sur_la_suite_parentale`
Lance la radio sur la Suite parentale avec sélection horaire et repli.

**Fonctionnement :**
1. Entre 4h et 20h30 → Voltage ; sinon → Évasion FM Essonne (radio de nuit).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Évasion FM Essonne via Radio Browser.

**Entités utilisées :** `media_player.suite_parentale`

---

### `script.sonos_radio_sur_le_garage`
Lance Voltage sur le Garage avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos.
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.garage`

---

## Réveil

### `script.gestion_du_reveil`
Déclenche le réveil musical et envoie un mail de confirmation.

**Fonctionnement :**
1. Si `input_select.sonos_action` est déjà en REVEIL → déclenche directement l'automation SONOS.
2. Sinon → positionne l'action sur REVEIL (déclenchement par trigger d'état).
3. Envoie mail "Réveil".

**Entités utilisées :**
- `input_select.sonos_action` : commande SONOS

---

## Actions iOS

### `script.ios_porte_du_garage`
Toggle de la porte du garage (Somfy RTS).

**Entités utilisées :** `cover.rts_4_portal`

---

### `script.ios_serrure_du_garage_deverrouiller`
Déverrouille la serrure Nuki du garage.

**Entités utilisées :** `lock.serrure_du_garage`

---

### `script.ios_serrure_de_l_entree_deverrouiller`
Déverrouille la serrure Nuki de l'entrée.

**Entités utilisées :** `lock.serrure_de_l_entree`

---

### `script.ios_serrure_de_l_entree_verrouiller`
Verrouille la serrure Nuki de l'entrée.

**Entités utilisées :** `lock.serrure_de_l_entree`

---

### `script.ios_alarme_activation_absent`
Arme l'alarme en mode absent.

**Entités utilisées :** `alarm_control_panel.alarme`

---

### `script.ios_alarme_desactivation`
Désarme l'alarme.

**Entités utilisées :** `alarm_control_panel.alarme`

---

## Utilitaires

### `script.reload_pyscript`
Recharge l'intégration pyscript sans redémarrer HA.

**Entités utilisées :** `pyscript.reload`

---

### `script.delete_all_orphaned_entities`
Supprime toutes les entités orphelines du registre HA (fournit par Spook).

**Entités utilisées :** `homeassistant.delete_all_orphaned_entities`
