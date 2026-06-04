# 🏠 Configuration Home Assistant

> Documentation de ma configuration Home Assistant, partagée pour aider la communauté.

## 📊 Vue d'ensemble

| Élément | Valeur |
|---|---|
| Version HA | 2026.6.0 |
| Entités totales | 2 156 |
| Domaines (types d'entités) | 43 |
| Zones / Pièces | 23 |
| Appareils connectés | **157** |
| Modules complémentaires (Add-ons) | **17** |
| Intégrations HACS | **19** |
| Cartes Lovelace HACS | **7** |

### 🔌 Appareils par technologie (157)

| Technologie | Appareils | Mode | Détail |
|---|---|---|---|
| Z-Wave | **25** | ✅ Local | [→ Détail](docs/appareils/zwave.md) |
| Zigbee | **20** | ✅ Local | [→ Détail](docs/appareils/zigbee.md) |
| EnOcean | **4** | ✅ Local | [→ Détail](docs/appareils/enocean.md) |
| WiFi / IP | **86** | ✅ Local + ☁️ Cloud | [→ Détail](docs/appareils/integrations.md) |
| Thread / Matter | **1** | ✅ Local | [→ Détail](docs/appareils/matter.md) |
| Intégrations (Somfy KLF200, Protexial, RF…) | **21** | ✅ Local | [→ Détail](docs/appareils/integrations.md) |

---

## 🤖 Automations (46 actives)


| Catégorie | Nb | Détail |
|---|---|---|
| Alarme & Sécurité | 3 | [→ Détail](docs/automations/alarme_securite.md) |
| Alertes & Notifications | 4 | [→ Détail](docs/automations/alertes_notifications.md) |
| Audio / HiFi | 3 | [→ Détail](docs/automations/audio_hifi.md) |
| Batteries | 4 | [→ Détail](docs/automations/batteries.md) |
| Calendrier & Planification | 2 | [→ Détail](docs/automations/calendrier_planification.md) |
| Chauffage | 2 | [→ Détail](docs/automations/chauffage.md) |
| Énergie & Environnement | 3 | [→ Détail](docs/automations/energie_environnement.md) |
| Lumières | 5 | [→ Détail](docs/automations/lumieres.md) |
| Maintenance & Corrections | 5 | [→ Détail](docs/automations/maintenance_corrections.md) |
| Présence & Domicile | 3 | [→ Détail](docs/automations/presence_domicile.md) |
| Velux (blueprint) | 3 | [→ Détail](docs/automations/blueprint_velux.md) |
| Volets (blueprint) | 9 | [→ Détail](docs/automations/blueprint_volets.md) |

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

| Add-on | Appareils | Rôle | GitHub | Source |
|---|---|---|---|---|
| EnOcean MQTT | 4 | Passerelle EnOcean | [asera-corp/ha-enoceanmqtt](https://github.com/asera-corp/ha-enoceanmqtt) | 📦 Communauté |
| File editor | — | Éditeur de fichiers | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/configurator) | 🏠 Officiel HA |
| Gazpar2MQTT | 1 | Données GAZPAR vers MQTT | [ssenart/gazpar2mqtt](https://github.com/ssenart/gazpar2mqtt) | 📦 Communauté |
| Get HACS | — | Installateur HACS | [hacs/get](https://github.com/hacs/get) | 📦 Communauté |
| Home Assistant MCP Server | — | Intégration IA via MCP | [voska/hass-mcp](https://github.com/voska/hass-mcp) | 📦 Communauté |
| Home-Assistant-Matter-Hub | — | Pont Matter vers Alexa/Apple/Google | [t0bst4r/home-assistant-matter-hub](https://github.com/t0bst4r/home-assistant-matter-hub) | 📦 Communauté |
| Homebridge | — | Support HomeKit | [homebridge/homebridge-hassio](https://github.com/homebridge/homebridge-hassio) | 📦 Communauté |
| Linky | 1 | Compteur Linky | [bokub/linky](https://github.com/bokub/linky) | 📦 Communauté |
| Matter Server | — | Support Matter | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/matter_server) | 🏠 Officiel HA |
| Mosquitto broker | — | Broker MQTT | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/mosquitto) | 🏠 Officiel HA |
| MQTT Explorer | — | Explorateur MQTT | [thomasloven/hassio-mqtt-explorer](https://github.com/thomasloven/hassio-mqtt-explorer) | 📦 Communauté |
| OpenThread Border Router | — | Thread/Matter | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/openthread_border_router) | 🏠 Officiel HA |
| Studio Code Server | — | VSCode intégré | [hassio-addons/addon-vscode](https://github.com/hassio-addons/addon-vscode) | 📦 Communauté |
| Terminal & SSH | — | Accès terminal | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/ssh) | 🏠 Officiel HA |
| Z-Wave JS | — | Réseau Z-Wave *(désactivé — remplacé par Z-Wave JS UI)* | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/zwave_js) | 🏠 Officiel HA |
| Z-Wave JS UI | 25 | Interface Z-Wave JS complète + publication MQTT | [hassio-addons/addon-zwave-js-ui](https://github.com/hassio-addons/addon-zwave-js-ui) | 📦 Communauté |
| Zigbee2MQTT | 22 | Réseau Zigbee | [zigbee2mqtt/hassio-zigbee2mqtt](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt) | 📦 Communauté |

---

## 🛠️ HACS — Intégrations (19)

[Voir la documentation complète →](docs/hacs.md)

> 🔧 **HACS** = disponible dans le catalogue HACS standard, sans dépôt personnalisé
> 🔧 **HACS Communauté** = dépôt tiers à ajouter manuellement dans les sources HACS
> ⚠️ **Dépôt perso** = dépôt GitHub personnel à ajouter manuellement dans HACS

| Intégration | Appareils | Rôle | GitHub | Source |
|---|---|---|---|---|
| Alexa Media Player | 1 | Contrôle des appareils Amazon Alexa | [alandtse/alexa_media_player](https://github.com/alandtse/alexa_media_player) | 🔧 HACS |
| Atmo France | — | Qualité de l'air des villes françaises (Atmo) | [sebcaps/atmofrance](https://github.com/sebcaps/atmofrance) | 🔧 HACS |
| Battery Notes | — | Suivi des types et dates de remplacement de piles | [andrew-codechimp/HA-Battery-Notes](https://github.com/andrew-codechimp/HA-Battery-Notes) | 🔧 HACS |
| Dyson Local | 1 | Intégration locale (sans cloud) des appareils Dyson | [libdyson-wg/ha-dyson](https://github.com/libdyson-wg/ha-dyson) | 🔧 HACS |
| Ecodevices RT2 | 1 | Mesure de consommation multi-circuits (GCE) | [pcourbin/ecodevices_rt2](https://github.com/pcourbin/ecodevices_rt2) | 🔧 HACS |
| EcoFlow Cloud | 3 | Appareils EcoFlow (batterie DELTA Max, PowerStream) | [snell-evan-itt/hassio-ecoflow-cloud-US](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US) | 🔧 HACS |
| HACS | — | Gestionnaire de contenu communautaire HA | [hacs/integration](https://github.com/hacs/integration) | 🔧 HACS |
| Local Agenda | — | Calendriers locaux enrichis pour la planification domotique | [slemeur91/local_agenda](https://github.com/slemeur91/local_agenda) | ⚠️ Dépôt perso |
| Micronova Agua IOT | — | Contrôle des poêles à granulés via Agua IOT *(désactivé)* | [vincentwolsink/home_assistant_micronova_agua_iot](https://github.com/vincentwolsink/home_assistant_micronova_agua_iot) | 🔧 HACS |
| My EcoWatt by RTE | — | Signaux de sobriété électrique RTE | [kamaradclimber/rte-ecowatt](https://github.com/kamaradclimber/rte-ecowatt) | 🔧 HACS |
| Orange Livebox | 1 | Supervision de la Livebox Orange | [cyr-ius/hass-livebox-component](https://github.com/cyr-ius/hass-livebox-component) | 🔧 HACS |
| pyscript | — | Scripts Python avancés dans HA | [custom-components/pyscript](https://github.com/custom-components/pyscript) | 🔧 HACS |
| Remote Home-Assistant | 4 | Liaison entre deux instances Home Assistant | [custom-components/remote_homeassistant](https://github.com/custom-components/remote_homeassistant) | 🔧 HACS |
| RfPlayer | 2 | Récepteur/émetteur RF 433/868 MHz (GCE RFPlayer) | [gce-electronics/HA_RFPlayer](https://github.com/gce-electronics/HA_RFPlayer) | 🔧 HACS Communauté |
| Somfy Protexial | 1 | Centrale d'alarme Somfy Protexial | [AuroreVgn/somfy-protexial](https://github.com/AuroreVgn/somfy-protexial) | 🔧 HACS Communauté |
| Spook | — | Services supplémentaires et détection d'entités orphelines | [frenck/spook](https://github.com/frenck/spook) | 🔧 HACS |
| Vacances Scolaires | — | Calendrier des vacances scolaires françaises (zone C) | [Master13011/vacances-scolaire-HA](https://github.com/Master13011/vacances-scolaire-HA) | 🔧 HACS |
| Xiaomi Miot | 2 | Appareils Xiaomi via protocole MIoT local | [al-one/hass-xiaomi-miot](https://github.com/al-one/hass-xiaomi-miot) | 🔧 HACS |
| xsense | 4 | Détecteurs de fumée/CO X-Sense (cloud) | [Jarnsen/ha-xsense-component_test](https://github.com/Jarnsen/ha-xsense-component_test) | 🔧 HACS Communauté |

### Cartes Lovelace HACS (7)

| Carte | Appareils | Rôle | GitHub | Source |
|---|---|---|---|---|
| apexcharts-card | — | Graphiques avancés (consommation énergie) | [RomRider/apexcharts-card](https://github.com/RomRider/apexcharts-card) | 🔧 HACS |
| Battery State Card | 1 | Tableau de bord des niveaux de batteries | [maxwroc/battery-state-card](https://github.com/maxwroc/battery-state-card) | 🔧 HACS |
| card-mod | 1 | CSS personnalisé sur n'importe quelle carte Lovelace | [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod) | 🔧 HACS |
| Custom-ui | — | Templates et couleurs d'icônes personnalisés | [Mariusthvdb/custom-ui](https://github.com/Mariusthvdb/custom-ui) | 🔧 HACS |
| expander-card | — | Carte extensible/rétractable pour les dashboards | [MelleD/lovelace-expander-card](https://github.com/MelleD/lovelace-expander-card) | 🔧 HACS |
| GrDF Gazpar card | 1 | Affichage des données de consommation GAZPAR | [ssenart/lovelace-gazpar-card](https://github.com/ssenart/lovelace-gazpar-card) | 🔧 HACS Communauté |
| Waze Travel Time Card | — | Temps de trajet calculé par Waze | [r-renato/ha-card-waze-travel-time](https://github.com/r-renato/ha-card-waze-travel-time) | 🔧 HACS |

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
