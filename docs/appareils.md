# 🔌 Appareils connectés

[← Retour README](../README.md)

> HA enregistre env. 316 entrées "devices" incluant appareils physiques, nœuds de services et intégrations virtuelles.

---

## Vue d'ensemble par technologie

| Technologie | Appareils | Mode | Détail |
|---|---|---|---|
| Z-Wave | **23** | ✅ Local | [→ Détail](appareils/zwave.md) |
| Zigbee | **14** | ✅ Local | [→ Détail](appareils/zigbee.md) |
| EnOcean | **3** | ✅ Local | [→ Détail](appareils/enocean.md) |
| WiFi / IP | **54** | ✅ Local + ☁️ Cloud | [→ Détail](appareils/wifi.md) |
| Thread / Matter | **1** | ✅ Local | [→ Détail](#thread--matter) |

---

## Thread / Matter (1 appareil)

> 🏠 **Natif HA** via add-ons Matter Server + Home-Assistant-Matter-Hub
> Infrastructure Thread/Matter en place (OpenThread Border Router)

| Nb | Fabricant | Modèle | Description | Intégration |
|---|---|---|---|---|
| 1 | EcoFlow | Smart Plug | Prise connectée Matter | 🏠 Natif HA (Matter) |

> ℹ️ L'EcoFlow Smart Plug est géré en Matter natif, distinct des autres appareils EcoFlow Cloud.

---

## Autres appareils — par intégration

Ces appareils utilisent des protocoles spécifiques documentés avec leur intégration.

### Somfy io-homecontrol — KLF200 (14 appareils)

> 🏠 **Natif HA** — [Documentation KLF200](https://www.home-assistant.io/integrations/velux/)
> Flux : KLF200 (passerelle locale) → HA

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 1 | Somfy KLF200 | Passerelle io-homecontrol | Armoire réseau |
| 9 | Somfy Volet io | Volet roulant motorisé | Bureau, Cellier, Chambre, Cuisine, Salle d'eau, Salle de bain, Salon, Séjour, Suite parentale |
| 3 | Velux INTEGRA / KIX 300 | Velux motorisé | Chambre, Salle d'eau, Salle de bain |
| 1 | Somfy Store io | Store extérieur (Pergola) | Terrasse |

---

### Somfy Protexial — Alarme (1 appareil)

> 🔧 **HACS Communauté** — [GitHub Somfy Protexial](https://github.com/AuroreVgn/somfy-protexial)

| Nb | Modèle | Description |
|---|---|---|
| 1 | Somfy Protexial IO | Centrale d'alarme |

---

### GCE RFPlayer — RF 433/868 MHz (2 appareils)

> 🔧 **HACS Communauté** — [GitHub HA RFPlayer](https://github.com/gce-electronics/HA_RFPlayer)

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 1 | GCE Electronics RFPlayer | Émetteur/récepteur RF 433/868 MHz | Armoire de brassage |
| 1 | Somfy RTS 4 Portal | Porte de garage motorisée RTS | Garage |

---

### Schneider Odace — via Remote HA (4 appareils)

> 🔧 **HACS** — [GitHub Remote Home-Assistant](https://github.com/custom-components/remote_homeassistant)
> Via instance HA secondaire (IP locale)

| Nb | Modèle | Description | Localisation |
|---|---|---|---|
| 2 | Schneider Odace SFSP | Armoire de toilette connectée | Salle de bain, Salle d'eau |
| 2 | Schneider Odace SFSP | Plafonnier connecté | Salle de bain, Salle d'eau |

---

### Compteurs & Mesure (4 appareils)

| Nb | Fabricant | Modèle | Description | Intégration | Mode |
|---|---|---|---|---|---|
| 1 | Enedis | Linky | Compteur électrique intelligent | 📦 Add-on [Linky](https://github.com/bokub/linky) | ☁️ Cloud |
| 1 | GrDF | GAZPAR | Compteur gaz communicant | 📦 Add-on [Gazpar2MQTT](https://github.com/ssenart/gazpar2mqtt) | ☁️ Cloud |
| 1 | — | Capteur Eau froide | Compteur eau froide | MQTT | ✅ Local |
| 1 | — | Capteur Eau chaude | Compteur eau chaude | MQTT | ✅ Local |
