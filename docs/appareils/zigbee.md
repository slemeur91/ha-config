# Zigbee (37 appareils)

[← Retour Appareils](../appareils.md)

---

## Aqara — Présence (3 appareils) — via HomeKit

> Intégration : **HomeKit** — 🏠 Natif HA
> Les capteurs FP2 sont publiés via le protocole HomeKit (pas via Zigbee2MQTT directement).

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 3 | Aqara | FP2 Presence Sensor | Capteur de présence radar mmWave | Bureau, Chambre, Suite parentale |

---

## Philips Hue — via Hue Bridge (31 appareils)

> Intégration : **Philips Hue** — 🏠 Natif HA — [Documentation](https://www.home-assistant.io/integrations/hue/)
> 1 Hue Bridge (Réseau, RJ45) + appareils Zigbee pilotés via le Bridge

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

| Nb | Modèle | Nom HA | Pièce |
|---|---|---|---|
| 1 | Hue Tento ambiance panel | Lumière du Bureau | Bureau |
| 1 | Hue Tento color panel | Lumière de la Chambre | Chambre |
| 1 | Hue Tento ambiance panel | Lumière de la Suite parentale | Suite parentale |
| 1 | Hue Aurelle Panel | Lumière du Séjour | Séjour |
| 4 | Hue ambiance candle | Lumière de la Cuisine 1 à 4 | Cuisine |
| 2 | Hue ambiance candle | Lumière du Palier 1, 2 | Palier |
| 1 | Hue ambiance lamp | Lumière du WC de l'Étage | WC Étage |
| 1 | Hue ambiance lamp | Lumière du Cellier | Cellier |
| 1 | Hue ambiance lamp | Lumière de l'Extérieur | Extérieur |
| 1 | Sunricher On/Off | Lumière de l'Escalier | Escalier |
| 1 | Sunricher On/Off | Lumière du WC du RDC | WC RDC |
| 1 | Sunricher On/Off | Lumière du Dressing | Dressing |
| 1 | Sunricher On/Off | Lumière du Meuble de la Cuisine | Cuisine |
| 1 | Sunricher Dimmable | Lumière du Salon | Salon |
| 1 | NodOn On/Off | Lumières de l'Entrée et du Garage | Garage |
| 1 | NodOn On/Off | Lumières de la Terrasse et Vide | Garage |

---

## Via Zigbee2MQTT (via Add-on Apps) — 23 appareils

> 📦 **Add-on Apps** — Zigbee2MQTT → Mosquitto MQTT → HA

### Prises et multiprises (13 appareils)

| Nb | Fabricant | Modèle | Nom HA | Pièce |
|---|---|---|---|---|
| 12 | Schneider Electric | Zigbee smart socket with power meter | Prise du Bureau, Salle de bain, Télévision, Cafetière, Jus d'orange, Hotte, Salle d'eau, Poêle, Chambre, Entrée, Garage, Informatique | Bureau, SdB, Suite parentale, Cuisine (×3), SdE, Séjour, Chambre, Entrée, Garage, Réseau |
| 1 | UseeLink | 4 gang switch with USB | Multiprise du Salon droite | Salon |

### Multiprises Zigbee (1 appareil)

| Nb | Fabricant | Modèle | Nom HA |
|---|---|---|---|
| 1 | Shelly | Power strip 4 Gen4 | Multiprises Shelly |

### Contacteurs DIN (3 appareils)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 2 | Nous | DIN Switch | Contacteur avec mesure | Garage (Four, Climatisation) |
| 1 | Tongou | Din smart relay | Contacteur avec mesure | Garage (Chaudière) |

### Aqara — Capteur multi-état (1 appareil)

| Nb | Fabricant | Modèle | Description | Localisation |
|---|---|---|---|---|
| 1 | Aqara | P100 Multi-state sensor | Capteur boîte aux lettres (posture/contact) | Extérieur |

### Capteurs divers (2 appareils)

| Nb | Fabricant | Modèle | Description | Pièce |
|---|---|---|---|---|
| 1 | OWON | Temperature sensor | Sonde de température | Placard réseau |
| 1 | Woox | Smart garden irrigation control | Vanne d'arrosage | Extérieur |

