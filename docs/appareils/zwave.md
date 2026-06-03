# Z-Wave (24 appareils)

[← Retour Appareils](../appareils.md)

> 🏠 **Natif HA** via add-on Z-Wave JS UI — [Documentation](https://www.home-assistant.io/integrations/zwave_js/)
> Flux : Z-Wave JS UI (zwavejs2mqtt) → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 1 | AEON Labs | ZW090 Z-Stick Gen5 | Contrôleur USB Z-Wave | Armoire de brassage |
| 5 | Fibargroup | FGT001 Thermostatic Valve | Tête thermostatique | Bureau, Chambre, Suite parentale, Salle d'eau, Salle de bain |
| 3 | Fibargroup | FGFS101 Flood Sensor | Détecteur d'eau | Salle de bain, Cuisine, Cellier |
| 2 | Fibargroup | FGMS001 Motion Sensor | Capteur température/luminosité | Armoire de brassage, Grenier |
| 1 | Fibargroup | FGWPE/F-101 Metered Wall Plug Switch | Prise connectée avec mesure | Salon (Canapé gauche) |
| 1 | Fibargroup | FGWP102 Metered Wall Plug Switch | Prise connectée avec mesure | Cellier |
| 1 | ID-RF | CRC-3100 Octan Remote Control | Télécommande Z-Wave 8 boutons | Salon |
| 1 | UFairy G.R. Tech | DMWV1 Water Main Shut-Off | Vanne d'arrivée d'eau | Cellier |
| 6 | Qubino | ZMNHCD Flush Shutter | Module volet roulant encastré | Bureau, Cellier, Cuisine, Salon, Séjour, Suite parentale |
| 3 | Qubino | ZMNHSD DIN Rail Dimmer | Variateur d'éclairage sur rail DIN | Garage, Entrée, Terrasse |

---

### ⚠️ Capteur de température FGT001 — Contournement MQTT

Le paramètre `[2-112-0-3-1] Temperature Sensor` ne remonte plus via zwavejs2mqtt pour les vannes FGT001. Le capteur est recréé manuellement via MQTT Discovery.

**Topic :** `homeassistant/binary_sensor/nodeID_2_temperature_sensor/config` (Retain = true)

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

> Adapter `nodeID_2` au numéro de nœud pour chaque vanne. Publier via MQTT Explorer.
