# Z-Wave (13 appareils)

[← Retour Appareils](../appareils.md)

> 🏠 **Natif HA** via add-on Z-Wave JS UI — [Documentation](https://www.home-assistant.io/integrations/zwave_js/)
> Flux : Z-Wave JS UI (zwavejs2mqtt) → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Pièces |
|---|---|---|---|---|
| 5 | Fibargroup | FGT001 Thermostatic Valve | Tête thermostatique | Bureau, Chambre, Suite parentale, Salle d'eau, Salle de bain |
| 3 | Fibaro | FGFS-101 Flood Sensor | Détecteur d'eau | Salle de bain, Cuisine, Cellier |
| 2 | — | Z-Wave Valve | Vanne motorisée | Arrosage, Arrivée d'eau réseau |
| 1 | — | Z-Wave Switch | Prise connectée | Cellier |
| 2 | — | Z-Wave Multisensor | Capteur température/luminosité | Armoire de brassage, Grenier |

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
