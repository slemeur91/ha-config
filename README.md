# 🏠 Configuration Home Assistant

> Documentation de ma configuration Home Assistant, partagée pour aider la communauté.

## 📊 Vue d'ensemble

| Élément | Valeur |
|---|---|
| Version HA | 2026.5.4 |
| Entités totales | 2 156 |
| Domaines | 43 |
| Zones / Pièces | 23 |
| Modules complémentaires (Add-ons) | **17** |
| Intégrations HACS | **19** |
| Cartes Lovelace HACS | **7** |

### 🔌 Appareils par technologie

| Technologie | Nb | Mode | Intégration |
|---|---|---|---|
| Z-Wave | 13 | ✅ Local | 🏠 Natif HA (Z-Wave JS UI via MQTT) |
| EnOcean | 3 | ✅ Local | 📦 Add-on Apps |
| Zigbee — Aqara | 3 | ✅ Local | 📦 Add-on Apps (Zigbee2MQTT) |
| Zigbee — Philips Hue | 11 | ✅ Local | 🏠 Natif HA (Hue Bridge) |
| Schneider Odace (via Remote HA) | 4 | ✅ Local | 🔧 HACS |
| Somfy io-homecontrol (volets/velux) | 14 | ✅ Local | 🏠 Natif HA (KLF200) |
| Somfy RTS (porte garage via RFPlayer) | 1 | ✅ Local | 🔧 HACS ⚠️ Dépôt perso |
| Somfy Protexial (alarme) | 1 | ✅ Local | 🔧 HACS ⚠️ Dépôt perso |
| SONOS WiFi | 5 | ✅ Local | 🏠 Natif HA |
| Daikin WiFi | 4 | ✅ Local | 🏠 Natif HA |
| Nuki Bluetooth/WiFi | 2 | ✅ Local | 🏠 Natif HA |
| Broadlink WiFi (télécommandes IR/RF) | 2 | ✅ Local | 🏠 Natif HA |
| Xiaomi MIoT WiFi (qualité d'air) | 2 | ✅ Local | 🔧 HACS |
| Xiaomi miio WiFi (aspirateurs) | 2 | ✅ Local | 🏠 Natif HA |
| Dyson WiFi (purificateur) | 1 | ✅ Local | 🔧 HACS |
| GCE EcoDevices RT2 (mesure conso) | 1 | ✅ Local | 🔧 HACS |
| GCE RFPlayer (RF 433/868 MHz) | 1 | ✅ Local | 🔧 HACS ⚠️ Dépôt perso |
| Sony Bravia WiFi | 1 | ✅ Local | 🏠 Natif HA |
| Apple TV | 1 | ✅ Local | 🏠 Natif HA |
| Synology NAS | 2 | ✅ Local | 🏠 Natif HA |
| Caméras IP (UniFi Protect) | 8 | ✅ Local | 🏠 Natif HA |
| Husqvarna Automower | 1 | ✅ Local | 🏠 Natif HA |
| Multiprises WiFi/MQTT | 7 | ✅ Local | 🏠 Natif HA |
| TP-Link Tapo | 1 | ✅ Local | 🏠 Natif HA |
| Netatmo (météo/température) | 7 | ☁️ Cloud | 🏠 Natif HA |
| EcoFlow (batterie/onduleur) | 3 | ☁️ Cloud | 🔧 HACS |
| Amazon Echo | 1 | ☁️ Cloud | 🔧 HACS |
| Sure Petcare (chatière) | 1 | ☁️ Cloud | 🏠 Natif HA |
| X-Sense (détecteurs incendie/CO) | 4 | ☁️ Cloud | 🔧 HACS ⚠️ Dépôt perso |
| Linky / GAZPAR (compteurs) | 2 | ☁️ Cloud | 📦 Add-on Apps |

> [Détail complet des appareils →](docs/appareils.md)

---

## 🤖 Automations (46 actives)


| Catégorie | Nb | Fichier détail |
|---|---|---|
| Alarme & Sécurité | 3 | [Voir →](docs/automations/alarme_securite.md) |
| Alertes & Notifications | 4 | [Voir →](docs/automations/alertes_notifications.md) |
| Audio / HiFi | 3 | [Voir →](docs/automations/audio_hifi.md) |
| Batteries | 4 | [Voir →](docs/automations/batteries.md) |
| Calendrier & Planification | 2 | [Voir →](docs/automations/calendrier_planification.md) |
| Chauffage | 2 | [Voir →](docs/automations/chauffage.md) |
| Énergie & Environnement | 3 | [Voir →](docs/automations/energie_environnement.md) |
| Lumières | 5 | [Voir →](docs/automations/lumieres.md) |
| Maintenance & Corrections | 5 | [Voir →](docs/automations/maintenance_corrections.md) |
| Présence & Domicile | 3 | [Voir →](docs/automations/presence_domicile.md) |
| Velux (blueprint) | 3 | [Voir →](docs/automations/blueprint_velux.md) |
| Volets (blueprint) | 9 | [Voir →](docs/automations/blueprint_volets.md) |

### Résumé des automations actives

<details>
<summary>Voir la liste complète (46) — triée par catégorie puis alphabétiquement</summary>

#### Alarme & Sécurité
| Alias | Entity ID | Résumé |
|---|---|---|
| Alarme Déclenchement | `automation.alarme_declenchement` | Snapshots et notifications en boucle lors d'un déclenchement |
| Alarme Sabotage | `automation.alarme_sabotage` | Notifications lors d'un sabotage du boîtier alarme |
| Gestion de l'Alarme | `automation.alarme` | Coordonne domicile, caméras et présence selon l'alarme |

#### Alertes & Notifications
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la température du réfrigérateur | `automation.gestion_de_la_temperature_du_refrigerateur` | Alerte si températures frigo/congélateur hors plage |
| Notification de l'Horloge | `automation.notification_de_l_horloge` | Annonce vocale de l'heure toutes les heures |
| Notification des Alertes | `automation.gestion_des_alertes` | Détecte et notifie fuites, fumées, serveurs, brouillage |
| Notification des Poubelles | `automation.notification_des_poubelles` | Rappels vocaux et SMS pour sortir/rentrer les poubelles |

#### Audio / HiFi
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la HiFi | `automation.gestion_de_la_hifi` | Allume/éteint la chaîne HiFi et gère les sources |
| Gestion de la Télécommande HiFi | `automation.gestion_de_la_telecommande_hifi` | Associe les boutons Z-Wave de la télécommande à la HiFi/SONOS |
| Gestion des SONOS | `automation.gestion_des_sonos` | Pilote les enceintes selon les modes ON/OFF/COUCHE/REVEIL |

#### Batteries
| Alias | Entity ID | Résumé |
|---|---|---|
| Notification appareils en batterie faible | `automation.notification_appareils_en_batterie_faible` | Notifications persistantes batterie faible/restaurée |
| Notification appareils en batterie faible - Hebdomadaire | `automation.notification_appareils_en_batterie_faible_hebdomadaire` | Vérification hebdomadaire batteries (vendredi 19h) |
| Notification appareils en batterie faible - Mail hebdomadaire | `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` | Mail récapitulatif batteries faibles |
| Notification de batterie remplacée | `automation.notification_de_batterie_remplacee` | Suggestion de marquer une batterie comme remplacée |

#### Calendrier & Planification
| Alias | Entity ID | Résumé |
|---|---|---|
| GAZPAR – Mise à jour statistiques journalières | `automation.gazpar_mise_a_jour_statistiques_journalieres` | Injecte les données gaz dans les statistiques HA |
| Planification de l'Agenda | `automation.planification_de_l_agenda` | Positionne les modes calendrier/chauffage selon l'agenda |

#### Chauffage
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion du Chauffage de l'Etage | `automation.gestion_du_chauffage_de_l_etage` | Pilote les 5 thermostats Z-Wave de l'étage |
| Gestion du Chauffage du RDC | `automation.gestion_du_chauffage_du_rdc` | Pilote le chauffage du rez-de-chaussée |

#### Énergie & Environnement
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de l'activation de l'Arrosage | `automation.gestion_de_l_activation_de_l_arrosage` | Ouvre/ferme la vanne selon le timer et la pluviométrie |
| Gestion de la Qualité de l'Air | `automation.gestion_de_la_qualite_de_l_air` | Active les purificateurs selon PM2.5/PM10/VOC/NO2 |
| Gestion du Soleil | `automation.gestion_du_soleil` | Calcule le mode soleil et positionne les volets en Été/Hiver |

#### Lumières
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la lumière du Garage | `automation.gestion_de_la_lumiere_du_garage` | Allume la lumière à l'ouverture de la porte si sombre |
| Gestion du Bouton Hue Central Droit | `automation.gestion_du_bouton_hue_central_droit` | Appuis longs : contrôle HiFi et SONOS |
| Gestion du Bouton Hue Central Gauche | `automation.gestion_du_bouton_hue_central_gauche` | Appuis longs : contrôle HiFi et SONOS |
| Gestion du Bouton Hue de l'Entrée | `automation.gestion_du_bouton_hue_de_l_entree` | En cours d'affectation |
| Gestion du Bouton Hue de l'Etage | `automation.gestion_du_bouton_hue_de_l_etage` | En cours d'affectation |

#### Maintenance & Corrections
| Alias | Entity ID | Résumé |
|---|---|---|
| Correction Tuya | `automation.correction_tuya` | Force la reconnexion Tuya 5 min après démarrage HA |
| Corrections des Appareils EcoFlow | `automation.corrections_des_appareils_ecoflow` | Redémarre les intégrations EcoFlow si hors ligne |
| Corrections du KLF200 pour les Velux | `automation.corrections_du_klf200_pour_les_velux` | Redémarre automatiquement le KLF200 en cas de panne |
| Gestion du Poêle et de la Climatisation | `automation.gestion_du_poele_et_de_la_climatisation` | Gère les flags poêle/clim et le contacteur selon l'alarme |
| Maintien des Prises et Appareils allumés | `automation.maintien_des_prises_et_appareils_allumes` | Garde les prises critiques allumées et surveille les serveurs |

#### Présence & Domicile
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la Boîte aux Lettres | `automation.gestion_de_la_boite_aux_lettres` | Détecte dépôt courrier/colis via capteur P100 |
| Gestion de la Présence dans les Pièces | `automation.gestion_de_la_presence_dans_les_pieces` | Met à jour la présence par pièce via capteurs Aqara FP2 |
| Gestion du Domicile en fonction de la Présence | `automation.gestion_du_domicile_en_fonction_de_la_presence` | Actions selon la présence (Réveil/Arrivée/Couché/Extinction) |

#### Velux — Blueprint `Volets/Gestion_des_velux.yaml`
| Alias | Entity ID | Pièce |
|---|---|---|
| Gestion du Velux - Chambre | `automation.gestion_du_velux_chambre` | Chambre |
| Gestion du Velux - Salle d'eau | `automation.gestion_du_velux_salle_d_eau` | Salle d'eau |
| Gestion du Velux - Salle de bain | `automation.gestion_du_velux_salle_de_bain` | Salle de bain |

#### Volets — Blueprint `Volets/Gestion_des_volets.yaml`
| Alias | Entity ID | Pièce |
|---|---|---|
| Gestion du Volet - Bureau | `automation.gestion_du_volet_bureau` | Bureau |
| Gestion du Volet - Cellier | `automation.gestion_du_volet_cellier` | Cellier |
| Gestion du Volet - Chambre | `automation.gestion_du_volet_chambre` | Chambre |
| Gestion du Volet - Cuisine | `automation.gestion_du_volet_cuisine` | Cuisine |
| Gestion du Volet - Salle d'eau | `automation.gestion_du_volet_salle_d_eau` | Salle d'eau |
| Gestion du Volet - Salle de bain | `automation.gestion_du_volet_salle_de_bain` | Salle de bain |
| Gestion du Volet - Salon | `automation.gestion_du_volet_salon` | Salon |
| Gestion du Volet - Séjour | `automation.gestion_du_volet_sejour` | Séjour |
| Gestion du Volet - Suite parentale | `automation.gestion_du_volet_suite_parentale` | Suite parentale |

</details>

---

## ⚙️ Configuration principale

[Voir la documentation complète →](docs/configuration.md)

| Section | Détail |
|---|---|
| Notifications SMTP (email) | Serveur SMTP local, `notify.email`, port 25 |

---

## 📜 Scripts (16)

[Voir la documentation complète →](docs/scripts.md)

| Script | Rôle |
|---|---|
| `delete_all_orphaned_entities` | Supprime les entités orphelines |
| `gestion_du_reveil` | Déclenchement réveil musical |
| `ios_alarme_activation_absent` | Arme l'alarme en mode absent (iOS) |
| `ios_alarme_desactivation` | Désarme l'alarme (iOS) |
| `ios_porte_du_garage` | Toggle porte garage (iOS) |
| `ios_serrure_de_l_entree_deverrouiller` | Déverrouille serrure entrée (iOS) |
| `ios_serrure_de_l_entree_verrouiller` | Verrouille serrure entrée (iOS) |
| `ios_serrure_du_garage_deverrouiller` | Déverrouille serrure garage (iOS) |
| `notification_mail` | Envoi mail |
| `notification_sms` | Envoi Telegram |
| `notification_snapshot` | Captures caméras par mail |
| `notification_vocale` | TTS SONOS multi-mode |
| `reload_pyscript` | Recharge l'intégration pyscript |
| `sonos_radio_sur_la_suite_parentale` | Radio Suite parentale avec sélection horaire |
| `sonos_radio_sur_le_garage` | Radio Garage avec repli |
| `sonos_radio_sur_le_salon` | Radio Salon avec repli |

---

## 📦 Modules complémentaires — Add-ons (17)

[Voir la documentation complète →](docs/addons.md)

> 🏠 **Officiel HA** = dépôt officiel Home Assistant, aucune source supplémentaire à ajouter
> 📦 **Communauté** = dépôt tiers à ajouter manuellement dans les sources d'add-ons

| Add-on | GitHub | Rôle | Source |
|---|---|---|---|
| EnOcean MQTT | [asera-corp/ha-enoceanmqtt](https://github.com/asera-corp/ha-enoceanmqtt) | Passerelle EnOcean | 📦 Communauté |
| File editor | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/configurator) | Éditeur de fichiers | 🏠 Officiel HA |
| Gazpar2MQTT | [ssenart/gazpar2mqtt](https://github.com/ssenart/gazpar2mqtt) | Données GAZPAR vers MQTT | 📦 Communauté |
| Get HACS | [hacs/get](https://github.com/hacs/get) | Installateur HACS | 📦 Communauté |
| Home Assistant MCP Server | [voska/hass-mcp](https://github.com/voska/hass-mcp) | Intégration IA via MCP | 📦 Communauté |
| Home-Assistant-Matter-Hub | [t0bst4r/home-assistant-matter-hub](https://github.com/t0bst4r/home-assistant-matter-hub) | Pont Matter vers Alexa/Apple/Google | 📦 Communauté |
| Homebridge | [homebridge/homebridge-hassio](https://github.com/homebridge/homebridge-hassio) | Support HomeKit | 📦 Communauté |
| Linky | [bokub/linky](https://github.com/bokub/linky) | Compteur Linky | 📦 Communauté |
| Matter Server | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/matter_server) | Support Matter | 🏠 Officiel HA |
| Mosquitto broker | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/mosquitto) | Broker MQTT | 🏠 Officiel HA |
| MQTT Explorer | [thomasloven/hassio-mqtt-explorer](https://github.com/thomasloven/hassio-mqtt-explorer) | Explorateur MQTT | 📦 Communauté |
| OpenThread Border Router | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/openthread_border_router) | Thread/Matter | 🏠 Officiel HA |
| Studio Code Server | [hassio-addons/addon-vscode](https://github.com/hassio-addons/addon-vscode) | VSCode intégré | 📦 Communauté |
| Terminal & SSH | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/ssh) | Accès terminal | 🏠 Officiel HA |
| Z-Wave JS | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/zwave_js) | Réseau Z-Wave *(désactivé — remplacé par Z-Wave JS UI)* | 🏠 Officiel HA |
| Z-Wave JS UI | [hassio-addons/addon-zwave-js-ui](https://github.com/hassio-addons/addon-zwave-js-ui) | Interface Z-Wave JS complète + publication MQTT | 📦 Communauté |
| Zigbee2MQTT | [zigbee2mqtt/hassio-zigbee2mqtt](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt) | Réseau Zigbee | 📦 Communauté |

---

## 🛠️ HACS — Intégrations (19)

[Voir la documentation complète →](docs/hacs.md)

> 🔧 **HACS** = disponible dans le catalogue HACS standard, sans dépôt personnalisé
> ⚠️ **Dépôt perso** = dépôt GitHub personnel à ajouter manuellement dans HACS

| Intégration | GitHub | Source |
|---|---|---|
| Alexa Media Player | [alandtse/alexa_media_player](https://github.com/alandtse/alexa_media_player) | 🔧 HACS |
| Atmo France | [sebcaps/atmofrance](https://github.com/sebcaps/atmofrance) | 🔧 HACS |
| Battery Notes | [andrew-codechimp/HA-Battery-Notes](https://github.com/andrew-codechimp/HA-Battery-Notes) | 🔧 HACS |
| Dyson Local | [libdyson-wg/ha-dyson](https://github.com/libdyson-wg/ha-dyson) | 🔧 HACS |
| Ecodevices RT2 | [pcourbin/ecodevices_rt2](https://github.com/pcourbin/ecodevices_rt2) | 🔧 HACS |
| EcoFlow Cloud | [snell-evan-itt/hassio-ecoflow-cloud-US](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US) | 🔧 HACS |
| HACS | [hacs/integration](https://github.com/hacs/integration) | 🔧 HACS |
| Local Agenda | [slemeur91/local_agenda](https://github.com/slemeur91/local_agenda) | ⚠️ Dépôt perso |
| Micronova Agua IOT | [vincentwolsink/home_assistant_micronova_agua_iot](https://github.com/vincentwolsink/home_assistant_micronova_agua_iot) | 🔧 HACS |
| My EcoWatt by RTE | [kamaradclimber/rte-ecowatt](https://github.com/kamaradclimber/rte-ecowatt) | 🔧 HACS |
| Orange Livebox | [cyr-ius/hass-livebox-component](https://github.com/cyr-ius/hass-livebox-component) | 🔧 HACS |
| pyscript | [custom-components/pyscript](https://github.com/custom-components/pyscript) | 🔧 HACS |
| Remote Home-Assistant | [custom-components/remote_homeassistant](https://github.com/custom-components/remote_homeassistant) | 🔧 HACS |
| RfPlayer | [gce-electronics/HA_RFPlayer](https://github.com/gce-electronics/HA_RFPlayer) | ⚠️ Dépôt perso |
| Somfy Protexial | [AuroreVgn/somfy-protexial](https://github.com/AuroreVgn/somfy-protexial) | ⚠️ Dépôt perso |
| Spook | [frenck/spook](https://github.com/frenck/spook) | 🔧 HACS |
| Vacances Scolaires | [Master13011/vacances-scolaire-HA](https://github.com/Master13011/vacances-scolaire-HA) | 🔧 HACS |
| Xiaomi Miot | [al-one/hass-xiaomi-miot](https://github.com/al-one/hass-xiaomi-miot) | 🔧 HACS |
| xsense | [Jarnsen/ha-xsense-component_test](https://github.com/Jarnsen/ha-xsense-component_test) | ⚠️ Dépôt perso |

### Cartes Lovelace HACS (7)

| Carte | GitHub | Source |
|---|---|---|
| apexcharts-card | [RomRider/apexcharts-card](https://github.com/RomRider/apexcharts-card) | 🔧 HACS |
| Battery State Card | [maxwroc/battery-state-card](https://github.com/maxwroc/battery-state-card) | 🔧 HACS |
| card-mod | [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod) | 🔧 HACS |
| Custom-ui | [Mariusthvdb/custom-ui](https://github.com/Mariusthvdb/custom-ui) | 🔧 HACS |
| expander-card | [MelleD/lovelace-expander-card](https://github.com/MelleD/lovelace-expander-card) | 🔧 HACS |
| GrDF Gazpar card | [ssenart/lovelace-gazpar-card](https://github.com/ssenart/lovelace-gazpar-card) | ⚠️ Dépôt perso |
| Waze Travel Time Card | [r-renato/ha-card-waze-travel-time](https://github.com/r-renato/ha-card-waze-travel-time) | 🔧 HACS |

---

## 📐 Blueprints

| Blueprint | Instances | Description |
|---|---|---|
| [Gestion des Velux](docs/automations/blueprint_velux.md) | 3 | Fermeture selon présence, météo, protection thermique |
| [Gestion des Volets](docs/automations/blueprint_volets.md) | 9 | Pilotage intelligent selon mode, météo, soleil, présence |

### Points d'attention lors de la création de blueprints

Deux limitations importantes rencontrées lors du développement :

**Les triggers ne peuvent pas utiliser les variables de la section `variables:`**
Les variables déclarées dans la section `variables:` du blueprint ne sont pas encore évaluées au moment où les triggers sont définis. Il faut donc utiliser directement les `!input` dans les triggers, ou des entités statiques.

**L'accès aux inputs dans les templates**
Dans les templates Jinja2 des actions, les inputs (`!input`) doivent être capturés au préalable dans la section `variables:` pour être accessibles. Un accès direct à `!input` dans un template imbriqué peut échouer selon le contexte d'évaluation.

---

## 🔌 Appareils connectés

[Voir la documentation complète →](docs/appareils.md)

---

## 🏗️ Architecture

```
Réseau Z-Wave    → Z-Wave JS UI (zwavejs2mqtt) → MQTT → HA
Réseau Zigbee    → Zigbee2MQTT               → MQTT → HA
EnOcean          → EnOcean MQTT              → MQTT → HA
GAZPAR           → Gazpar2MQTT               → MQTT → HA
Appareils locaux → Intégrations natives HA
Appareils cloud  → Intégrations HACS
```

---

## 📄 Licence

Cette configuration est partagée sous licence MIT. Libre à vous de l'adapter à votre installation.
