# Z-Wave (25 appareils)

[← Retour Appareils](../appareils.md)

> 🏠 **Natif HA** via add-on Z-Wave JS UI — [Documentation](https://www.home-assistant.io/integrations/zwave_js/)
> Flux : Z-Wave JS UI (zwavejs2mqtt) → Mosquitto MQTT → HA

| Nb | Fabricant | Modèle | Description | Localisation | Documentation |
|---|---|---|---|---|---|
| 1 | AEON Labs | ZW090 Z-Stick Gen5 | Contrôleur USB Z-Wave | Armoire de brassage | [📄 Manuel](<../hardware/Z-Stick Gen5+ user guide _ Aeotec Help Desk.pdf>) |
| 5 | Fibargroup | FGT001 Thermostatic Valve | Tête thermostatique | Bureau, Chambre, Suite parentale, Salle d'eau, Salle de bain | [📄 Manuel](../hardware/FGT-001-S-v1.4-web.pdf) |
| 3 | Fibargroup | FGFS101 Flood Sensor | Détecteur d'eau | Salle de bain, Cuisine, Cellier | [📄 Manuel](../hardware/FGFS-101-FR-A-v1.00.pdf) |
| 2 | Fibargroup | FGMS001 Motion Sensor | Capteur température/luminosité | Armoire de brassage, Grenier | [📄 Manuel](../hardware/FGMS-001-FR-A-v1.01.pdf) |
| 2 | Fibargroup | FGWPE/F-101 Metered Wall Plug Switch | Prise connectée avec mesure | Salon (Canapé gauche, Canapé droite) | [📄 Manuel](../hardware/FGWPx-102-FR-A-v1.00.pdf) |
| 1 | Fibargroup | FGWP102 Metered Wall Plug Switch | Prise connectée avec mesure | Cellier | [📄 Manuel](../hardware/FGWPx-102-FR-A-v1.00.pdf) |
| 1 | ID-RF (NodOn) | CRC-3100 Octan Remote Control | Télécommande Z-Wave 8 boutons | Salon | [📄 Manuel](../hardware/NodOn-CRC-3-1-xx-UserGuide-150609-FR-online.pdf) |
| 1 | UFairy G.R. Tech | DMWV1 Water Main Shut-Off | Vanne d'arrivée d'eau | Cellier | [📄 Manuel](../hardware/4f09da.pdf) |
| 6 | Qubino | ZMNHCD Flush Shutter | Module volet roulant encastré | Bureau, Cellier, Cuisine, Salon, Séjour, Suite parentale | [📄 Manuel](../hardware/Qubino_Flush%20shutter%20PLUS%20user%20manual_V1.1_fra.pdf) |
| 3 | Qubino | ZMNHSD DIN Rail Dimmer | Variateur d'éclairage sur rail DIN | Garage, Entrée, Terrasse | [📄 Manuel](../hardware/qubino_din_dimmer_user_manual_v1.0_eng_1.pdf) |

---

### ⚠️ Capteur de température FGT001 — Contournement Z-Wave JS UI

Le paramètre `[2-112-0-3-1] Temperature Sensor` est une option qui a disparu lors du passage de **Z-Wave JS** vers **Z-Wave JS UI** (zwavejs2mqtt). Ce capteur n'est donc plus remonté automatiquement dans HA.

**Solution :** Dans Z-Wave JS UI, ouvrir chaque périphérique FGT001, aller dans l'onglet **HOME ASSISTANT**, et coller le JSON ci-dessous dans le champ **"Hass Device JSON"**, en remplaçant les 4 occurrences de `nodeID_X` (dans `state_topic`, `topic` de disponibilité, `identifiers` et `unique_id`) par le numéro de nœud réel du périphérique :

- Bureau → node **2**, Chambre → node **6**, Salle de bain → node **5**, Salle d'eau → node **4**, Suite parentale → node **3**

**JSON à copier (adapter les 4 occurrences de `nodeID_X`) :**

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

> ⚠️ **4 occurrences à remplacer** dans ce JSON : `state_topic`, le premier `topic` de disponibilité, `identifiers` et `unique_id`. Ne pas oublier d'adapter aussi le numéro dans `unique_id` (ex: `2-112-0-3-1` → `6-112-0-3-1` pour le node 6).
