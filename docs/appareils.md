# 🔌 Appareils connectés

[← Retour README](../README.md)

> Ce fichier liste les appareils physiques principaux, groupés par technologie.
> HA enregistre env. 316 entrées "devices" incluant appareils physiques, nœuds de services et intégrations virtuelles.

**Légende :**
- 🏠 **Natif HA** — intégré dans HA core, aucun dépôt supplémentaire
- 🔧 **HACS** — disponible via le catalogue HACS standard, aucun dépôt personnalisé à ajouter
- 📦 **Add-on Apps** — disponible via la boutique d'add-ons Home Assistant

---

## Z-Wave — Local ✅
> 🏠 **Natif HA** via add-on — [Documentation Z-Wave JS](https://www.home-assistant.io/integrations/zwave_js/)
> Z-Wave JS UI (zwavejs2mqtt) → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 5 | Fibargroup | FGT001 Thermostatic Valve | Tête thermostatique Z-Wave | Bureau, Chambre, Suite parentale, Salle d'eau, Salle de bain |
### ⚠️ Capteur de température FGT001 — Contournement MQTT

Le paramètre `[2-112-0-3-1] Temperature Sensor` ne remonte plus via zwavejs2mqtt pour les vannes FGT001. Pour contourner ce problème, le capteur est recréé manuellement via MQTT Discovery.

**Configuration MQTT Discovery à publier** (topic : `homeassistant/binary_sensor/nodeID_2_temperature_sensor/config`) :

```json
{
    "payload_on": "1",
    "payload_off": "0",
    "value_template": "{{ value_json.value | string }}",
    "device_class": "problem",
    "state_topic": "zwave/nodeID_2/112/0/3/1",
    "availability": [
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/nodeID_2/status",
            "value_template": "{{'true' if value_json.value else 'false'}}"
        },
        {
            "topic": "zwave/_CLIENTS/ZWAVE_GATEWAY-Mosquitto/status",
            "value_template": "{{'online' if value_json.value else 'offline'}}"
        },
        {
            "payload_available": "true",
            "payload_not_available": "false",
            "topic": "zwave/driver/status"
        }
    ],
    "availability_mode": "all",
    "json_attributes_topic": "zwave/nodeID_2/112/0/3/1",
    "device": {
        "identifiers": ["zwavejs2mqtt_0xee883d6d_node2"],
        "manufacturer": "Fibargroup",
        "model": "Thermostatic Valve (FGT001)",
        "name": "nodeID_2",
        "sw_version": "4.7"
    },
    "name": "nodeID_2_temperature_sensor",
    "unique_id": "zwavejs2mqtt_0xee883d6d_2-112-0-3-1"
}
```

> ℹ️ Adapter `nodeID_2` au numéro de nœud correspondant pour chaque vanne. Publier via MQTT Explorer sur le topic ci-dessus avec **Retain = true**.


| 1 | Fibaro | FGFS-101 Flood Sensor | Détecteur d'eau Z-Wave | Salle de bain |
| 1 | Fibaro | FGFS-101 Flood Sensor | Détecteur d'eau Z-Wave | Cuisine |
| 1 | Fibaro | FGFS-101 Flood Sensor | Détecteur d'eau Z-Wave | Cellier |
| 1 | — | Z-Wave Valve | Vanne motorisée Z-Wave | Arrosage |
| 1 | — | Z-Wave Switch | Prise connectée Z-Wave | Cellier |
| 1 | — | Z-Wave Multisensor | Capteur température/luminosité | Armoire de brassage |
| 1 | — | Z-Wave Multisensor | Capteur température/luminosité | Grenier |
| 1 | — | Z-Wave Valve | Vanne d'arrivée d'eau | Réseau |

---

## EnOcean — Local ✅
> 📦 **Add-on Apps** — [GitHub EnOcean MQTT](https://github.com/asera-corp/ha-enoceanmqtt)
> EnOcean MQTT add-on → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 1 | — | EnOcean Switch | Contacteur chaudière étage | Réseau |
| 1 | — | EnOcean Smart Plug | Prise connectée avec mesure | Multimédia |
| 1 | — | EnOcean Smart Plug | Prise connectée avec mesure | Réfrigérateur |

---

## Zigbee — Local ✅
> 📦 **Add-on Apps** — [GitHub Zigbee2MQTT](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt)
> Zigbee2MQTT → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 3 | Aqara | FP2 Presence Sensor | Capteur de présence radar mmWave | Bureau, Chambre, Suite parentale |

---

## Philips Hue — Local ✅
> 🏠 **Natif HA** — [Documentation Hue](https://www.home-assistant.io/integrations/hue/)
> Via Hue Bridge local

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 4 | Philips Hue | Tap Dial Switch | Interrupteur 4 boutons + molette | Central Droit, Central Gauche, Entrée, Étage |
| 6 | Philips Hue | Smart Button | Bouton connecté Hue | Suite parentale, WC étage, Palier, Cellier, Chambre, Bureau |
| 1 | Philips Hue | Motion Sensor | Détecteur de mouvement (zone) | — |

---

## Schneider Odace — Local ✅ (via Remote HA)
> 🔧 **HACS** — [GitHub Remote Home-Assistant](https://github.com/custom-components/remote_homeassistant)
> Via Remote Home-Assistant pointant sur une instance HA secondaire

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 2 | Schneider | Odace SFSP | Armoire de toilette connectée | Salle de bain, Salle d'eau |
| 2 | Schneider | Odace SFSP | Plafonnier connecté | Salle de bain, Salle d'eau |

---

## SONOS — Local ✅
> 🏠 **Natif HA** — [Documentation SONOS](https://www.home-assistant.io/integrations/sonos/)
> Via WiFi local

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | SONOS | Era 100 (ou similaire) | Enceinte connectée | Salon |
| 1 | SONOS | Beam | Barre de son | Suite parentale |
| 1 | SONOS | Era 100 (ou similaire) | Enceinte connectée | Salle d'eau |
| 1 | SONOS | Era 100 (ou similaire) | Enceinte connectée | Garage |
| 1 | SONOS | Era 100 (ou similaire) | Enceinte connectée | Salle de bain |

---

## Somfy KLF200 — io-homecontrol — Local ✅
> 🏠 **Natif HA** — [Documentation KLF200](https://www.home-assistant.io/integrations/velux/)
> Via passerelle KLF200 (protocole io-homecontrol)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Somfy | KLF200 | Passerelle io-homecontrol | Armoire réseau |
| 9 | Somfy | Volet io | Volet roulant motorisé io | Bureau, Cellier, Chambre, Cuisine, Salle d'eau, Salle de bain, Salon, Séjour, Suite parentale |
| 3 | Velux | INTEGRA / KIX 300 | Velux motorisé io | Chambre, Salle d'eau, Salle de bain |
| 1 | Somfy | Store io (Pergola) | Store extérieur motorisé io | Terrasse |

---

## Somfy Protexial — Alarme — Local ✅
> 🔧 **HACS** — [GitHub Somfy Protexial](https://github.com/AuroreVgn/somfy-protexial)
> Via protocole propriétaire Somfy Protexial (réseau local)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Somfy | Protexial IO | Centrale d'alarme | — |

---

## Porte de Garage — RTS via GCE RFPlayer — Local ✅
> 🔧 **HACS** — [GitHub HA RFPlayer](https://github.com/gce-electronics/HA_RFPlayer)
> Via GCE Electronics RFPlayer (émission RF 433 MHz)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Somfy | RTS 4 Portal | Porte de garage motorisée RTS | Garage |
| 1 | GCE Electronics | RFPlayer | Émetteur/récepteur RF 433/868 MHz | Armoire de brassage |

---

## Daikin — Local ✅
> 🏠 **Natif HA** — [Documentation Daikin](https://www.home-assistant.io/integrations/daikin/)
> Via WiFi local (découverte zeroconf)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 4 | Daikin | — | Climatiseur réversible WiFi | Bureau, Chambre, Suite parentale, Séjour |

---

## Nuki — Local ✅
> 🏠 **Natif HA** — [Documentation Nuki](https://www.home-assistant.io/integrations/nuki/)
> Via WiFi (Nuki Bridge)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 2 | Nuki | Smart Lock 3.0 Pro | Serrure connectée (Bluetooth + WiFi) | Entrée, Garage |

---

## Netatmo — Cloud ☁️
> 🏠 **Natif HA** — [Documentation Netatmo](https://www.home-assistant.io/integrations/netatmo/)
> Via API cloud Netatmo

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Netatmo | Smart Weather Station | Station météo principale | Salon |
| 4 | Netatmo | Smart Indoor Module | Sonde température/humidité | Bureau, Chambre, Suite parentale, Extérieur |
| 1 | Netatmo | Rain Gauge | Pluviomètre | Extérieur |
| 1 | Netatmo | Wind Gauge | Anémomètre | Extérieur |

---

## Xiaomi MIoT — Local ✅
> 🔧 **HACS** — [GitHub Xiaomi Miot](https://github.com/al-one/hass-xiaomi-miot)
> Via protocole MIoT local (WiFi)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | Xiaomi | 米家PM2.5检测仪 (zhimi.airmonitor.v1) | Moniteur qualité d'air PM2.5 | Salon |
| 1 | Xiaomi | Mi Air Purifier (zhimi.airpurifier.m1) | Purificateur d'air | Salon |

---

## Xiaomi / Roborock — Local ✅
> 🏠 **Natif HA** — [Documentation Xiaomi Miio](https://www.home-assistant.io/integrations/xiaomi_miio/)
> Via protocole local xiaomi_miio (WiFi)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 2 | Xiaomi / Roborock | Mi Robot Vacuum (rockrobo.vacuum.v1) | Aspirateur robot | Étage, Bas |

---

## Dyson — Local ✅
> 🔧 **HACS** — [GitHub Dyson Local](https://github.com/libdyson-wg/ha-dyson)
> Via protocole MQTT local (WiFi)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | Dyson | Pure Cool (527) | Purificateur/ventilateur avec capteurs qualité d'air | Salon |

---

## EcoFlow — Cloud ☁️
> 🔧 **HACS** — [GitHub EcoFlow Cloud](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | EcoFlow | DELTA Max | Batterie de stockage | — |
| 1 | EcoFlow | PowerStream | Micro-onduleur solaire | — |
| 1 | EcoFlow | Smart Plug | Prise connectée | — |

---

## Broadlink — Local ✅
> 🏠 **Natif HA** — [Documentation Broadlink](https://www.home-assistant.io/integrations/broadlink/)
> Via WiFi local

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 2 | Broadlink | RM4 Pro | Télécommande universelle IR/RF | Salon (×2) |

---

## GCE Electronics EcoDevices RT2 — Local ✅
> 🔧 **HACS** — [GitHub Ecodevices RT2](https://github.com/pcourbin/ecodevices_rt2)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | GCE Electronics | EcoDevices RT2 | Mesure consommation multi-circuits | Armoire de brassage |

---

## Sure Petcare — Cloud ☁️
> 🏠 **Natif HA** — [Documentation Sure Petcare](https://www.home-assistant.io/integrations/surepetcare/)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Sure Petcare | SureFlap Microchip Pet Door | Chatière connectée | — |

---

## X-Sense — Cloud ☁️
> 🔧 **HACS** — [GitHub xsense](https://github.com/Jarnsen/ha-xsense-component_test)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | X-Sense | SBS50 | Station de base alarme incendie/CO | — |
| 3 | X-Sense | XS01-WX / SC06-W | Détecteurs de fumée/CO connectés | Séjour, Cellier, Étage |

---

## Sony — Local ✅
> 🏠 **Natif HA** — [Documentation Bravia TV](https://www.home-assistant.io/integrations/braviatv/)
> Via WiFi local

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | Sony | KD-55A1 | Téléviseur OLED 55" | Salon |

---

## Apple TV — Local ✅
> 🏠 **Natif HA** — [Documentation Apple TV](https://www.home-assistant.io/integrations/apple_tv/)
> Via réseau local

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | Apple | Apple TV | Lecteur multimédia | Salon |

---

## Amazon Echo — Cloud ☁️
> 🔧 **HACS** — [GitHub Alexa Media Player](https://github.com/alandtse/alexa_media_player)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | Amazon | Echo Show | Assistant vocal avec écran | — |

---

## Synology — Local ✅
> 🏠 **Natif HA** — [Documentation Synology DSM](https://www.home-assistant.io/integrations/synology_dsm/)
> Via réseau local

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 2 | Synology | NAS | Serveur NAS (slm-disk3, slm-disk4) | Armoire réseau |

---

## Caméras — Local ✅
> Via **Synology Surveillance Station** (pyscript) + **UniFi Protect** natif HA
> 🏠 **Natif HA** (UniFi Protect) — [Documentation UniFi Protect](https://www.home-assistant.io/integrations/unifiprotect/)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 7 | — | IP Camera | Caméras de surveillance (slm-camera1 à 7) | Extérieur / Intérieur |
| 1 | Ubiquiti | UNVR Instant | Enregistreur vidéo réseau | Armoire réseau |

---

## Robot tondeuse — Local ✅
> 🏠 **Natif HA** — [Documentation Husqvarna Automower](https://www.home-assistant.io/integrations/husqvarna_automower/)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Husqvarna | Automower | Robot tondeuse connecté | Jardin |

---

## Multiprises connectées — Local ✅
> 🏠 **Natif HA** (Shelly) — [Documentation Shelly](https://www.home-assistant.io/integrations/shelly/)
> Autres via intégration MQTT ou Tuya

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Shelly | Multiprise (4 prises + USB) | Multiprise connectée avec mesure | — |
| 6 | — | Multiprise 4 prises + 2 USB | Multiprises connectées avec mesure individuelle | Suite parentale, Salon G/D, Garage, Informatique, Bureau |

---

## TP-Link Tapo — Cloud ☁️
> 🏠 **Natif HA** — [Documentation TP-Link Tapo](https://www.home-assistant.io/integrations/tplink/)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | TP-Link | Tapo P100 | Capteur de posture (boîte aux lettres) | Entrée |

---

## Compteurs & Mesure — Cloud ☁️ / Local

| Nb | Fabricant | Modèle | Description | Intégration | Mode |
|---|---|---|---|---|---|
| 1 | Enedis | Linky | Compteur électrique intelligent | 📦 Add-on Apps — [Linky](https://github.com/bokub/linky) | Cloud ☁️ |
| 1 | GrDF | GAZPAR | Compteur gaz communicant | 📦 Add-on Apps — [Gazpar2MQTT](https://github.com/ssenart/gazpar2mqtt) | Cloud ☁️ |
| 1 | — | Capteur Eau froide | Compteur eau froide | MQTT | Local ✅ |
| 1 | — | Capteur Eau chaude | Compteur eau chaude | MQTT | Local ✅ |

---

## Réseau & Infrastructure — Local ✅

| Nb | Fabricant | Modèle | Description | Intégration | Mode |
|---|---|---|---|---|---|
| 1 | Ubiquiti | UniFi | Switch/AP réseau | 🏠 Natif HA — [UniFi Network](https://www.home-assistant.io/integrations/unifi/) | Local ✅ |
| 1 | Orange | Livebox | Box internet | 🔧 HACS — [GitHub](https://github.com/cyr-ius/hass-livebox-component) | Local ✅ |

---

## Résumé par technologie

| Technologie | Nb appareils | Intégration | Mode |
|---|---|---|---|
| Z-Wave | 13 | 🏠 Natif HA | ✅ Local |
| EnOcean | 3 | 📦 Add-on Apps | ✅ Local |
| Zigbee (Aqara) | 3 | 📦 Add-on Apps | ✅ Local |
| Philips Hue (Zigbee) | 11 | 🏠 Natif HA | ✅ Local |
| Schneider Odace (via Remote HA) | 4 | 🔧 HACS | ✅ Local |
| SONOS (WiFi) | 5 | 🏠 Natif HA | ✅ Local |
| Somfy KLF200 io (volets/velux) | 14 | 🏠 Natif HA | ✅ Local |
| Somfy Protexial (alarme) | 1 | 🔧 HACS | ✅ Local |
| Somfy RTS via RFPlayer (porte garage) | 2 | 🔧 HACS | ✅ Local |
| Daikin (WiFi) | 4 | 🏠 Natif HA | ✅ Local |
| Nuki (WiFi/Bluetooth) | 2 | 🏠 Natif HA | ✅ Local |
| Broadlink (WiFi) | 2 | 🏠 Natif HA | ✅ Local |
| Xiaomi MIoT (WiFi) | 2 | 🔧 HACS | ✅ Local |
| Xiaomi miio / Roborock (WiFi) | 2 | 🏠 Natif HA | ✅ Local |
| Dyson Local (WiFi) | 1 | 🔧 HACS | ✅ Local |
| GCE EcoDevices RT2 | 1 | 🔧 HACS | ✅ Local |
| Sony Bravia (WiFi) | 1 | 🏠 Natif HA | ✅ Local |
| Apple TV (WiFi) | 1 | 🏠 Natif HA | ✅ Local |
| Synology NAS (Ethernet) | 2 | 🏠 Natif HA | ✅ Local |
| Caméras IP | 8 | 🏠 Natif HA | ✅ Local |
| Husqvarna (WiFi) | 1 | 🏠 Natif HA | ✅ Local |
| Shelly (WiFi) | 1 | 🏠 Natif HA | ✅ Local |
| Multiprises MQTT | 6 | 🏠 Natif HA | ✅ Local |
| TP-Link Tapo | 1 | 🏠 Natif HA | ✅ Local |
| Netatmo (WiFi) | 7 | 🏠 Natif HA | ☁️ Cloud |
| EcoFlow | 3 | 🔧 HACS | ☁️ Cloud |
| Amazon Echo | 1 | 🔧 HACS | ☁️ Cloud |
| Sure Petcare | 1 | 🏠 Natif HA | ☁️ Cloud |
| X-Sense | 4 | 🔧 HACS | ☁️ Cloud |
| Linky / GAZPAR | 2 | 📦 Add-on Apps | ☁️ Cloud |
