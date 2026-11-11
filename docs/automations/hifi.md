# HiFi (3)

[← Retour README](../../README.md)

---

## `automation.gestion_de_la_hifi` — Gestion de la HiFi
> [📄 Voir le YAML](../../automations/gestion_de_la_hifi.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.hifi_action` (ON / SOURCE / OFF)
- Appui sur `input_button.hifi`

**Fonctionnement :**
1. Action OFF → notification vocale, puis extinction en parallèle : télécommande TV Sony (si allumée), ampli Rotel (`script.allumer_eteindre_amplificateur_rotel`, action off), Apple TV (`media_player.turn_off` direct), Zappiti si allumé, alimentation de la Sync Box et bandeau Hue Play. Gestion SONOS selon contexte : alarme armée (absent) → SONOS OFF ; alarme désarmée entre 05:30 et 22:30 → SONOS ON. Enfin `input_select.hifi` passe à OFF.
2. Action ON → s'arrête sans rien faire avant 10:30 (et selon présence salon/bureau la nuit) ; sinon, si l'iPhone de Sylvain est au domicile, sélectionne la source BluRay et passe en SOURCE ; sinon attend 1 min et réessaie une fois.
3. Action SOURCE → notification vocale, puis en parallèle : SONOS OFF, allumage du Zappiti ou de slm-media4 selon la source, TV sur HDMI3, ampli Rotel (`script.allumer_eteindre_amplificateur_rotel`, action on), Apple TV (`media_player.turn_on` direct), lumière du salon à partir de 30 min avant le coucher du soleil, synchronisation des lumières de la Sync Box sur la sortie HDMI 4. Enfin `input_select.hifi` prend la valeur de la source.

**Remarque :** l'appel groupé à `script.allumer_eteindre_apple_tv_salon` est désactivé dans les deux branches ; l'Apple TV est pilotée directement via `media_player.apple_tv_du_salon`.

**Entités principales :**
- `input_select.hifi` : état courant de la HiFi
- `input_select.hifi_action` : commande entrante
- `input_select.hifi_source` : source active (Zappiti / BluRay / slm-media4)
- `remote.sony_kd_55a1`, `button.tv_hdmi3` : TV Sony
- `script.allumer_eteindre_amplificateur_rotel` : ampli Rotel
- `media_player.apple_tv_du_salon` : Apple TV
- `switch.sync_box_alimentation`, `switch.sync_box_synchronisation_des_lumieres`, `select.sync_box_sortie_hdmi`, `light.hue_play_gradient_lightstrip_1` : Sync Box et bandeau Hue
- `input_select.sonos` / `input_select.sonos_action` : coordination avec les SONOS

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.hifi` | input_select | Zappiti, BluRay, slm-media4, OFF |
| `input_select.hifi_action` | input_select | ON, SOURCE, OFF |
| `input_select.hifi_source` | input_select | Zappiti, BluRay, slm-media4 |
| `input_select.sonos` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.presence_salon` | input_select | Présent, Absent |
| `input_select.presence_bureau` | input_select | Présent, Absent |
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_button.hifi` | input_button | — |

---

## `automation.gestion_de_la_telecommande_hifi` — Télécommande HiFi (Z-Wave)
> [📄 Voir le YAML](../../automations/gestion_de_la_telecommande_hifi.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement des capteurs de scène Z-Wave (boutons 1 à 4)

**Fonctionnement :**
- Bouton 1 (court) → Source BluRay / HiFi SOURCE
- Bouton 2 (court) → SONOS ON
- Bouton 3 (court) → HiFi OFF
- Bouton 4 (court) → SONOS OFF

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.hifi_action` | input_select | ON, SOURCE, OFF |
| `input_select.hifi_source` | input_select | Zappiti, BluRay, slm-media4 |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |

---

## `automation.gestion_des_enceintes` — Gestion des enceintes
> [📄 Voir le YAML](../../automations/gestion_des_enceintes.yaml)

**Statut :** En test | **Evolution :** Remplace « Gestion des SONOS » et les scripts « SONOS Radio sur … »

Un seul groupe Music Assistant à membres dynamiques, `media_player.enceintes`, rempli selon le mode. Au repos, il ne contient que le Salon.
- ON → Salon, Voltage ; en TéléTravail, Garage sur le favori Sonos VOLTAGE
- COUCHE → Suite parentale + Salle d'eau, Voltage entre 4h et 20h30, sinon Évasion FM, timer 90 min
- REVEIL → Salon + Suite parentale + Salle d'eau, Voltage ; timer 80 min (TéléTravail) / 135 min. Le Garage n'est pas touché par le réveil
- OFF → arrêt, le groupe revient au Salon seul

**Déclencheurs :** `input_select.sonos_action`, fin de `timer.sonos_timer`, `input_button.sonos`.

**Fonctionnement :** à chaque changement de mode : arrêt de la lecture, remise de TOUTES les enceintes à leur volume par défaut (base `input_number.volume_sonos_base` ; Garage -0.04 ; Salon et Suite parentale +0.01 ; Salle d'eau et Salle de bain = base) avec sourdine désactivée, composition du groupe (ajout des enceintes voulues, pause de 2 s, puis retrait des autres), lancement de la radio sur le groupe avec une nouvelle tentative après 5 s.

**Garage :** piloté hors Music Assistant par l'intégration Sonos native (`media_player.garage`), car il est en Wi-Fi sur un autre réseau où MA ne peut ni le grouper ni lui envoyer de flux. Il est arrêté à chaque changement de mode (sauf REVEIL, qui ne le touche pas) et ne fait jamais partie du groupe ; il n'est donc pas synchronisé avec les autres pièces.

**Prérequis :** les enceintes ne doivent appartenir à aucun autre groupe Music Assistant, sinon le retrait (`media_player.unjoin`) est redirigé vers cet autre groupe.

**Entités principales :** `media_player.enceintes`, `media_player.salon_3`, `media_player.garage` (Sonos natif), `media_player.suite_parentale_3`, `media_player.salle_d_eau_3`, `media_player.salle_de_bain_3`, `input_select.sonos`, `input_select.sonos_action`, `input_select.sonos_delay_action`, `input_select.calendrier`, `input_number.volume_sonos_base`, `timer.sonos_timer`, `device_tracker.iphone_de_sylvain_le_meur`
