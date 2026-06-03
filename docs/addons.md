# 📦 Modules complémentaires (Add-ons)

17 add-ons installés. [← Retour README](../README.md)

---

## Add-ons officiels (dépôt `core`)

### Matter Server
Serveur WebSocket pour le support Matter dans Home Assistant.
- Utilisé par l'intégration Matter native de HA.

### File editor
Éditeur de fichiers basé sur le navigateur.
- Permet d'éditer les fichiers de configuration directement depuis l'interface HA.

### Terminal & SSH
Accès SSH à Home Assistant.
- Utilisé pour les opérations de maintenance avancées.

### Z-Wave JS
Contrôle du réseau Z-Wave via Z-Wave JS.
- Gère les modules Z-Wave (thermostats Fibaro FGT001, détecteurs, volets).

### OpenThread Border Router
Routeur de bordure OpenThread pour Thread/Matter.
- Permet aux appareils Thread de rejoindre le réseau.

### Mosquitto broker
Broker MQTT open source.
- Point central pour tous les appareils/add-ons utilisant MQTT (Z-Wave JS UI, Zigbee2MQTT, Gazpar2MQTT, EnOcean).

---

## Add-ons communautaires

### Studio Code Server
> Dépôt : `a0d7b954`

Visual Studio Code intégré dans l'interface HA.
- Édition avancée des automations, scripts et blueprints.

### Z-Wave JS UI
> Dépôt : `a0d7b954` — [GitHub](https://github.com/zwave-js/zwave-js-ui)

Interface complète de gestion du réseau Z-Wave.
- Utilisé pour la configuration des modules Z-Wave et la publication MQTT des valeurs.
- Les entités HA sont créées via le broker MQTT (intégration MQTT discovery).

**Configuration spécifique :**
- Broker MQTT : Mosquitto local
- Discovery HA activé
- Réseau Z-Wave : contrôleur USB

### MQTT Explorer
> Dépôt : `9cf1ea8f` — [GitHub](https://github.com/thomasloven/hassio-mqtt-explorer)

Client MQTT graphique pour inspecter les topics.
- Outil de diagnostic des messages MQTT.

### Home-Assistant-Matter-Hub
> Dépôt : `3fd9e6b0` — [GitHub](https://github.com/t0bst4r/home-assistant-matter-hub)

Pont Matter qui publie les entités HA vers les écosystèmes Matter (Alexa, Apple Home, Google Home).

### EnOcean MQTT
> Dépôt : `f93730fa` — [GitHub](https://github.com/asera-corp/ha-enoceanmqtt)

Passerelle EnOcean → MQTT.
- Intègre les appareils EnOcean dans HA via MQTT.

### Homebridge
> Dépôt : `0656e7b8` — [GitHub](https://github.com/homebridge/homebridge)

Support HomeKit pour les appareils non supportés nativement.

### Zigbee2MQTT
> Dépôt : `45df7312` — [GitHub](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt)

Passerelle Zigbee sans bridge propriétaire.
- Gère les appareils Zigbee (capteurs de présence Aqara FP2, chatière Sure Petcare, etc.).
- Publication MQTT vers Mosquitto.

### Gazpar2MQTT
> Dépôt : `dc5bab34` — [GitHub](https://github.com/ssenart/gazpar2mqtt)

Lit les données de consommation gaz depuis GrDF et les publie sur MQTT.

**Configuration spécifique :**
- Compte GrDF : [anonymisé]
- Topic MQTT : `gazpar/[identifiant]`
- Fréquence : quotidienne

### Linky
> Dépôt : `cf6b56a3` — [GitHub](https://github.com/bokub/linky)

Synchronise les données du compteur Linky avec le tableau de bord Énergie de HA.

### Get HACS
> Dépôt : `cb646a50`

Installateur HACS. Non actif en production.

### Home Assistant MCP Server
> Dépôt : `81f33d0f` — [GitHub](https://github.com/voska/hass-mcp)

Expose HA via le protocole MCP (Model Context Protocol) pour l'intégration avec des assistants IA.
