# Blueprint — Gestion des Velux (3 instances)

[← Retour README](../../README.md)


Blueprint : [`blueprints/Gestion_des_velux.yaml`](../../blueprints/Gestion_des_velux.yaml)

---

## Description du Blueprint

Contrôle intelligent d'un Velux selon la présence, les alertes météo et la protection thermique.

**Déclencheurs :**
- Changement de domicile, mode volets, alerte météo
- Bouton de fermeture manuelle ou `input_button.volets_reactivation`
- Changement de température extérieure, du chauffage ou de la sonde secondaire

**Fonctionnement :**
1. Fermeture manuelle / réactivation → ferme si absence et velux non fermé.
2. Alerte météo Rouge → ferme le velux.
3. Mode Vacances ou Absent → ferme le velux.
4. Protection thermique → ferme si température extérieure > intérieure, ou intérieure < 19,5°C.

**Entités globales requises :**
- `input_select.domicile` : Présent / Nuit / Absent / Vacances
- `sensor.91_weather_alert` : alerte météo rouge
- `sensor.netatmo_exterieur_temperature` : température extérieure
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

---

### Velux Salle d'eau
> [📄 Voir le YAML](../../automations/gestion_du_velux_salle_d_eau.yaml)
- **Velux cible :** `cover.velux_de_la_salle_d_eau`
- **Chauffage associé :** `climate.chauffage_de_la_salle_d_eau_nodeid_4_climate`
- **Sonde secondaire :** *(optionnel)*
- **Présence :** *(optionnel)*
- **Bouton fermeture :** `input_button.velux_sde_fermer`

---

### Velux Salle de bain
> [📄 Voir le YAML](../../automations/gestion_du_velux_salle_de_bain.yaml)
- **Velux cible :** `cover.velux_de_la_salle_de_bain`
- **Chauffage associé :** `climate.chauffage_de_la_salle_de_bain_nodeid_5_climate`
- **Sonde secondaire :** *(optionnel)*
- **Présence :** *(optionnel)*
- **Bouton fermeture :** `input_button.velux_sdb_fermer`

---

## Configuration des Entrées

| Entrée | Type | Options / Valeur |
|---|---|---|
| `input_button.velux_chambre_fermer` | input_button | Fermeture manuelle |
| `input_button.velux_sde_fermer` | input_button | Fermeture manuelle |
| `input_button.velux_sdb_fermer` | input_button | Fermeture manuelle |
| `input_select.presence_chambre` | input_select | Présent, Absent |

> ⚠️ **Bug connu** : le trigger `temp_secondaire` surveille `attribute: current_temperature` qui n'existe pas sur un sensor. La température secondaire ne déclenchera pas l'automation directement (les autres triggers corrigent la situation).
