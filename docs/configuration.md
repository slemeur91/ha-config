# ⚙️ Configuration principale — configuration.yaml

[← Retour README](../README.md)

---

## 📧 Notifications — SMTP (email)

Déclaré dans `configuration.yaml` sous la clé `notify`.

```yaml
notify:
  - name: "email"
    platform: smtp
    server: "votre-serveur.domaine.fr"
    port: 25
    timeout: 15
    user: "votre-utilisateur"
    password: "[MOT_DE_PASSE]"
    encryption: none
    sender_name: "Home Assistant"
    sender: "votre-email@domaine.fr"
    recipient: "votre-email@domaine.fr"
```

**Utilisation :** Le service `notify.email` est appelé par les scripts `notification_mail` et `notification_snapshot` pour envoyer des alertes, des récapitulatifs batteries, et des captures caméras.

**Serveur :** SMTP local auto-hébergé (NAS Synology), sans chiffrement (port 25, réseau interne).

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

## 🏠 Personnalisation — Homeassistant

Packages et correction de `state_class` sur les capteurs d'énergie (Zigbee, Z-Wave, EnOcean) pour les rendre compatibles avec le tableau de bord Énergie de HA.

```yaml
homeassistant:
  packages: !include_dir_named packages
  customize:
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
```

---
