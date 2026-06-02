# 📦 Modules complémentaires (Add-ons)

17 add-ons installés. [← Retour README](../README.md)

---

## Add-ons officiels (dépôt `core`)

### Matter Server `8.5.0`
Serveur WebSocket pour le support Matter dans Home Assistant.
- Utilisé par l'intégration Matter native de HA.

### File editor `6.0.0`
Éditeur de fichiers basé sur le navigateur.
- Permet d'éditer les fichiers de configuration directement depuis l'interface HA.

### Terminal & SSH `10.2.0`
Accès SSH à Home Assistant.
- Utilisé pour les opérations de maintenance avancées.

### Z-Wave JS `1.3.0`
Contrôle du réseau Z-Wave via Z-Wave JS.
- Gère les modules Z-Wave (thermostats Fibaro FGT001, détecteurs, volets).

### OpenThread Border Router `3.0.1`
Routeur de bordure OpenThread pour Thread/Matter.
- Permet aux appareils Thread de rejoindre le réseau.

### Mosquitto broker `7.1.0`
Broker MQTT open source.
- Point central pour tous les appareils/add-ons utilisant MQTT (Z-Wave JS UI, Zigbee2MQTT, Gazpar2MQTT, EnOcean).

---

## Add-ons communautaires

### Studio Code Server `6.0.1`
> Dépôt : `a0d7b954`

Visual Studio Code intégré dans l'interface HA.
- Édition avancée des automations, scripts et blueprints.

### Z-Wave JS UI `7.3.0`
> Dépôt : `a0d7b954` — [GitHub](https://github.com/zwave-js/zwave-js-ui)

Interface complète de gestion du réseau Z-Wave.
- Utilisé pour la configuration des modules Z-Wave et la publication MQTT des valeurs.
- Les entités HA sont créées via le broker MQTT (intégration MQTT discovery).

**Configuration spécifique :**
- Broker MQTT : Mosquitto local
- Discovery HA activé
- Réseau Z-Wave : contrôleur USB

### MQTT Explorer `browser-1.0.3`
> Dépôt : `9cf1ea8f` — [GitHub](https://github.com/thomasloven/hassio-mqtt-explorer)

Client MQTT graphique pour inspecter les topics.
- Outil de diagnostic des messages MQTT.

### Home-Assistant-Matter-Hub `2.0.45`
> Dépôt : `3fd9e6b0` — [GitHub](https://github.com/t0bst4r/home-assistant-matter-hub)

Pont Matter qui publie les entités HA vers les écosystèmes Matter (Alexa, Apple Home, Google Home).

### EnOcean MQTT `3.1.0`
> Dépôt : `f93730fa` — [GitHub](https://github.com/asera-corp/ha-enoceanmqtt)

Passerelle EnOcean → MQTT.
- Intègre les appareils EnOcean dans HA via MQTT.

### Homebridge `2026-05-22`
> Dépôt : `0656e7b8` — [GitHub](https://github.com/homebridge/homebridge)

Support HomeKit pour les appareils non supportés nativement.

### Zigbee2MQTT `2.11.0-1`
> Dépôt : `45df7312` — [GitHub](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt)

Passerelle Zigbee sans bridge propriétaire.
- Gère les appareils Zigbee (capteurs de présence Aqara FP2, chatière Sure Petcare, etc.).
- Publication MQTT vers Mosquitto.

### Gazpar2MQTT `0.2.5`
> Dépôt : `dc5bab34` — [GitHub](https://github.com/ssenart/gazpar2mqtt)

Lit les données de consommation gaz depuis GrDF et les publie sur MQTT.

**Configuration spécifique :**
- Compte GrDF : [anonymisé]
- Topic MQTT : `gazpar/[identifiant]`
- Fréquence : quotidienne

### Linky `1.7.0`
> Dépôt : `cf6b56a3` — [GitHub](https://github.com/bokub/linky)

Synchronise les données du compteur Linky avec le tableau de bord Énergie de HA.

### Get HACS `1.3.1`
> Dépôt : `cb646a50`

Installateur HACS. Non actif en production.

### Home Assistant MCP Server `7.6.0`
> Dépôt : `81f33d0f` — [GitHub](https://github.com/voska/hass-mcp)

Expose HA via le protocole MCP (Model Context Protocol) pour l'intégration avec des assistants IA.
