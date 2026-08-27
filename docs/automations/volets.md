# Volets (14)

[← Retour README](../../README.md)


---

## Blueprints

### Gestion des Velux (3 instances)
Blueprint : [`blueprints/Gestion_des_velux.yaml`](../../blueprints/Gestion_des_velux.yaml)

Contrôle intelligent d'un Velux selon la présence, les alertes météo, la protection thermique et la dérogation d'ouverture.

**Déclencheurs :**
- Changement de domicile, mode volets, alerte météo
- Changement d'aube/crépuscule (`sensor.sun_next_dawn` / `sensor.sun_next_dusk`)
- Bouton de fermeture manuelle ou `input_button.volets_reactivation`
- Changement de température extérieure, du chauffage ou de la sonde secondaire
- Changement de position du velux (pour détection d'ouverture manuelle)
- Fin du timer de dérogation

**Fonctionnement :**
1. Timer de dérogation terminé → désactive la dérogation.
2. Mouvement détecté sur le velux → si position > 5 % : active la dérogation + démarre le timer 1h ; si fermé : désactive la dérogation + annule le timer.
3. Fermeture manuelle / réactivation → reset dérogation + annule timer, puis ferme si absence et velux non fermé.
4. Alerte météo Rouge (grêle ou vent violent) → ferme via bouton (si pas de dérogation).
5. Mode Vacances ou Absent → ferme via bouton (si pas de dérogation).
6. Nuit en mode Hiver → ferme via bouton (si pas de dérogation).
7. Protection thermique → ferme si température extérieure > intérieure, ou intérieure < 19,5°C (si pas de dérogation).

> La dérogation bloque toutes les fermetures automatiques pendant 1h dès qu'un velux est ouvert manuellement. Une fermeture via le bouton ou `volets_reactivation` réinitialise la dérogation.

**Entités globales requises :**
- `input_select.domicile` : Présent / Nuit / Absent / Vacances
- `input_select.volets_mode` : Été / Hiver
- `sensor.91_weather_alert` : alerte météo
- `sensor.netatmo_exterieur_temperature` : température extérieure
- `input_button.volets_reactivation` : réactivation manuelle globale

**Helpers à créer par instance :**
- `input_boolean.velux_<nom>_derogation` : flag de dérogation (généré automatiquement depuis le nom)
- `timer.velux_<nom>_timer` : timer de dérogation (durée 1h00)

### Gestion des Volets (9 instances)
Blueprint : [`blueprints/Gestion_des_volets.yaml`](../../blueprints/Gestion_des_volets.yaml)

Pilote les volets selon le mode domicile, la météo, le soleil et la présence.

**Déclencheurs :**
- Changement de domicile, mode volets, alerte météo, capteur soleil, capteur porte
- Changement de position du volet (pour détection de mouvement manuel)
- Fin du timer de dérogation
- Appui sur `input_button.volets_reactivation`

**Fonctionnement :**
1. Timer de dérogation terminé → désactive la dérogation.
2. Mouvement détecté sur le volet (position stable 1 min) → si écart entre position réelle et attendue : active la dérogation + démarre le timer ; sinon désactive la dérogation + annule le timer.
3. Calcule la position attendue :
   - Alerte rouge (grêle ou vent violent) → Fermé
   - Vacances → Fermé
   - Nuit → Fermé
   - Mode Été + soleil + protection solaire active + absent → Fermé ; sinon Ouvert
   - Mode Hiver + soleil + pas Nuit → Ouvert ; si Présent + position_30 activée → Ouvert ; sinon Fermé
4. Applique la position si porte fermée, pas de dérogation active, et (position = Fermé, OU alarme armée-absent, OU alarme désarmée avec absence/seul_a_la_maison).

> L'ouverture automatique n'a lieu que si personne n'est présent dans la pièce (ou si `input_boolean.seul_a_la_maison` est actif). La fermeture s'applique toujours.

**Entités globales requises :**
- `input_select.domicile` : Présent / Nuit / Absent / Vacances
- `input_select.volets_mode` : Été / Hiver
- `input_boolean.volets_soleil` : activation mode protection solaire
- `input_boolean.seul_a_la_maison` : conditionne l'ouverture automatique
- `sensor.sun_next_dawn` / `sensor.sun_next_dusk` / `sensor.sun_next_midnight`
- `sensor.91_weather_alert` : alerte météo
- `alarm_control_panel.alarme` : état alarme (conditionne l'ouverture)
- `input_button.volets_reactivation` : réactivation manuelle globale

---

## Instances configurées

### Velux Chambre
> [📄 Voir le YAML](../../automations/gestion_du_velux_chambre.yaml)
- **Velux cible :** `cover.velux_de_la_chambre`
- **Chauffage associé :** `climate.chauffage_de_la_chambre_nodeid_6_climate`
- **Sonde secondaire :** `sensor.netatmo_chambre_temperature`
- **Présence :** `input_select.presence_chambre`
- **Bouton fermeture :** `input_button.velux_chambre_fermer`
- **Timer dérogation :** `timer.velux_chambre_timer`
- **Dérogation :** `input_boolean.velux_chambre_derogation`
- **Seuil pluie :** `input_number.volet_consigne_risque_de_pluie`

---

### Velux Salle d'eau
> [📄 Voir le YAML](../../automations/gestion_du_velux_salle_d_eau.yaml)
- **Velux cible :** `cover.velux_de_la_salle_d_eau`
- **Chauffage associé :** `climate.chauffage_de_la_salle_d_eau_nodeid_4_climate`
- **Sonde secondaire :** *(optionnel)*
- **Présence :** *(optionnel)*
- **Bouton fermeture :** `input_button.velux_sde_fermer`
- **Timer dérogation :** `timer.velux_salle_d_eau_timer`
- **Dérogation :** `input_boolean.velux_salle_d_eau_derogation`
- **Seuil pluie :** `input_number.volet_consigne_risque_de_pluie`

---

### Velux Salle de bain
> [📄 Voir le YAML](../../automations/gestion_du_velux_salle_de_bain.yaml)
- **Velux cible :** `cover.velux_de_la_salle_de_bain`
- **Chauffage associé :** `climate.chauffage_de_la_salle_de_bain_nodeid_5_climate`
- **Sonde secondaire :** *(optionnel)*
- **Présence :** *(optionnel)*
- **Bouton fermeture :** `input_button.velux_sdb_fermer`
- **Timer dérogation :** `timer.velux_salle_de_bain_timer`
- **Dérogation :** `input_boolean.velux_salle_de_bain_derogation`
- **Seuil pluie :** `input_number.volet_consigne_risque_de_pluie`

---

### Volet Bureau
- **Volet cible :** `cover.volet_du_bureau_nodeid_36_position`
- **Capteur soleil :** `binary_sensor.volet_bureau_soleil`
- **Présence :** `input_select.presence_bureau`
- **Timer :** `timer.volet_bureau_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Oui

> ℹ️ Logique spéciale Bureau : ouverture forcée en mode Présent + TéléTravail quelle que soit l'heure.

**Entrées dédiées :**
- `input_select.volet_bureau_attendu` : Ouvert/Fermé/30
- `input_boolean.volet_bureau_derogation`

---

### Volet Cellier
> [📄 Voir le YAML](../../automations/gestion_du_volet_cellier.yaml)
- **Volet cible :** `cover.volet_du_cellier_nodeid_31_position`
- **Capteur soleil :** `binary_sensor.volet_cellier_soleil`
- **Présence :** *(aucune)*
- **Timer :** `timer.volet_cellier_timer`
- **Capteur porte :** `cover.velux_du_cellier` *(si existant)*
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_cellier_attendu` : position cible (Ouvert/Fermé/30)
- `input_boolean.volet_cellier_derogation` : flag dérogation

---

### Volet Chambre
- **Volet cible :** `cover.volet_de_la_chambre`
- **Capteur soleil :** `binary_sensor.volet_chambre_soleil`
- **Présence :** `input_select.presence_chambre`
- **Timer :** `timer.volet_chambre_timer`
- **Capteur porte :** `cover.velux_de_la_chambre`
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_chambre_attendu` : position cible (Ouvert/Fermé/30)
- `input_boolean.volet_chambre_derogation` : flag dérogation

---

### Volet Cuisine
- **Volet cible :** `cover.volet_de_la_cuisine_nodeid_34_position`
- **Capteur soleil :** `binary_sensor.volet_cuisine_soleil`
- **Présence :** *(aucune)*
- **Timer :** `timer.volet_cuisine_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_cuisine_attendu`
- `input_boolean.volet_cuisine_derogation`

---

### Volet Salle d'eau
- **Volet cible :** `cover.volet_de_la_salle_d_eau`
- **Capteur soleil :** `binary_sensor.volet_salle_d_eau_soleil`
- **Présence :** *(aucune)*
- **Timer :** `timer.volet_sde_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_sde_attendu`
- `input_boolean.volet_sde_derogation`

---

### Volet Salle de bain
- **Volet cible :** `cover.volet_de_la_salle_de_bain`
- **Capteur soleil :** `binary_sensor.volet_salle_de_bain_soleil`
- **Présence :** *(aucune)*
- **Timer :** `timer.volet_sdb_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_sdb_attendu`
- `input_boolean.volet_sdb_derogation`

---

### Volet Salon
- **Volet cible :** `cover.volet_du_salon_nodeid_32_position`
- **Capteur soleil :** `binary_sensor.volet_salon_soleil`
- **Présence :** `input_select.presence_salon`
- **Timer :** `timer.volet_salon_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Oui

**Entrées dédiées :**
- `input_select.volet_salon_attendu` : Ouvert/Fermé/30
- `input_boolean.volet_salon_derogation`

---

### Volet Séjour
- **Volet cible :** `cover.volet_du_sejour_nodeid_33_position`
- **Capteur soleil :** `binary_sensor.volet_sejour_soleil`
- **Présence :** *(aucune)*
- **Timer :** `timer.volet_sejour_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Oui

**Entrées dédiées :**
- `input_select.volet_sejour_attendu` : Ouvert/Fermé/30
- `input_boolean.volet_sejour_derogation`

---

### Volet Suite parentale
- **Volet cible :** `cover.volet_de_la_suite_parentale_nodeid_35_position`
- **Capteur soleil :** `binary_sensor.volet_suite_parentale_soleil`
- **Présence :** `input_select.presence_suite_parentale`
- **Timer :** `timer.volet_suite_parentale_timer`
- **Capteur porte :** *(à compléter)*
- **Position 30 :** Non

**Entrées dédiées :**
- `input_select.volet_suite_parentale_attendu`
- `input_boolean.volet_suite_parentale_derogation`

---

## `automation.suspension_de_l_automatisation_du_volet_de_la_suite_parentale_paliatif_detecteur_do` — Suspension du Volet Suite Parentale — Palliatif détecteur DO
> [📄 Voir le YAML](../../automations/suspension_de_l_automatisation_du_volet_de_la_suite_parentale_paliatif_detecteur_do.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement d'état des ouvertures : `binary_sensor.do_bureau`, `do_cuisine`, `do_salon`, `do_sejour`, `do_vitre_cellier` + `cover.velux_de_la_chambre`, `velux_de_la_salle_d_eau`, `velux_de_la_salle_de_bain`

**Fonctionnement :**
1. Toutes les ouvertures ouvertes (`do_cuisine`/`do_salon`/`do_sejour`/`do_vitre_cellier` via condition native `door.is_open`, `do_bureau` via `window.is_open`, + 3 velux en position > 0) → désactive `automation.gestion_du_volet_suite_parentale`.
2. Dès qu'une ouverture se ferme → réactive `automation.gestion_du_volet_suite_parentale`.

> **Contexte :** Palliatif en l'absence de capteur DO sur la suite parentale. Quand toutes les autres fenêtres sont ouvertes, il est probable que la suite parentale l'est aussi — on suspend l'automatisation du volet pour éviter une fermeture indésirable. Les conditions natives `door.is_open` / `window.is_open` sont utilisées à la place de l'état principal des `binary_sensor.do_*` (qui peut rester bloqué sur une valeur incorrecte, cas observé sur `binary_sensor.do_suite_parental`).

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.volets_ouvrir` — Volets Ouvrir
> [📄 Voir le YAML](../../automations/volets_ouvrir.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheur :**
- Appui sur `input_button.volets_ouvrir`

**Fonctionnement :**
Ouvre les 6 volets non liés à un velux (Cuisine, Suite parentale, Bureau, Cellier, Salon, Séjour) — Chambre, Salle de bain, Salle d'eau exclus.

**Entités principales :**
- `input_button.volets_ouvrir`
- 6 `cover.volet_*` (Cellier, Cuisine, Séjour, Salon, Bureau, Suite parentale)

---

## Configuration des Entrées

### Velux

| Entrée | Type | Options / Valeur |
|---|---|---|
| `input_button.velux_chambre_fermer` | input_button | Fermeture manuelle |
| `input_button.velux_sde_fermer` | input_button | Fermeture manuelle |
| `input_button.velux_sdb_fermer` | input_button | Fermeture manuelle |
| `input_select.presence_chambre` | input_select | Présent, Absent |
| `input_boolean.velux_chambre_derogation` | input_boolean | Flag dérogation Chambre |
| `input_boolean.velux_salle_d_eau_derogation` | input_boolean | Flag dérogation Salle d'eau |
| `input_boolean.velux_salle_de_bain_derogation` | input_boolean | Flag dérogation Salle de bain |
| `timer.velux_chambre_timer` | timer | Dérogation Chambre (1h00) |
| `timer.velux_salle_d_eau_timer` | timer | Dérogation Salle d'eau (1h00) |
| `timer.velux_salle_de_bain_timer` | timer | Dérogation Salle de bain (1h00) |

### Volets — globales

| Entrée | Type | Options / Valeur |
|---|---|---|
| `input_select.domicile` | input_select | Absent, Présent, Nuit, Vacances |
| `input_select.volets_mode` | input_select | Été, Hiver |
| `input_boolean.volets_soleil` | input_boolean | on/off |
| `input_button.volets_reactivation` | input_button | — |
| `input_boolean.seul_a_la_maison` | input_boolean | on/off — géré manuellement |
