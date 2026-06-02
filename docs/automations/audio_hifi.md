# Audio & HiFi

[← Retour README](../../README.md)

---

## `automation.gestion_des_sonos` — Gestion des SONOS

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.sonos_action`
- Fin de `timer.sonos_timer`
- Appui sur `input_button.sonos`

**Fonctionnement :**
1. Annule le timer si actif.
2. Timer → bascule sur l'action différée si COUCHE ou REVEIL.
3. ON → dégroupage, volumes, radio salon (+garage si TéléTravail), état=ON.
4. OFF → arrêt musique selon contexte, état=OFF.
5. Guard iPhone absent → bloque COUCHE et REVEIL si téléphone non détecté.
6. COUCHE → volumes, jointure suite+sde, radio suite, timer 90 min.
7. REVEIL → volumes, jointure salon+suite+sde, radio salon, timer variable.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.sonos` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |
| `input_select.sonos_delay_action` | input_select | ON, OFF |
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `timer.sonos_timer` | timer | Durée variable |
| `input_number.volume_sonos_base` | input_number | min:0, max:1, step:0.01 |
| `input_button.sonos` | input_button | — |

---

## `automation.gestion_de_la_hifi` — Gestion de la HiFi

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.hifi_action`
- Appui sur `input_button.hifi`

**Fonctionnement :**
1. OFF → extinction (Sony, Rotel, Apple TV, Zappiti si allumé), gestion SONOS selon contexte.
2. ON → vérification horaires/présence, sélection source, passe en SOURCE.
3. SOURCE → SONOS, notification vocale, allumage (Sony, Rotel, HDMI3, Apple TV, lumière salon).

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
