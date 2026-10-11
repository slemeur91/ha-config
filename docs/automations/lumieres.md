# Lumières (8)

[← Retour README](../../README.md)

---

## `automation.gestion_de_la_lumiere_du_garage` — Lumière du Garage
> [📄 Voir le YAML](../../automations/gestion_de_la_lumiere_du_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Ouverture de la porte du garage (`binary_sensor.do_gar_porte_garage` passe de off à on)

**Fonctionnement :**
1. Si période sombre (de 30 min avant le coucher du soleil à 30 min après le lever) ET que l'alarme est désarmée → allume la lumière du garage.
2. Aucune extinction automatique n'est prévue dans cette automatisation.

**Entités principales :**
- `binary_sensor.do_gar_porte_garage` : porte du garage
- `light.lumiere_du_garage` : lumière commandée
- `alarm_control_panel.alarme` : condition de sécurité

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_du_bouton_hue_central_droit` — Bouton Hue Central Droit
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_central_droit.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Appui sur les 4 boutons du Tap Dial Central Droit (`event.tap_dial_central_droit_bouton_1` à `_4`)
- Rotation de la molette (`event.tap_dial_central_droit_rotatif`) : détectée, aucune action affectée

**Fonctionnement :**
1. Bouton 1 appui long → déclenche la HiFi en mode SOURCE.
2. Bouton 2 appui long → lance les SONOS en mode ON.
3. Bouton 3 appui long → éteint la HiFi.
4. Bouton 4 appui long → éteint les SONOS.
(Les appuis courts sont réservés pour une future affectation lumière.)

**Entités principales :**
- `event.tap_dial_central_droit_bouton_*` / `event.tap_dial_central_droit_rotatif` : événements du Tap Dial
- `input_select.hifi_action` / `input_select.sonos_action` : coordination AV

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.hifi_action` | input_select | ON, SOURCE, OFF |
| `input_select.hifi_source` | input_select | Zappiti, BluRay, slm-media4 |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |

---

## `automation.gestion_du_bouton_hue_central_gauche` — Bouton Hue Central Gauche
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_central_gauche.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Appui sur les 4 boutons du Tap Dial Central Gauche (`event.tap_dial_central_gauche_bouton_1` à `_4`)
- Rotation de la molette (`event.tap_dial_central_gauche_rotatif`) : détectée, aucune action affectée

**Fonctionnement :**
1. Bouton 1 appui long → déclenche la HiFi en mode SOURCE.
2. Bouton 2 appui long → lance les SONOS en mode ON.
3. Bouton 3 appui long → éteint la HiFi.
4. Bouton 4 appui long → éteint les SONOS.
(Les appuis courts sont réservés pour une future affectation lumière.)

**Entités principales :**
- `event.tap_dial_central_gauche_bouton_*` / `event.tap_dial_central_gauche_rotatif` : événements du Tap Dial
- `input_select.hifi_action` / `input_select.sonos_action` : coordination AV

**Entrées utilisées :** Idem Bouton Central Droit.

---

## `automation.gestion_du_bouton_hue_de_l_entree` — Bouton Hue de l'Entrée
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_de_l_entree.yaml)

**Statut :** Finalisé | **Evolution :** En cours d'affectation des actions

**Déclencheurs :**
- Appui sur les 4 boutons du Tap Dial côté Entrée (événements Hue)
- Rotation de la molette (`event.tap_dial_cote_entree_rotatif`) : détectée, aucune action affectée

**Fonctionnement :**
Les appuis courts et longs sont détectés mais aucune action n'est encore affectée : séquences vides pour les appuis longs, action `light.toggle` désactivée et sans cible pour les appuis courts.

**Entités principales :**
- `event.tap_dial_cote_entree_bouton_*` : événements boutons Hue

**Entrées utilisées :** Aucune.

---

## `automation.gestion_du_bouton_hue_de_l_etage` — Bouton Hue de l'Étage
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_de_l_etage.yaml)

**Statut :** Finalisé | **Evolution :** En cours d'affectation des actions

**Déclencheurs :**
- Appui sur les 4 boutons du Tap Dial de l'Étage (événements Hue)
- Rotation de la molette (`event.tap_dial_de_letage_rotatif`) : détectée, aucune action affectée

**Fonctionnement :**
Les appuis courts et longs sont détectés mais aucune action n'est encore affectée : séquences vides pour les appuis longs, action `light.toggle` désactivée et sans cible pour les appuis courts.

**Entités principales :**
- `event.tap_dial_de_letage_bouton_*` : événements boutons Hue

**Entrées utilisées :** Aucune.

---

## `automation.gestion_de_la_lumiere_de_l_entree` — Gestion de la Lumière de l'Entrée
> [📄 Voir le YAML](../../automations/gestion_de_la_lumiere_de_l_entree.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Sonnette du portier (`binary_sensor.exterieur_slm_portier_visiteur` → on)
- Présence devant le portier (`binary_sensor.exterieur_slm_portier_personne` → on)
- Ouverture de la porte d'entrée (`binary_sensor.do_porte_entree`)

**Fonctionnement :**
1. Si période sombre (de 30 min avant le coucher du soleil à 30 min après le lever) → allume `light.lumiere_de_lexterieur`, attend 5 s.
2. Si la lumière est allumée → attend 5 min puis éteint automatiquement.

**Note :** mode `restart` : une nouvelle détection pendant le délai de 5 min relance l'extinction à zéro.

**Entités principales :**
- `binary_sensor.exterieur_slm_portier_visiteur`, `binary_sensor.exterieur_slm_portier_personne`, `binary_sensor.do_porte_entree`
- `light.lumiere_de_lexterieur`

---

## `automation.gestion_de_la_lumiere_du_wc_de_l_etage` — Gestion de la Lumière du WC de l'Étage
> [📄 Voir le YAML](../../automations/gestion_de_la_lumiere_du_wc_de_l_etage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `binary_sensor.presence_dans_le_wc_de_l_etage_presence` (on/off)

**Fonctionnement :**
1. Présence détectée → allume `light.lumiere_du_wc_de_letage` avec un pas de luminosité de +50% en période sombre (de 30 min avant le coucher du soleil à 30 min après le lever), +80% sinon.
2. Absence détectée → éteint `light.lumiere_du_wc_de_letage`.

**Remarque :** l'action utilise `brightness_step_pct` (incrément relatif) et non `brightness_pct` (valeur absolue) ; partant d'une lumière éteinte le résultat est équivalent à 50% / 80%.

**Entités principales :**
- `binary_sensor.presence_dans_le_wc_de_l_etage_presence`
- `light.lumiere_du_wc_de_letage`

---

## `automation.gestion_de_la_lumiere_du_wc_du_rdc` — Gestion de la Lumière du WC du RDC
> [📄 Voir le YAML](../../automations/gestion_de_la_lumiere_du_wc_du_rdc.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `binary_sensor.presence_dans_le_wc_du_rdc_presence` (on/off)

**Fonctionnement :**
1. Présence détectée → allume `light.lumiere_du_wc_du_rdc`.
2. Absence détectée → éteint `light.lumiere_du_wc_du_rdc`.

**Entités principales :**
- `binary_sensor.presence_dans_le_wc_du_rdc_presence`
- `light.lumiere_du_wc_du_rdc`

---

