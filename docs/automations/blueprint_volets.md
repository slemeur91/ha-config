# Blueprint — Gestion des Volets (9 instances)

[← Retour README](../../README.md)


Blueprint : [`blueprints/Gestion_des_volets.yaml`](../../blueprints/Gestion_des_volets.yaml)

---

## Description du Blueprint

Pilote les volets selon le mode domicile, la météo, le soleil et la présence.

**Déclencheurs :**
- Changement de domicile, mode volets, alerte météo, soleil, capteur soleil, capteur porte
- Fin de timer de dérogation
- Appui sur `input_button.volets_reactivation`

**Fonctionnement :**
1. Timer de dérogation terminé → désactive la dérogation.
2. Mouvement détecté sur le volet → active/désactive la dérogation selon écart position attendue/réelle.
3. Calcule la position attendue selon : alerte rouge → Fermé, vacances → Fermé, nuit → Fermé, mode Été/Hiver, ensoleillement, présence.
4. Applique la position si la porte est fermée et pas de dérogation active.

**Entités globales requises :**
- `input_select.domicile` : Présent / Nuit / Absent / Vacances
- `input_select.volets_mode` : Été / Hiver
- `input_boolean.volets_soleil` : activation mode protection solaire
- `sensor.sun_next_dawn` / `sensor.sun_next_dusk` / `sensor.sun_next_midnight`
- `sensor.91_weather_alert` : alerte météo rouge
- `input_button.volets_reactivation` : réactivation manuelle globale

---

## Instances configurées

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

## Configuration des Entrées globales

| Entrée | Type | Options / Valeur |
|---|---|---|
| `input_select.domicile` | input_select | Absent, Présent, Nuit, Vacances |
| `input_select.volets_mode` | input_select | Été, Hiver |
| `input_boolean.volets_soleil` | input_boolean | on/off |
| `input_button.volets_reactivation` | input_button | — |
| `input_boolean.seul_a_la_maison` | input_boolean | on/off — géré manuellement |
