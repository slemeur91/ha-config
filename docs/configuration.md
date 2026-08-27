# ⚙️ Configuration principale — configuration.yaml

[← Retour README](../README.md)

---

## 🐛 Débogage — Logger

Configuration à activer temporairement dans `configuration.yaml` pour le diagnostic.

```yaml
logger:
  default: info
  logs:
    custom_components.somfy_protexial: debug
    custom_components.local_agenda: debug
#    components.husqvarna_automower_ble: debug
    homeassistant.components.apple_tv: debug
    pyatv: debug
```

---

## 🚨 Événements de log — System Log

Nécessaire pour que l'automatisation [Surveillance - Automatisations et Scripts en Défaut](automations/alertes_notifications.md) puisse détecter les erreurs : par défaut, `fire_event` est à `false` et l'événement `system_log_event` n'est jamais émis sur le bus, donc aucun trigger basé sur cet événement ne se déclenche (testé et confirmé le 19/06/2026).

```yaml
system_log:
  fire_event: true
```

**Redémarrage requis** après ajout (composant non rechargeable à chaud).

---

## 🏠 Personnalisation — Homeassistant

Packages et correction de `state_class` sur les capteurs d'énergie (Zigbee, Z-Wave, EnOcean) pour les rendre compatibles avec le tableau de bord Énergie de HA.

Le bloc `customize:` est externalisé dans un fichier dédié `customize.yaml` (à la racine de la config HA, au même niveau que `configuration.yaml`) pour garder `configuration.yaml` lisible :

```yaml
homeassistant:
  packages: !include_dir_named packages
  customize: !include customize.yaml
```

**`customize.yaml` :**

```yaml
sensor.contacteur_de_la_chaudiere_energy:
  state_class: total
sensor.contacteur_de_la_climatisation_energy:
  state_class: total
sensor.contacteur_du_four_energy:
  state_class: total
sensor.prise_de_l_entree_energy:
  state_class: total
sensor.prise_de_l_informatique_energy:
  state_class: total
sensor.prise_de_la_cafetiere_energy:
  state_class: total
sensor.prise_de_la_chambre_energy:
  state_class: total
sensor.prise_de_la_hotte_energy:
  state_class: total
sensor.prise_de_la_salle_d_eau_energy:
  state_class: total
sensor.prise_de_la_salle_de_bain_energy:
  state_class: total
sensor.prise_de_la_television_energy:
  state_class: total
sensor.prise_du_bureau_energy:
  state_class: total
sensor.prise_du_garage_energy:
  state_class: total
sensor.prise_du_jus_d_orange_energy:
  state_class: total
sensor.prise_du_poele_energy:
  state_class: total
sensor.lumiere_de_l_entree_electric_consumption_kwh:
  state_class: total
sensor.lumiere_de_la_terrasse_electric_consumption_kwh:
  state_class: total
sensor.lumiere_du_garage_electric_consumption_kwh:
  state_class: total
sensor.prise_du_canape_droite_purificateur_electric_consumption_kwh:
  state_class: total
sensor.prise_du_canape_gauche_chats_electric_consumption_kwh:
  state_class: total
sensor.prise_du_cellier_electric_consumption_kwh:
  state_class: total
sensor.prise_du_cellier_electric_kwh:
  state_class: total
sensor.volet_de_la_cuisine_electric_consumption_kwh:
  state_class: total
sensor.volet_de_la_suite_parentale_electric_consumption_kwh:
  state_class: total
sensor.volet_du_bureau_electric_consumption_kwh:
  state_class: total
sensor.volet_du_cellier_electric_consumption_kwh:
  state_class: total
sensor.volet_du_salon_electric_consumption_kwh:
  state_class: total
sensor.volet_du_sejour_electric_consumption_kwh:
  state_class: total
cover.storepergola:
  templates:
    icon_color: >
      ${ states ['cover.storepergola'].attributes.current_position === 100 ? return 'black' : return 'purple' }
```

---
