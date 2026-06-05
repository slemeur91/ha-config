# Intégrations (WiFi, Ethernet RJ45 & Autres) — 145 appareils

[← Retour Appareils](../appareils.md)

---

## Audio — SONOS (5 appareils)

> 🏠 **Natif HA** — Intégration : **Sonos** — [Documentation](https://www.home-assistant.io/integrations/sonos/)

| Nb | Modèle | Localisation | Connexion |
|---|---|---|---|
| 3 | Sonos One | Salle de bain, Séjour (×2 groupés), Salle d'eau | 🔌 Ethernet (RJ45) |
| 1 | Sonos Beam | Suite parentale | 🔌 Ethernet (RJ45) |
| 1 | Sonos Move | Bureau (nommé "Garage") | 📶 WiFi |

> ℹ️ Le Séjour dispose de 2 enceintes One groupées, comptées comme 1 dans HA.

---

## Climatisation — Daikin (4 appareils)

> 🏠 **Natif HA** — Intégration : **Daikin** — [Documentation](https://www.home-assistant.io/integrations/daikin/)

| Nb | Modèle | Gamme | Localisation | Connexion |
|---|---|---|---|---|
| 3 | CTXA15AW | Stylish Blanche R32 | Bureau, Chambre, Suite parentale | 📶 WiFi |
| 1 | FTXA35AW | Stylish Blanche R32 | Séjour | 📶 WiFi |

---

## Multimédia (4 appareils)

> 🏠 **Natif HA** — Intégration : **Bravia TV** (Sony) + **Apple TV**

| Nb | Fabricant | Modèle | Localisation | Connexion | Intégration |
|---|---|---|---|---|---|
| 1 | Sony | KD-55A1 (OLED 55") | Salon | 🔌 Ethernet (RJ45) | Bravia TV |
| 1 | Apple | Apple TV | Salon | 🔌 Ethernet (RJ45) | Apple TV |
| 1 | Broadlink | RM4 Pro | Salon | 📶 WiFi | Broadlink |
| 1 | Broadlink | RM4 Pro | Suite parentale | 📶 WiFi | Broadlink |

---

## Qualité de l'air & Purification (4 appareils)

| Nb | Fabricant | Modèle | Localisation | Connexion | Intégration |
|---|---|---|---|---|---|
| 1 | Xiaomi | 米家PM2.5 (zhimi.airmonitor.v1) | Salon | 📶 WiFi | 🔧 HACS — Xiaomi Miot |
| 1 | Xiaomi | Mi Air Purifier (zhimi.airpurifier.m1) | Salon | 📶 WiFi | 🔧 HACS — Xiaomi Miot |
| 1 | Dyson | Pure Cool (527) | Purificateur/ventilateur | Salon | 📶 WiFi | 🔧 HACS — Dyson Local |
| 1 | Dyson | Pure Cool | Purificateur/ventilateur | Bureau | 📶 WiFi | 🔧 HACS — Dyson Local |

---

## Robots & Automatismes (3 appareils)

| Nb | Fabricant | Modèle | Localisation | Connexion | Intégration |
|---|---|---|---|---|---|
| 2 | Roborock | Mi Robot Vacuum (rockrobo.vacuum.v1) | Étage, Bas | 📶 WiFi | 🏠 Natif HA (Xiaomi Miio) |
| 1 | Husqvarna | Automower | Jardin | 📶 WiFi | 🏠 Natif HA |

---

## Serrures & Accès (2 appareils)

> 🏠 **Natif HA** — Intégration : **Nuki** — [Documentation](https://www.home-assistant.io/integrations/nuki/)

| Nb | Fabricant | Modèle | Localisation | Connexion |
|---|---|---|---|---|
| 2 | Nuki | Smart Lock 3.0 Pro | Entrée, Garage | 📶 WiFi (via Nuki Bridge) |

---

## Météo & Capteurs — Netatmo (7 appareils)

> 🏠 **Natif HA** — Intégration : **Netatmo** — [Documentation](https://www.home-assistant.io/integrations/netatmo/)
> ☁️ Cloud

| Nb | Modèle | Description | Localisation | Connexion |
|---|---|---|---|---|
| 1 | Smart Weather Station | Station météo principale | Salon | 📶 WiFi → ☁️ Cloud |
| 4 | Smart Indoor Module | Sonde température/humidité | Bureau, Chambre, Suite parentale, Extérieur | Protocole propriétaire → Station |
| 1 | Rain Gauge | Pluviomètre | Extérieur | Protocole propriétaire → Station |
| 1 | Wind Gauge | Anémomètre | Extérieur | Protocole propriétaire → Station |

---

## Énergie — EcoFlow (2 appareils cloud)

> 🔧 **HACS Communauté** — Intégration : **EcoFlow Cloud**
> ☁️ Cloud

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 1 | DELTA Max | Batterie de stockage | Réseau |
| 1 | PowerStream | Micro-onduleur solaire | Extérieur |

---

## Énergie — Compteurs & Mesure (24 appareils)

### Linky & GAZPAR (2 appareils)

| Nb | Fabricant | Modèle | Intégration | Mode |
|---|---|---|---|---|
| 1 | Enedis | Linky | 📦 Add-on [Linky](https://github.com/bokub/linky) | ☁️ Cloud |
| 1 | GrDF | GAZPAR | 📦 Add-on [Gazpar2MQTT](https://github.com/ssenart/gazpar2mqtt) | ☁️ Cloud |

### GCE EcoDevices RT2 (22 appareils de mesure)

> 🔧 **HACS** — Intégration : **Ecodevices RT2** — [GitHub](https://github.com/pcourbin/ecodevices_rt2)
> 🔌 Ethernet (RJ45)

| Nom | Type | Localisation |
|---|---|---|
| Armoire Ecodevice RT2 | Poste consommation | Garage |
| Autre PC | Poste consommation | Consommation |
| Cabane | Poste consommation | Extérieur |
| Chaudière | Poste consommation | Cellier |
| Chauffe eau | Poste consommation | Cellier |
| Compteur Eau Chaude | Compteur impulsion eau | Cellier |
| Compteur Eau froide | Compteur impulsion eau | Cellier |
| Compteur GAZ | Compteur impulsion gaz | Extérieur |
| EcoRT2 | Passerelle | Garage |
| Eclairage | Poste consommation | Consommation |
| Four | Poste consommation | Cuisine |
| Index Base (EDF Info) | Télé-information | Garage |
| PC Cuisine+Ext | Poste consommation | Cuisine |
| PC Lave vaisselle | Poste consommation | Cuisine |
| PC LL et SL | Poste consommation | Salle de bain |
| PC Poêle | Poste consommation | Séjour |
| PC Réseau | Poste consommation | Réseau |
| Plaque | Poste consommation | Cuisine |
| Production | Poste production | Extérieur |
| Tele-Info | Poste | Extérieur |
| VMC | Poste consommation | Grenier |
| Volets | Poste consommation | Consommation |

---

## Prises connectées — Multiprises (6 appareils)

> 🏠 **Natif HA** — Intégration : **Tuya** — [Documentation](https://www.home-assistant.io/integrations/tuya/)
> 📶 WiFi → ☁️ Cloud

| Nb | Fabricant | Description | Localisation | Documentation |
|---|---|---|---|---|
| 6 | Konyks | Multiprise 4 prises + 4 USB | Suite parentale, Salon G, Salon D, Garage, Informatique, Bureau | [📄 Manuel](<../hardware/Konyks - Manuel Polyco v1..1 Update Web.pdf>) |

---

## Caméras & NVR (9 appareils)

> 🏠 **Natif HA** — Intégration : **UniFi Protect** — [Documentation](https://www.home-assistant.io/integrations/unifiprotect/)
> 🔌 Ethernet (RJ45)
> 📹 Enregistrement et analyse vidéo via **Synology Surveillance Station** sur slm-disk4 (DVA1622)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 7 | Synology Surveillance Station | IP Camera | Caméras de surveillance (slm-camera1 à 7) | Extérieur / Intérieur |
| 1 | Synology Surveillance Station | Portier IP | Portier vidéo | Entrée |
| 1 | Ubiquiti | UNVR Instant | Enregistreur vidéo réseau | Armoire réseau |

---

## Infrastructure & NAS (5 appareils)

> 🔌 Ethernet (RJ45)

| Nb | Fabricant | Modèle | Nom | Description | Intégration |
|---|---|---|---|---|---|
| 1 | Synology | DS916+ | slm-disk3 | Serveur NAS | 🏠 Natif HA — Synology DSM |
| 1 | Synology | DVA1622 | slm-disk4 | Serveur NAS + Surveillance Station | 🏠 Natif HA — Synology DSM |
| 1 | Ubiquiti | Cloud Gateway Fiber | — | Routeur | 🏠 Natif HA — UniFi Network |
| 1 | Ubiquiti | U7 Pro | — | Point d'accès WiFi | 🏠 Natif HA — UniFi Network |
| 1 | Orange | Livebox 7 | — | Box internet | 🔧 HACS — [Orange Livebox](https://github.com/cyr-ius/hass-livebox-component) |

---

## Philips Hue — via Hue Bridge (31 appareils)

> 🏠 **Natif HA** — Intégration : **Philips Hue** — [Documentation](https://www.home-assistant.io/integrations/hue/)
> Les appareils communiquent en Zigbee avec le pont Hue Bridge (RJ45, Réseau). HA accède aux appareils via l'intégration Hue, pas directement en Zigbee.

### Contrôles (11 appareils)

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 4 | Hue tap dial switch | Interrupteur 4 boutons + molette | Central Droit (Cuisine), Central Gauche (Cuisine), côté Entrée, Étage (Palier) |
| 2 | Hue Smart button | Bouton connecté | Cellier (×2) |
| 1 | Hue Smart button | Bouton connecté | Bureau |
| 1 | Hue Smart button | Bouton connecté | Suite parentale |
| 1 | Hue Smart button | Bouton connecté | Chambre |
| 1 | Hue Smart button | Bouton connecté | Palier |
| 1 | Hue Smart button | Bouton connecté | WC Étage |

### Lumières (20 appareils)

> ℹ️ Les modèles et regroupements seront complétés ultérieurement.

| Nb | Fabricant | Modèle | Nom HA / Description | Localisation | Documentation |
|---|---|---|---|---|---|
| 1 | Signify | Hue Tento ambiance panel | Lumière du Bureau | Bureau | — |
| 1 | Signify | Hue Tento color panel | Lumière de la Chambre | Chambre | — |
| 1 | Signify | Hue Tento ambiance panel | Lumière de la Suite parentale | Suite parentale | — |
| 1 | Signify | Hue Aurelle Panel | Lumière du Séjour | Séjour | — |
| 4 | Signify | Hue ambiance candle | Lumière de la Cuisine 1 à 4 | Cuisine *(zone)* | — |
| 2 | Signify | Hue ambiance candle | Lumière du Palier 1, 2 | Palier *(zone)* | — |
| 1 | Signify | Hue ambiance lamp | Lumière du WC de l'Étage | WC Étage | — |
| 1 | Signify | Hue ambiance lamp | Lumière du Cellier | Cellier | — |
| 1 | Signify | Hue ambiance lamp | Lumière de l'Extérieur | Extérieur | — |
| 1 | Sunricher | On/Off | Lumière de l'Escalier | Escalier | [📄 Manuel](../hardware/SR-ZG9100A.pdf) |
| 1 | Sunricher | On/Off | Lumière du WC du RDC | WC RDC | [📄 Manuel](../hardware/SR-ZG9100A.pdf) |
| 1 | Sunricher | On/Off | Lumière du Dressing | Dressing | [📄 Manuel](../hardware/SR-ZG9100A.pdf) |
| 1 | Sunricher | On/Off | Lumière du Meuble de la Cuisine | Cuisine | [📄 Manuel](../hardware/SR-ZG9100A.pdf) |
| 1 | Sunricher | SR-ZG9101SAC-HP-V3 Dimmable | Lumière du Salon | Salon | [📄 Manuel](../hardware/SR-ZG9101SAC-HP-V3-Instruction.pdf) |
| 1 | NodOn | SIN-4-2-20 On/Off (2 sorties) | Lumière de l'Entrée (sortie 1), Lumière du Garage (sortie 2) | Entrée, Garage | [📄 Manuel](../hardware/SIN-4-2-20-FR.pdf) |
| 1 | NodOn | SIN-4-2-20 On/Off (2 sorties) | Lumière de la Terrasse (sortie 2) — sortie 1 vide | Terrasse | [📄 Manuel](../hardware/SIN-4-2-20-FR.pdf) |

---

## Présence — Aqara FP2 (3 appareils)

> 🏠 **Natif HA** — Intégration : **Appareil HomeKit** — [Documentation](https://www.home-assistant.io/integrations/homekit_controller/)
> Les capteurs FP2 sont appairés directement via le protocole HomeKit.

| Nb | Fabricant | Modèle | Description | Localisation | Documentation |
|---|---|---|---|---|---|
| 3 | Aqara | FP2 Presence Sensor | Capteur de présence radar mmWave | Bureau, Chambre, Suite parentale | [📄 Manuel](https://www.aqara.com/en/product/presence-sensor-fp2/) |

---

## Assistants vocaux (1 appareil)

> 🔧 **HACS** — Intégration : **Alexa Media Player**
> ☁️ Cloud

| Nb | Fabricant | Modèle | Localisation |
|---|---|---|---|
| 1 | Amazon | Echo Show | Cuisine |

---

## Sécurité & Détection (6 appareils)

### Sure Petcare (1 appareil)

> 🏠 **Natif HA** — Intégration : **Sure Petcare** — ☁️ Cloud

| Nb | Modèle | Description | Localisation | Connexion |
|---|---|---|---|---|
| 1 | SureFlap Hub | Hub passerelle | Entrée | 🔌 Ethernet (RJ45) → ☁️ Cloud |
| 1 | SureFlap Microchip Pet Door | Chatière connectée | Entrée | Protocole propriétaire → Hub |

### X-Sense (4 appareils)

> 🔧 **HACS Communauté** — Intégration : **xsense** — ☁️ Cloud

| Nb | Modèle | Description | Localisation | Connexion |
|---|---|---|---|---|
| 1 | SBS50 | Station de base alarme incendie/CO | Réseau | 📶 WiFi → ☁️ Cloud |
| 3 | XS01-WX / SC06-W | Détecteurs de fumée/CO | Séjour, Cellier, Étage | Protocole propriétaire → SBS50 |

---

## Autres appareils (26 appareils)

### Somfy io-homecontrol — KLF200 (14 appareils)

> 🏠 **Natif HA** — Intégration : **KLF200 (Velux)** — [Documentation](https://www.home-assistant.io/integrations/velux/)
> Passerelle KLF200 : 🔌 Ethernet (RJ45) → HA
> Appareils : protocole io-homecontrol (radio propriétaire Somfy/Velux)

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 1 | Somfy KLF200 | Passerelle io-homecontrol | Armoire réseau |
| 9 | Somfy Volet io | Volet roulant motorisé | Bureau, Cellier, Chambre, Cuisine, Salle d'eau, Salle de bain, Salon, Séjour, Suite parentale |
| 3 | Velux INTEGRA / KIX 300 | Velux motorisé | Chambre, Salle d'eau, Salle de bain |
| 1 | Somfy Store io | Store extérieur (Pergola) | Terrasse |

---

### Somfy Protexial — Alarme (1 appareil)

> 🔧 **HACS Communauté** — Intégration : **Somfy Protexial** — [GitHub](https://github.com/AuroreVgn/somfy-protexial)
> 🔌 Ethernet (RJ45)

| Nb | Modèle | Description | Documentation |
|---|---|---|---|
| 1 | Somfy Protexial IO | Centrale d'alarme | [📄 Manuel](../hardware/Notice_Protexiom_2014.pdf) |

---

### GCE RFPlayer — RF 433/868 MHz (2 appareils)

> 🔧 **HACS Communauté** — Intégration : **RfPlayer** — [GitHub](https://github.com/gce-electronics/HA_RFPlayer)
> Contrôleur GCE RFPlayer : 🔌 USB
> Appareil Somfy RTS : protocole radio RTS 433 MHz

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 1 | GCE Electronics RFPlayer | Émetteur/récepteur RF 433/868 MHz | Armoire de brassage |
| 1 | Somfy RTS 4 Portal | Porte de garage motorisée RTS | Garage |

---

### Oral-B — Brosse à dents (1 appareil)

> 🏠 **Natif HA** — Intégration : **Oral-B** — [Documentation](https://www.home-assistant.io/integrations/oral_b/)
> 🔵 Bluetooth

| Nb | Fabricant | Modèle | Localisation |
|---|---|---|---|
| 1 | Oral-B | IO Series 6/7 | Salle d'eau |

---

### Schneider Odace SFSP — via Remote HA (8 appareils)

> 🔵 Bluetooth
> Intégration personnelle : **Odace SFSP** — [GitHub slemeur91/odace_sfsp](https://github.com/slemeur91/odace_sfsp) sur l'instance HA secondaire
> Remontée dans cette instance via 🔧 **HACS** — **Remote Home-Assistant** — [GitHub](https://github.com/custom-components/remote_homeassistant)

| Nb | Modèle | Description | Localisation | Documentation |
|---|---|---|---|---|
| 2 | DCL | Armoire de toilette connectée | Salle de bain, Salle d'eau | [📄 Notice DCL](../hardware/notice_DCL.pdf) |
| 2 | DCL | Plafonnier connecté | Salle de bain, Salle d'eau | [📄 Notice DCL](../hardware/notice_DCL.pdf) |
| 2 | Switch | Interrupteur armoire de toilette | Salle de bain, Salle d'eau | [📄 Manuel](../hardware/GDE33208-0026Sept19.pdf) |
| 2 | Switch | Interrupteur plafonnier | Salle de bain, Salle d'eau | [📄 Manuel](../hardware/GDE33208-0026Sept19.pdf) |
