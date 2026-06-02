# 📜 Scripts (16)

[← Retour README](../README.md)

---

## Notifications

### `script.notification_mail` — Notification Mail

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'un mail de notification.

**Paramètres :**
- `message_type` : type (Information, Alerte, Chauffage Etage, Chauffage RDC…)
- `message_mail` : corps du message

**Fonctionnement :**
1. Appelle `notify.email` avec le type en objet et le message en corps.

**Destinataire :** [votre-email@domaine.fr]

---

### `script.notification_sms` — Notification SMS

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Envoi d'un message via Telegram.

**Paramètres :**
- `message_type` : type du message
- `message_sms` : corps du message

**Fonctionnement :**
1. Appelle `telegram_bot.send_message` avec le type en titre et le message en corps.

---

### `script.notification_vocale` — Notification Vocale

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Diffusion d'un message TTS sur les enceintes SONOS actives.

**Paramètres :**
- `message_vocal` : texte à synthétiser

**Fonctionnement :**
1. Selon le mode SONOS actif (COUCHE → Suite parentale / REVEIL → Salon+Suite+SdE / autre → Salon+Garage si TéléTravail) :
2. Snapshot de l'état des enceintes.
3. Mise en pause si lecture en cours.
4. Volume à 60% (40% Garage en TéléTravail).
5. Synthèse vocale via `tts.google_translate_fr_fr`.
6. Attente fin de diffusion (timeout 2 min).
7. Restauration état précédent.

**Entités utilisées :**
- `input_select.sonos` / `input_select.calendrier`
- `media_player.salon` / `media_player.suite_parentale` / `media_player.salle_d_eau` / `media_player.garage`
- `tts.google_translate_fr_fr`

---

### `script.notification_snapshot` — Notification Snapshot

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Capture et envoi par mail des images de 6 caméras lors d'une alerte.

**Fonctionnement :**
1. Capture en parallèle les caméras 1, 2, 3, 4, 6 et le portier.
2. Envoie un mail avec toutes les images en pièces jointes.

**Entités utilisées :** `camera.slm_camera1` à `camera.slm_camera6`, `camera.slm_portier`

---

## SONOS Radio

### `script.sonos_radio_sur_le_salon` — SONOS Radio sur le Salon

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance Voltage sur le Salon avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos (FV:2/37).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.salon`

---

### `script.sonos_radio_sur_la_suite_parentale` — SONOS Radio sur la Suite parentale

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance la radio sur la Suite parentale avec sélection horaire et repli.

**Fonctionnement :**
1. Entre 4h et 20h30 → Voltage ; sinon → Évasion FM Essonne (radio de nuit).
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Évasion FM Essonne via Radio Browser.

**Entités utilisées :** `media_player.suite_parentale`

---

### `script.sonos_radio_sur_le_garage` — SONOS Radio sur le Garage

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Lance Voltage sur le Garage avec repli automatique.

**Fonctionnement :**
1. Lance Voltage via favoris Sonos.
2. Attend 5 secondes.
3. Si pas de lecture → repli sur flux Radio Browser direct.

**Entités utilisées :** `media_player.garage`

---

## Réveil

### `script.gestion_du_reveil` — Gestion du Réveil

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déclenche le réveil musical et envoie un mail de confirmation.

**Fonctionnement :**
1. Si `input_select.sonos_action` est déjà en REVEIL → déclenche directement l'automation SONOS.
2. Sinon → positionne l'action sur REVEIL (déclenchement par trigger d'état).
3. Envoie mail "Réveil".

**Entités utilisées :** `input_select.sonos_action`

---

## Actions iOS

### `script.ios_porte_du_garage` — iOS - Porte du Garage

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Toggle de la porte du garage (Somfy RTS via RFPlayer).

**Fonctionnement :**
1. Appelle `cover.toggle` sur `cover.rts_4_portal`.

---

### `script.ios_serrure_du_garage_deverrouiller` — iOS - Serrure du Garage déverrouiller

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déverrouille la serrure Nuki du garage.

**Fonctionnement :**
1. Appelle `lock.unlock` sur `lock.serrure_du_garage`.

---

### `script.ios_serrure_de_l_entree_deverrouiller` — iOS - Serrure de l'Entrée déverrouiller

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Déverrouille la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle `lock.unlock` sur `lock.serrure_de_l_entree`.

---

### `script.ios_serrure_de_l_entree_verrouiller` — iOS - Serrure de l'Entrée verrouiller

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Verrouille la serrure Nuki de l'entrée.

**Fonctionnement :**
1. Appelle `lock.lock` sur `lock.serrure_de_l_entree`.

---

### `script.ios_alarme_activation_absent` — iOS - Alarme Activation (Absent)

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Arme l'alarme en mode absent.

**Fonctionnement :**
1. Appelle `alarm_control_panel.alarm_arm_away` sur `alarm_control_panel.alarme`.

---

### `script.ios_alarme_desactivation` — iOS - Alarme Désactivation

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Désarme l'alarme.

**Fonctionnement :**
1. Appelle `alarm_control_panel.alarm_disarm` sur `alarm_control_panel.alarme`.

---

## Utilitaires

### `script.reload_pyscript` — Reload pyscript

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Recharge l'intégration pyscript sans redémarrer HA.

**Fonctionnement :**
1. Appelle `pyscript.reload`.

---

### `script.delete_all_orphaned_entities` — Delete all orphaned entities

**Statut :** Finalisé | **Evolution :** Aucune

**Rôle :** Supprime toutes les entités orphelines du registre HA (service fourni par l'intégration Spook).

**Fonctionnement :**
1. Appelle `homeassistant.delete_all_orphaned_entities`.
