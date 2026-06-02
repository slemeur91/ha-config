# 🛠️ HACS — Intégrations & Cartes Lovelace

[← Retour README](../README.md)

---

## Intégrations (19)

### Alexa Media Player `v5.15.4`
> [GitHub](https://github.com/alandtse/alexa_media_player) — `domain: alexa_media`

Contrôle des appareils Amazon Alexa via l'API non officielle.

---

### Atmo France `V2.1.3`
> [GitHub](https://github.com/sebcaps/atmofrance) — `domain: atmofrance`

Qualité de l'air pour les villes françaises depuis Atmo France.

**Configuration :**
- Ville : [Votre ville]

---

### Battery Notes `3.4.6`
> [GitHub](https://github.com/andrew-codechimp/HA-Battery-Notes) — `domain: battery_notes`

Suivi des types et dates de remplacement des batteries.

**Utilisation :** Automations `battery_low_notification`, `daily_battery_low_check`, `battery_increased_notification`.

---

### Dyson Local `v1.7.0`
> [GitHub](https://github.com/libdyson-wg/ha-dyson) — `domain: dyson_local`

Intégration locale (sans cloud) des appareils Dyson.

**Appareils configurés :**
- Dyson Pure Cool (purificateur Salon) — `fan.salon`
- Dyson Pure Cool (Bureau) — en erreur de connexion

---

### Ecodevices RT2 `v2.2.10`
> [GitHub](https://github.com/pcourbin/ecodevices_rt2) — `domain: ecodevices_rt2`

Intégration pour le module de mesure GCE Ecodevices RT2.

**Configuration :**
- IP : [IP locale]
- Fournit les capteurs de consommation par circuit (réfrigérateur, chaudière, chauffe-eau, production solaire, etc.)

---

### EcoFlow Cloud `v1.1.7`
> [GitHub](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US) — `domain: ecoflow_cloud`

Intégration cloud pour les appareils EcoFlow (batterie DELTA Max + PowerStream).

> ⚠️ Erreur connue : incompatibilité avec la version actuelle de paho-mqtt. Mise à jour requise.

---

### HACS `2.0.5`
> [GitHub](https://github.com/hacs/integration) — `domain: hacs`

Home Assistant Community Store — gestionnaire de contenu communautaire.

---

### Local Agenda `v1.0.3`
> [GitHub](https://github.com/slemeur91/local_agenda) — `domain: local_agenda`

Intégration de calendriers locaux enrichis pour la planification de l'agenda domotique.

**Calendriers configurés :**
- Agenda Travail
- Agenda Télétravail
- Agenda Absent
- Agenda WE-Férié-Repos
- Agenda Permanent

---

### Micronova Agua IOT `1.1.2`
> [GitHub](https://github.com/vincentwolsink/home_assistant_micronova_agua_iot) — `domain: aguaiot`

Contrôle des poêles à granulés connectés via la plateforme Agua IOT.

> ℹ️ Intégration désactivée — la prise de la pellet stove est coupée pour économies d'énergie.

---

### My EcoWatt by RTE `0.9.6`
> [GitHub](https://github.com/kamaradclimber/rte-ecowatt) — `domain: rte_ecowatt`

Données EcoWatt de RTE (signaux de sobriété électrique).

---

### Orange Livebox `2.5.3`
> [GitHub](https://github.com/cyr-ius/hass-livebox-component) — `domain: livebox`

Supervision de la Livebox Orange (état WAN, appareils connectés).

---

### pyscript `2.0.1`
> [GitHub](https://github.com/custom-components/pyscript) — `domain: pyscript`

Scripts Python avancés dans Home Assistant.

**Scripts utilisés :**
- `gazpar_update` : injection des statistiques GAZPAR
- `surveillance_station_recording` : contrôle de l'enregistrement des caméras Synology

---

### Remote Home-Assistant `4.6`
> [GitHub](https://github.com/custom-components/remote_homeassistant) — `domain: remote_homeassistant`

Liaison entre deux instances Home Assistant.

**Configuration :**
- Instance distante : `192.168.51.34:8123` (instance secondaire)

---

### RfPlayer `v1.3.0`
> [GitHub](https://github.com/gce-electronics/HA_RFPlayer) — `domain: rfplayer`

Intégration du module GCE Electronics RFPlayer (réception/émission RF 433/868 MHz).

**Utilisation :** Détection du brouillage réseau RF (`binary_sensor.jamming_0_detector`).

---

### Somfy Protexial `2.0.4`
> [GitHub](https://github.com/AuroreVgn/somfy-protexial) — `domain: somfy_protexial`

Intégration de la centrale d'alarme Somfy Protexial/Protexiom.

**Configuration :**
- URL : `http://[IP locale]:80`
- Entité principale : `alarm_control_panel.alarme`

---

### Spook `v4.0.1`
> [GitHub](https://github.com/frenck/spook) — `domain: spook`

Boîte à outils avancée pour Home Assistant (services supplémentaires, détection entités orphelines).

**Utilisation :** `script.delete_all_orphaned_entities` utilise `homeassistant.delete_all_orphaned_entities` fourni par Spook.

---

### Vacances Scolaires `2.1.9`
> [GitHub](https://github.com/Master13011/vacances-scolaire-HA) — `domain: vacances_scolaires`

Calendrier des vacances scolaires françaises.

**Configuration :**
- Zone : C (Île-de-France)

---

### Xiaomi Miot `v1.1.4`
> [GitHub](https://github.com/al-one/hass-xiaomi-miot) — `domain: xiaomi_miot`

Intégration de tous les appareils Xiaomi/Mi via le protocole MiOT.

**Appareils configurés :**
- Moniteur PM2.5 (米家PM2.5检测仪) — `sensor.zhimi_v1_5052_pm25_density`
- Purificateur Mi Air — `fan.zhimi_m1_6186_air_purifier`

---

### xsense `v.1.2.0`
> [GitHub](https://github.com/Jarnsen/ha-xsense-component_test) — `domain: xsense`

Intégration des appareils X-Sense (station de sécurité SBS50, détecteurs de fumée/CO).

---

## Cartes Lovelace (7)

### apexcharts-card `v2.2.3`
> [GitHub](https://github.com/RomRider/apexcharts-card)

Graphiques avancés basés sur ApexCharts. Utilisé pour les graphiques de consommation énergie.

### Battery State Card `v4.2.0`
> [GitHub](https://github.com/maxwroc/battery-state-card)

Tableau de bord des niveaux de batteries de tous les appareils.

### card-mod `v4.2.1`
> [GitHub](https://github.com/thomasloven/lovelace-card-mod)

Permet d'ajouter du CSS personnalisé à n'importe quelle carte Lovelace.

### Custom-ui `20240118`
> [GitHub](https://github.com/Mariusthvdb/custom-ui)

Templates et couleurs d'icônes personnalisés dans l'interface HA.

### expander-card `7.1.2`
> [GitHub](https://github.com/MelleD/lovelace-expander-card)

Carte extensible/rétractable pour organiser les dashboards.

### GrDF Gazpar card `1.3.11`
> [GitHub](https://github.com/ssenart/lovelace-gazpar-card)

Carte dédiée à l'affichage des données GAZPAR (consommation gaz).

### Waze Travel Time Card `038f2a8`
> [GitHub](https://github.com/r-renato/ha-card-waze-travel-time)

Affiche le temps de trajet calculé par Waze.
