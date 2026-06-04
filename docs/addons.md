# 📦 Modules complémentaires (Add-ons)

17 add-ons installés. [← Retour README](../README.md)

---

## Add-ons officiels (dépôt `core`)

### Matter Server
Serveur WebSocket pour le support Matter dans Home Assistant.
- Utilisé par l'intégration Matter native de HA.

```yaml
log_level: info
log_level_sdk: error
beta: false
enable_test_net_dcl: false
```

### File editor
Éditeur de fichiers basé sur le navigateur.
- Permet d'éditer les fichiers de configuration directement depuis l'interface HA.

### Terminal & SSH
Accès SSH à Home Assistant.
- Utilisé pour les opérations de maintenance avancées.

### Z-Wave JS
Contrôle du réseau Z-Wave via Z-Wave JS.
- ⚠️ **Désactivé automatiquement** par Z-Wave JS UI lors de l'installation de ce dernier. Z-Wave JS UI prend en charge toutes ses fonctions avec en plus la publication MQTT.

```yaml
log_level: info
log_to_file: false
log_max_files: 7
rf_region: Automatic
soft_reset: Automatic
s0_legacy_key: <clé_s0_legacy>
s2_access_control_key: <clé_s2_access_control>
s2_authenticated_key: <clé_s2_authenticated>
s2_unauthenticated_key: <clé_s2_unauthenticated>
lr_s2_access_control_key: <clé_lr_s2_access_control>
lr_s2_authenticated_key: <clé_lr_s2_authenticated>
device: /dev/serial/by-id/usb-0658_0200-if00
network_key: <clé_réseau>
```

### OpenThread Border Router
Routeur de bordure OpenThread pour Thread/Matter.
- Permet aux appareils Thread de rejoindre le réseau.

```yaml
device: /dev/serial/by-id/usb-ITEAD_SONOFF_Zigbee_3.0_USB_Dongle_Plus_V2_20221202105231-if00
baudrate: "460800"
flow_control: true
otbr_log_level: notice
firewall: true
nat64: false
beta: false
autoflash_firmware: true
```

### Mosquitto broker
Broker MQTT open source.
- Point central pour tous les appareils/add-ons utilisant MQTT (Z-Wave JS UI, Zigbee2MQTT, Gazpar2MQTT, EnOcean).

```yaml
logins:
  - username: <utilisateur_mqtt>
    password: <mot_de_passe_mqtt>
log_dest: []
log_type: []
require_certificate: false
certfile: fullchain.pem
keyfile: privkey.pem
customize:
  active: false
  folder: mosquitto
```

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

```yaml
app_log_level: info
disable_log_colors: false
mdns_network_interface: ""
```

### EnOcean MQTT
> Dépôt : `f93730fa` — [GitHub](https://github.com/asera-corp/ha-enoceanmqtt)

Passerelle EnOcean → MQTT.
- Intègre les appareils EnOcean dans HA via MQTT.

```yaml
device_file: /config/enoceanmqtt.devices
enocean_port: /dev/serial/by-id/usb-EnOcean_GmbH_EnOcean_USB_300_DA_FTWTOFZ5-if00-port0
enocean_tcp: ""
mapping_files:
  mapping_file: ""
  eep_file: ""
logging:
  log_file: /config/enoceanmqtt.log
  debug: false
  log_packets: true
mqtt:
  host: core-mosquitto
  port: "1883"
  user: <utilisateur_mqtt>
  pwd: <mot_de_passe_mqtt>
  discovery_prefix: homeassistant
  prefix: enoceanmqtt
  client_id: enocean_gateway
  keepalive: 60
```

### Homebridge
> Dépôt : `0656e7b8` — [GitHub](https://github.com/homebridge/homebridge)

Support HomeKit pour les appareils non supportés nativement.

### Zigbee2MQTT
> Dépôt : `45df7312` — [GitHub](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt)

Passerelle Zigbee sans bridge propriétaire.
- Gère les appareils Zigbee (capteurs de présence Aqara FP2, chatière Sure Petcare, etc.).
- Publication MQTT vers Mosquitto.

```yaml
data_path: /config/zigbee2mqtt
socat:
  enabled: false
  master: pty,raw,echo=0,link=/tmp/ttyZ2M,mode=777
  slave: tcp-listen:8485,keepalive,nodelay,reuseaddr,keepidle=1,keepintvl=1,keepcnt=5
  options: "-d -d"
  log: false
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://core-mosquitto:1883
  user: <utilisateur_mqtt>
  password: <mot_de_passe_mqtt>
serial:
  adapter: ember
  port: /dev/ttyAMA1
  baudrate: 115200
  rtscts: true
```

### Gazpar2MQTT
> Dépôt : `dc5bab34` — [GitHub](https://github.com/ssenart/gazpar2mqtt)

Lit les données de consommation gaz depuis GrDF et les publie sur MQTT.

```yaml
scan_interval: 480
devices:
  - name: GAZPAR Cheptainville
    username: <email_grdf>
    password: <mot_de_passe_grdf>
    pce_identifier: "<identifiant_pce>"
    last_days: 1095
mqtt:
  broker: core-mosquitto
  port: 1883
  username: <utilisateur_mqtt>
  password: <mot_de_passe_mqtt>
  keepalive: 60
  base_topic: gazpar2mqtt
```

### Linky
> Dépôt : `cf6b56a3` — [GitHub](https://github.com/bokub/linky)

Synchronise les données du compteur Linky avec le tableau de bord Énergie de HA.

```yaml
meters:
  - prm: "<prm_linky>"
    token: <token_linky>
    name: Consommation Linky
    action: sync
    production: false
costs: []
```

### Get HACS
> Dépôt : `cb646a50`

Installateur HACS. Non actif en production.

### Home Assistant MCP Server
> Dépôt : `81f33d0f` — [GitHub](https://github.com/voska/hass-mcp)

Expose HA via le protocole MCP (Model Context Protocol) pour l'intégration avec des assistants IA.

```yaml
backup_hint: normal
enable_tool_search: false
tool_search_max_results: 5
enable_tool_security_policies: false
enable_mandatory_bps: true
disabled_tools: ""
pinned_tools: ""
enable_auto_backup: true
auto_backup_throttle_minutes: 0
auto_backup_retain_per_entity: 100
verify_ssl: true
secret_path: /private_<secret>
```
