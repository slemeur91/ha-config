# 🏠 Configuration Home Assistant

> Documentation de ma configuration Home Assistant, partagée pour aider la communauté.

## 📊 Vue d'ensemble

| Élément | Valeur |
|---|---|
| Version HA | 2026.x.x |
| Entités totales | 2 986 |
| Domaines (types d'entités) | 47 |
| Zones / Pièces | 23 |
| Appareils connectés | **203** |
| Automatisations | **64** |
| Scripts | **21** |
| Modules complémentaires (Add-ons) | **19** |
| Intégrations HACS | **37** |
| Cartes Lovelace HACS | **21** |

---

### ⚙️ Configuration principale (4)

[Voir la documentation complète →](docs/configuration.md)

| Section | Détail |
|---|---|
| Débogage — Logger | Niveaux `debug` pour Somfy Protexial, Local Agenda, Apple TV, pyatv |
| Événements de log — System Log | `fire_event: true` requis pour l'automatisation de surveillance des erreurs |
| Personnalisation — Homeassistant | Packages + correction `state_class: total` sur 28 capteurs d'énergie |
| Notifications SMTP (email) | Serveur SMTP local, `notify.email`, port 25 |

---

### 🔌 Appareils par technologie (203)

| Technologie | Appareils | Mode | Détail |
|---|---|---|---|
| Z-Wave | **25** | ✅ Local | [→ Détail](docs/appareils/zwave.md) |
| Zigbee | **22** | ✅ Local | [→ Détail](docs/appareils/zigbee.md) |
| EnOcean | **4** | ✅ Local | [→ Détail](docs/appareils/enocean.md) |
| Intégrations (WiFi, Ethernet RJ45 & Autres) | **151** | ✅ Local + ☁️ Cloud | [→ Détail](docs/appareils/integrations.md) |
| Thread / Matter | **1** | ✅ Local | [→ Détail](docs/appareils/matter.md) |

---

## 🤖 Automations (64)


| Catégorie | Nb | Détail |
|---|---|---|
| Alarme | 3 | [→ Détail](docs/automations/alarme.md) |
| Automatisation | 20 | [→ Détail](docs/automations/automatisation.md) |
| Corrections | 10 | [→ Détail](docs/automations/corrections.md) |
| HiFi | 3 | [→ Détail](docs/automations/hifi.md) |
| Lumières | 8 | [→ Détail](docs/automations/lumieres.md) |
| Notifications | 15 | [→ Détail](docs/automations/notifications.md) |
| Surveillance HA | 4 | [→ Détail](docs/automations/surveillance_ha.md) |
| Volets | 1 | [→ Détail](docs/automations/volets.md) |

### Résumé des automations actives

<details>
<summary>Voir la liste complète (64) — triée par catégorie puis alphabétiquement</summary>

#### Alarme
| Alias | Entity ID | Résumé |
|---|---|---|
| Alarme Déclenchement | `automation.alarme_declenchement` | Snapshots et notifications en boucle lors d'un déclenchement |
| Alarme Sabotage | `automation.alarme_sabotage` | Notifications lors d'un sabotage du boîtier alarme |
| Gestion de l'Alarme | `automation.alarme` | Coordonne domicile, caméras et présence selon l'alarme |

#### Automatisation
| Alias | Entity ID | Résumé |
|---|---|---|
| GAZPAR – Gestion des statistiques journalières (Réécriture) | `automation.gestion_des_statistiques_journalieres_de_gazpar_reecriture` | Injecte les données gaz dans les statistiques HA |
| Gestion du Cycle du Lave Linge | `automation.gestion_du_cycle_du_lave_linge` | Suit début/fin de cycle et enregistre index d'énergie |
| Gestion du Cycle du Lave Vaisselle | `automation.gestion_du_cycle_du_lave_vaisselle` | Suit début/fin de cycle et enregistre index d'énergie |
| Gestion du Cycle du Sèche Linge | `automation.gestion_du_cycle_du_seche_linge` | Suit début/fin de cycle et enregistre index d'énergie |
| LINKY – Gestion des statistiques journalières (Réécriture) | `automation.gestion_des_statistiques_journalieres_du_linky_reecriture` | Réimporte les statistiques Linky avec les vraies dates Enedis |
| Gestion de l'activation de l'Arrosage | `automation.gestion_de_l_activation_de_l_arrosage` | Ouvre/ferme la vanne selon le timer et la pluviométrie |
| Gestion de l'Activation de l'imprimante Canon MF650C | `automation.gestion_de_l_activation_de_l_imprimante_canon_mf650c` | Active/désactive l'intégration selon la présence réseau de l'imprimante |
| Gestion de la charge batterie de l'iPad | `automation.gestion_de_la_charge_batterie_de_l_ipad` | Charge et cycle mensuel de décharge de la batterie |
| Gestion de la Climatisation - Start en Boost / Stop | `automation.gestion_de_la_climatisation_start_en_boost_stop` | Lance ou arrête le mode boost sur les 4 climatisations en parallèle |
| Gestion de la Livebox W7 : désactivation du WiFi | `automation.gestion_de_la_livebox_w7_desactivation_du_wifi` | Coupe le WiFi de la Livebox W7 au démarrage ou si réactivé |
| Gestion de la Présence dans les Pièces | `automation.gestion_de_la_presence_dans_les_pieces` | Met à jour la présence par pièce via capteurs Aqara FP2 |
| Gestion de la Qualité de l'Air | `automation.gestion_de_la_qualite_de_l_air` | Active les purificateurs selon PM2.5/PM10/VOC/NO2 |
| Gestion du Chauffage de l'Etage | `automation.gestion_du_chauffage_de_l_etage` | Pilote les 5 thermostats Z-Wave de l'étage |
| Gestion du Chauffage du RDC | `automation.gestion_du_chauffage_du_rdc` | Pilote le chauffage du rez-de-chaussée |
| Gestion du Domicile en fonction de la Présence | `automation.gestion_du_domicile_en_fonction_de_la_presence` | Actions selon la présence (Réveil/Arrivée/Couché/Extinction) |
| Gestion du Poêle et de la Climatisation | `automation.gestion_du_poele_et_de_la_climatisation` | Gère les flags poêle/clim et le contacteur selon l'alarme |
| Gestion emplacement Sylvain Domicile/Absent | `automation.gestion_emplacement_sylvain_domicile_absent` | Adapte l'interrogation de l'alarme et coupe/rallume des prises selon la présence de l'iPhone au domicile |
| MAJ Auto Prises LL/SL (Zigbee2MQTT) | `automation.maj_auto_prises_ll_sl_zigbee2mqtt` | Force la relecture de la puissance des multiprises lave-linge/sèche-linge (contournement Zigbee2MQTT) |
| Gestion du Soleil | `automation.gestion_du_soleil` | Calcule le mode soleil et positionne les volets en Été/Hiver |
| Planification de l'Agenda | `automation.planification_de_l_agenda` | Positionne les modes calendrier/chauffage selon l'agenda |

#### Corrections
| Alias | Entity ID | Résumé |
|---|---|---|
| Correction de l'Onduleur | `automation.correction_de_l_onduleur` | Redémarre l'add-on NUT si l'onduleur est indisponible |
| Correction du Mi Air Purifier | `automation.correction_du_mi_air_purifier` | Cycle d'alimentation du purificateur si indisponible |
| Corrections des Appareils EcoFlow | `automation.corrections_des_appareils_ecoflow` | Redémarre les intégrations EcoFlow si hors ligne |
| KLF200 - Filet de sécurité de la prise | `automation.klf200_filet_de_securite_de_la_prise` | Rallume la prise du KLF200 si elle reste éteinte 5 mn, puis recharge l'intégration Velux |
| KLF200 - Redémarrage de la passerelle à l'arrêt de HA | `automation.klf200_redemarrage_de_la_passerelle_a_l_arret_de_ha` | Redémarre la passerelle KLF200 à l'arrêt de HA *(désactivée, en validation)* |
| KLF200 - Surveillance et réparation graduée | `automation.klf200_surveillance_et_reparation_graduee` | Détecte les défauts KLF200 et répare par étapes : rechargement, redémarrage, coupure de la prise *(désactivée, en validation)* |
| Maintien des Prises et Appareils allumés | `automation.maintien_des_prises_et_appareils_allumes` | Garde les prises critiques allumées et surveille les serveurs |
| Rechargement de l'intégration LocalTuya | `automation.rechargement_de_l_integration_localtuya` | Recharge LocalTuya 4 min après le démarrage de HA |
| Rechargement de l'intégration Netatmo | `automation.rechargement_de_l_integration_netatmo` | Recharge Netatmo si tous les modules sont indisponibles |
| Redémarrage de l'intégration OTBR sur CPU élevé | `automation.redemarrage_de_l_integration_otbr_sur_cpu_eleve` | Redémarre l'add-on OTBR si CPU > 25% au démarrage |

#### HiFi
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la HiFi | `automation.gestion_de_la_hifi` | Allume/éteint la chaîne HiFi et gère les sources |
| Gestion de la Télécommande HiFi | `automation.gestion_de_la_telecommande_hifi` | Associe les boutons Z-Wave de la télécommande à la HiFi/SONOS |
| Gestion des SONOS | `automation.gestion_des_sonos` | Pilote les enceintes selon les modes ON/OFF/COUCHE/REVEIL |

#### Lumières
| Alias | Entity ID | Résumé |
|---|---|---|
| Gestion de la lumière du Garage | `automation.gestion_de_la_lumiere_du_garage` | Allume la lumière à l'ouverture de la porte si sombre |
| Gestion de la Lumière de l'Entrée | `automation.gestion_de_la_lumiere_de_l_entree` | Allume l'extérieur si sombre lors d'un appui sonnette/présence portier |
| Gestion de la Lumière du WC de l'Étage | `automation.gestion_de_la_lumiere_du_wc_de_l_etage` | Allume/éteint la lumière WC étage selon la présence |
| Gestion de la Lumière du WC du RDC | `automation.gestion_de_la_lumiere_du_wc_du_rdc` | Allume/éteint la lumière WC RDC selon la présence |
| Gestion du Bouton Hue Central Droit | `automation.gestion_du_bouton_hue_central_droit` | Appuis longs : contrôle HiFi et SONOS |
| Gestion du Bouton Hue Central Gauche | `automation.gestion_du_bouton_hue_central_gauche` | Appuis longs : contrôle HiFi et SONOS |
| Gestion du Bouton Hue de l'Entrée | `automation.gestion_du_bouton_hue_de_l_entree` | En cours d'affectation |
| Gestion du Bouton Hue de l'Etage | `automation.gestion_du_bouton_hue_de_l_etage` | En cours d'affectation |

#### Notifications
| Alias | Entity ID | Résumé |
|---|---|---|
| Notification de capteur déporté du chauffage désactivé | `automation.notification_de_capteur_deporte_du_chauffage_desactive` | Notifie quand une sonde de chauffage de l'étage passe à Non Détecté |
| Notification de coupure de courant EDF | `automation.notification_de_coupure_de_courant_edf` | Notifie sur coupure/rétablissement secteur via onduleur EcoFlow |
| Notification appareils en batterie faible | `automation.notification_appareils_en_batterie_faible` | Notifications persistantes batterie faible/restaurée |
| Notification appareils en batterie faible - Hebdomadaire | `automation.notification_appareils_en_batterie_faible_hebdomadaire` | Vérification hebdomadaire batteries (vendredi 19h) |
| Notification appareils en batterie faible - Mail hebdomadaire | `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` | Mail récapitulatif batteries faibles |
| Notification de batterie remplacée | `automation.notification_de_batterie_remplacee` | Suggestion de marquer une batterie comme remplacée |
| Notification de défaut du réfrigérateur | `automation.notification_de_defaut_du_refrigerateur` | Alerte si températures frigo/congélateur hors plage |
| Notification de l'Horloge | `automation.notification_de_l_horloge` | Annonce vocale de l'heure toutes les heures |
| Notification de la Boîte aux Lettres | `automation.notification_de_la_boite_aux_lettres` | Détecte dépôt courrier/colis via capteur P100 |
| Notification des Alertes | `automation.gestion_des_alertes` | Détecte et notifie fuites, fumées, serveurs, brouillage |
| Notification des Poubelles | `automation.notification_des_poubelles` | Rappels vocaux et SMS pour sortir/rentrer les poubelles |
| Notification du Portier | `automation.notification_du_portier` | Notifie par snapshot mail lors d'un appui sonnette/présence portier |
| Notification des Alertes de défaut des Onduleurs - UPS | `automation.notification_des_alertes_de_defaut_des_onduleurs_ups` | Notifie les défauts des onduleurs réseau (Ups) et USB (Eaton) |
| Notification d'Ouverture ou Fermeture des fenêtres | `automation.notification_d_ouverture_ou_fermeture_des_fenetres` | Annonce vocale fermeture/ouverture selon températures intérieur/extérieur |
| Suspension des Notifications en Mode Invités | `automation.suspension_des_notifications_en_mode_invites` | Désactive les alertes vocales et sonnettes en mode invités |

#### Surveillance HA
| Alias | Entity ID | Résumé |
|---|---|---|
| Notification des Automatisations désactivées | `automation.notification_des_automatisations_desactivees` | Notifie chaque jour les automatisations désactivées |
| Notification des Automatisations et Scripts en Défaut | `automation.notification_des_automatisations_et_scripts_en_defaut` | Notifie en temps réel les erreurs d'exécution d'automatisations/scripts |
| Notification des Automatisations sans déclenchement récent | `automation.notification_des_automatisations_sans_declenchement_recent` | Notifie chaque jour les automatisations jamais/peu déclenchées |
| Rechargement des intégrations en défaut | `automation.rechargement_des_integrations_en_defaut` | Détecte et recharge les intégrations en erreur ou en panne silencieuse |

#### Volets
| Alias | Entity ID | Résumé |
|---|---|---|
| Scénario coverAutomatic | `automation.scenario_coverautomatic` | Sélectionne le scénario CoverAutomatic (vacation / summer / winter) selon le domicile et le mode des volets |

> Le pilotage des volets, velux et store est désormais assuré par l'intégration **CoverAutomatic** (voir [Volets](docs/automations/volets.md)) : les 12 automatisations par volet et velux ont été supprimées.

</details>

---

## 📜 Scripts (21)

[Voir la documentation complète →](docs/scripts.md)

| Script | Rôle |
|---|---|
| `allumer_eteindre_amplificateur_rotel` | Allume/Éteint l'ampli ROTEL et sélectionne l'entrée vidéo |
| `allumer_eteindre_apple_tv_salon` | Allume/Éteint l'Apple TV du salon |
| `delete_all_orphaned_entities` | Supprime les entités orphelines |
| `gestion_du_reveil` | Déclenchement réveil musical |
| `ios_alarme_activation_absent` | Arme l'alarme en mode absent (iOS) |
| `ios_alarme_desactivation` | Désarme l'alarme (iOS) |
| `ios_porte_du_garage` | Toggle porte garage (iOS) |
| `ios_serrure_de_l_entree_deverrouiller` | Déverrouille serrure entrée (iOS) |
| `ios_serrure_de_l_entree_verrouiller` | Verrouille serrure entrée (iOS) |
| `ios_serrure_du_garage_deverrouiller` | Déverrouille serrure garage (iOS) |
| `notification_ha` | Notification persistante Home Assistant |
| `notification_mail` | Envoi mail |
| `notification_sms` | Envoi Telegram |
| `notification_telephone` | Notification push iPhone |
| `notification_snapshot_du_portier` | Snapshot portier par mail |
| `notification_snapshot_des_cameras` | Captures 8 caméras par mail |
| `notification_vocale` | TTS SONOS multi-mode |
| `reload_pyscript` | Recharge l'intégration pyscript |
| `sonos_radio_sur_la_suite_parentale` | Radio Suite parentale avec sélection horaire |
| `sonos_radio_sur_le_garage` | Radio Garage avec repli |
| `sonos_radio_sur_le_salon` | Radio Salon avec repli |

---

## 📦 Modules complémentaires — Add-ons (19)

[Voir la documentation complète →](docs/addons.md)

> 🏠 **Officiel HA** = dépôt officiel Home Assistant, aucune source supplémentaire à ajouter
> 📦 **Communauté** = dépôt tiers à ajouter manuellement dans les sources d'add-ons

| Add-on | Appareils | Rôle | GitHub | Source |
|---|---|---|---|---|
| EnOcean MQTT | 4 | Passerelle EnOcean | [asera-corp/ha-enoceanmqtt](https://github.com/asera-corp/ha-enoceanmqtt) | 📦 Communauté |
| File editor | — | Éditeur de fichiers | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/configurator) | 🏠 Officiel HA |
| Frigate (Full Access) | — | NVR avec détection d'objets locale pour caméras IP *(arrêté)* | [blakeblackshear/frigate-hass-addons](https://github.com/blakeblackshear/frigate-hass-addons) | 📦 Communauté |
| Gazpar2MQTT | 1 | Données GAZPAR vers MQTT | [ssenart/gazpar2mqtt](https://github.com/ssenart/gazpar2mqtt) | 📦 Communauté |
| Get HACS | — | Installateur HACS | [hacs/get](https://github.com/hacs/get) | 📦 Communauté |
| Home Assistant MCP Server | — | Intégration IA via MCP | [voska/hass-mcp](https://github.com/voska/hass-mcp) | 📦 Communauté |
| Home-Assistant-Matter-Hub | — | Pont Matter vers Alexa/Apple/Google | [t0bst4r/home-assistant-matter-hub](https://github.com/t0bst4r/home-assistant-matter-hub) | 📦 Communauté |
| Homebridge | — | Support HomeKit | [homebridge/homebridge-hassio](https://github.com/homebridge/homebridge-hassio) | 📦 Communauté |
| Matter Server | — | Support Matter | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/matter_server) | 🏠 Officiel HA |
| Mosquitto broker | — | Broker MQTT | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/mosquitto) | 🏠 Officiel HA |
| MQTT Explorer | — | Explorateur MQTT | [thomasloven/hassio-mqtt-explorer](https://github.com/thomasloven/hassio-mqtt-explorer) | 📦 Communauté |
| MyElectricalData | 1 | Données du compteur Linky (Enedis) vers MQTT | [MyElectricalData/myelectricaldata_import](https://github.com/MyElectricalData/myelectricaldata_import) | 📦 Communauté |
| Network UPS Tools | 2 | Supervision des onduleurs (NUT) | [hassio-addons/addon-nut](https://github.com/hassio-addons/addon-nut) | 📦 Communauté |
| OpenThread Border Router | — | Thread/Matter | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/openthread_border_router) | 🏠 Officiel HA |
| Studio Code Server | — | VSCode intégré | [hassio-addons/addon-vscode](https://github.com/hassio-addons/addon-vscode) | 📦 Communauté |
| Terminal & SSH | — | Accès terminal | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/ssh) | 🏠 Officiel HA |
| Z-Wave JS | — | Réseau Z-Wave *(désactivé — remplacé par Z-Wave JS UI)* | [home-assistant/addons](https://github.com/home-assistant/addons/tree/master/zwave_js) | 🏠 Officiel HA |
| Z-Wave JS UI | 25 | Interface Z-Wave JS complète + publication MQTT | [hassio-addons/addon-zwave-js-ui](https://github.com/hassio-addons/addon-zwave-js-ui) | 📦 Communauté |
| Zigbee2MQTT | 22 | Réseau Zigbee | [zigbee2mqtt/hassio-zigbee2mqtt](https://github.com/zigbee2mqtt/hassio-zigbee2mqtt) | 📦 Communauté |

---

## 🛠️ HACS — Intégrations (37)

[Voir la documentation complète →](docs/hacs.md)

> 🔧 **HACS** = disponible dans le catalogue HACS standard, sans dépôt personnalisé
> 🔧 **HACS Communauté** = dépôt tiers à ajouter manuellement dans les sources HACS
> ⚠️ **Dépôt perso** = dépôt GitHub personnel à ajouter manuellement dans HACS

| Intégration | Appareils | Rôle | GitHub | Source |
|---|---|---|---|---|
| Alexa Media Player | 1 | Contrôle des appareils Amazon Alexa | [alandtse/alexa_media_player](https://github.com/alandtse/alexa_media_player) | 🔧 HACS |
| Atmo France | 1 | Qualité de l'air (Cheptainville) | [sebcaps/atmofrance](https://github.com/sebcaps/atmofrance) | 🔧 HACS |
| Battery Notes | — | Suivi des types et dates de remplacement de piles | [andrew-codechimp/HA-Battery-Notes](https://github.com/andrew-codechimp/HA-Battery-Notes) | 🔧 HACS |
| Cork Dork | — | Suivi de la cave à vin par lecture de codes-barres, avec plan des étagères | [BaconWappedBitcoin/ha-wine-cellar](https://github.com/BaconWappedBitcoin/ha-wine-cellar) | 🔧 HACS Communauté |
| CoverAutomatic | 13 | Pilotage automatique des volets, velux et store selon soleil, heure, température et scénario | [slemeur91/CoverAutomatic](https://github.com/slemeur91/CoverAutomatic) | ⚠️ Dépôt perso |
| DomoLink-Mistral IA | — | Diagnostic HA, agent Assist et analyse des journaux par Mistral AI | [SocrateMobile/DomoLink-Mistral](https://github.com/SocrateMobile/DomoLink-Mistral) | 🔧 HACS Communauté |
| Dyson Local | 2 | Intégration locale (sans cloud) des appareils Dyson | [libdyson-wg/ha-dyson](https://github.com/libdyson-wg/ha-dyson) | 🔧 HACS |
| Ecodevices RT2 | 1 | Mesure de consommation multi-circuits (GCE) | [pcourbin/ecodevices_rt2](https://github.com/pcourbin/ecodevices_rt2) | 🔧 HACS |
| EcoFlow Cloud | 2 | Appareils EcoFlow (batterie DELTA Max, PowerStream) | [snell-evan-itt/hassio-ecoflow-cloud-US](https://github.com/snell-evan-itt/hassio-ecoflow-cloud-US) | 🔧 HACS |
| Frigate | 1 | Intégration du NVR Frigate (détection de personnes sur caméra) | [blakeblackshear/frigate-hass-integration](https://github.com/blakeblackshear/frigate-hass-integration) | 🔧 HACS |
| HACS | — | Gestionnaire de contenu communautaire HA | [hacs/integration](https://github.com/hacs/integration) | 🔧 HACS |
| HAGHS | — | Score global de santé de l'instance Home Assistant | [HA-Pulse/home-assistant-global-health-score](https://github.com/HA-Pulse/home-assistant-global-health-score) | 🔧 HACS |
| Heating & Cooling Degree Days | 1 | Degrés-jours de chauffage et de climatisation (base 18 °C) | [alepee/hass-heating_cooling_degree_days](https://github.com/alepee/hass-heating_cooling_degree_days) | 🔧 HACS Communauté |
| Home Architect | — | Éditeur de plan de la maison et tableau de bord associé | [SocrateMobile/home-architect](https://github.com/SocrateMobile/home-architect) | 🔧 HACS Communauté |
| Hue Sync Box | 1 | Synchronisation lumières Philips Hue avec l'HDMI (Hue Play HDMI Sync Box) | [mvdwetering/huesyncbox](https://github.com/mvdwetering/huesyncbox) | 🔧 HACS |
| L'eau d'Ile-de-France | — | Consommation d'eau depuis l'espace client Eau d'Île-de-France *(installée, non configurée)* | [TimoPtr/ha_eauidf](https://github.com/TimoPtr/ha_eauidf) | 🔧 HACS |
| Local Agenda | 5 | Calendriers locaux enrichis pour la planification domotique | [slemeur91/local_agenda](https://github.com/slemeur91/local_agenda) | ⚠️ Dépôt perso |
| LocalTuya | 6 | Contrôle local (sans cloud) des appareils Tuya | [rospogrigio/localtuya](https://github.com/rospogrigio/localtuya) | 🔧 HACS |
| Micronova Agua IOT | 1 | Contrôle du poêle à granulés Jolly Mec via Agua IOT | [vincentwolsink/home_assistant_micronova_agua_iot](https://github.com/vincentwolsink/home_assistant_micronova_agua_iot) | 🔧 HACS |
| Millésime — Cave à Vin | 1 | Inventaire de la cave à vin | [Redsklns/ha-millesime](https://github.com/Redsklns/ha-millesime) | 🔧 HACS Communauté |
| My EcoWatt by RTE | — | Signaux de sobriété électrique RTE | [kamaradclimber/rte-ecowatt](https://github.com/kamaradclimber/rte-ecowatt) | 🔧 HACS |
| Orange Livebox | 1 | Supervision de la Livebox Orange | [cyr-ius/hass-livebox-component](https://github.com/cyr-ius/hass-livebox-component) | 🔧 HACS |
| PDF Scrape | — | Création de capteurs à partir de fichiers PDF en ligne *(installée, non configurée)* | [iluvdata/pdf_scrape](https://github.com/iluvdata/pdf_scrape) | 🔧 HACS |
| Powercalc | 16 | Estimation de la consommation électrique des lumières | [bramstroker/homeassistant-powercalc](https://github.com/bramstroker/homeassistant-powercalc) | 🔧 HACS |
| pyscript | 3 | Scripts Python avancés dans HA (gazpar_energy, linky_energy, surveillance_station_recording) | [custom-components/pyscript](https://github.com/custom-components/pyscript) | 🔧 HACS |
| Remote Home-Assistant | 4 | Liaison entre deux instances Home Assistant | [custom-components/remote_homeassistant](https://github.com/custom-components/remote_homeassistant) | 🔧 HACS |
| Restart Guard | — | Avertit avant un redémarrage de HA si une automatisation planifiée est en cours ou imminente | [igraph100/ha-restart-guard](https://github.com/igraph100/ha-restart-guard) | 🔧 HACS Communauté |
| RfPlayer | 2 | Récepteur/émetteur RF 433/868 MHz (GCE RFPlayer) | [gce-electronics/HA_RFPlayer](https://github.com/gce-electronics/HA_RFPlayer) | 🔧 HACS Communauté |
| Somfy Protexial | 1 | Centrale d'alarme Somfy Protexial | [AuroreVgn/somfy-protexial](https://github.com/AuroreVgn/somfy-protexial) | 🔧 HACS Communauté |
| Spook | — | Services supplémentaires et détection d'entités orphelines | [frenck/spook](https://github.com/frenck/spook) | 🔧 HACS |
| Streaming Top FR | — | Classement des films et séries des plateformes de streaming françaises | [PourLePlaisir-HA/Streaming-Top-FR](https://github.com/PourLePlaisir-HA/Streaming-Top-FR) | 🔧 HACS Communauté |
| Suivi Stock Pellet | 1 | Stock, consommation et achats de granulés de bois | [cyclope205/suivi-stock-pellet](https://github.com/cyclope205/suivi-stock-pellet) | 🔧 HACS Communauté |
| Vacances Scolaires | — | Calendrier des vacances scolaires françaises (zone C) | [Master13011/vacances-scolaire-HA](https://github.com/Master13011/vacances-scolaire-HA) | 🔧 HACS |
| Vigilance Météo France | 1 | Vigilance Météo-France par département (Essonne) avec carte Lovelace intégrée | [Pulpyyyy/meteo_france_vigilance](https://github.com/Pulpyyyy/meteo_france_vigilance) | 🔧 HACS Communauté |
| WashData | 3 | Détection des cycles de lavage par analyse de consommation électrique | [3dg1luk43/ha_washdata](https://github.com/3dg1luk43/ha_washdata) | 🔧 HACS |
| Xiaomi Miot | 2 | Appareils Xiaomi via protocole MIoT local | [al-one/hass-xiaomi-miot](https://github.com/al-one/hass-xiaomi-miot) | 🔧 HACS |
| xsense | 4 | Détecteurs de fumée/CO X-Sense (cloud) | [Jarnsen/ha-xsense-component_test](https://github.com/Jarnsen/ha-xsense-component_test) | 🔧 HACS Communauté |

### Cartes Lovelace HACS (21)

| Carte | Utilisation | Rôle | GitHub | Source |
|---|---|---|---|---|
| apexcharts-card | 4 | Graphiques avancés (consommation énergie) | [RomRider/apexcharts-card](https://github.com/RomRider/apexcharts-card) | 🔧 HACS |
| Battery State Card | 1 | Tableau de bord des niveaux de batteries | [maxwroc/battery-state-card](https://github.com/maxwroc/battery-state-card) | 🔧 HACS |
| button-card | 3 | Bouton personnalisable (état animé des appareils de lavage) | [custom-cards/button-card](https://github.com/custom-cards/button-card) | 🔧 HACS |
| card-mod | 1 | CSS personnalisé sur n'importe quelle carte Lovelace | [thomasloven/lovelace-card-mod](https://github.com/thomasloven/lovelace-card-mod) | 🔧 HACS |
| Custom-ui | — | Templates et couleurs d'icônes personnalisés | [Mariusthvdb/custom-ui](https://github.com/Mariusthvdb/custom-ui) | 🔧 HACS |
| Decluttering Card | — | Templates réutilisables pour réduire la duplication dans les dashboards | [custom-cards/decluttering-card](https://github.com/custom-cards/decluttering-card) | 🔧 HACS |
| expander-card | — | Carte extensible/rétractable pour les dashboards | [MelleD/lovelace-expander-card](https://github.com/MelleD/lovelace-expander-card) | 🔧 HACS |
| GrDF Gazpar card | 1 | Affichage des données de consommation GAZPAR | [ssenart/lovelace-gazpar-card](https://github.com/ssenart/lovelace-gazpar-card) | 🔧 HACS Communauté |
| HA Appliance Card | 4 | Carte pour lave-linge, sèche-linge, lave-vaisselle et réfrigérateur | [ADNPolymerase/ha-appliance-card](https://github.com/ADNPolymerase/ha-appliance-card) | 🔧 HACS |
| HA Printer Card | 1 | Carte d'imprimante (état, niveaux de toner) | [ADNPolymerase/ha-printer-card](https://github.com/ADNPolymerase/ha-printer-card) | 🔧 HACS Communauté |
| ha-floorplan | — | Plan interactif SVG avec états d'entités superposés | [ExperienceLovelace/ha-floorplan](https://github.com/ExperienceLovelace/ha-floorplan) | 🔧 HACS |
| Helios | 1 | Visualisation 2.5D de la maison et de la course du soleil | [ReikanYsora/Helios](https://github.com/ReikanYsora/Helios) | 🔧 HACS |
| Kiosk Mode | — | Masque l'en-tête/sidebar HA pour affichage kiosque | [NemesisRE/kiosk-mode](https://github.com/NemesisRE/kiosk-mode) | 🔧 HACS |
| Linky Content Card | 1 | Affichage de la consommation Linky (avec EcoWatt et Tempo) | [MyElectricalData/content-card-linky](https://github.com/MyElectricalData/content-card-linky) | 🔧 HACS Communauté |
| Mushroom | 15 | Cartes épurées (cycles des appareils de lavage) | [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom) | 🔧 HACS |
| Pollenprognos Card | 1 | Prévisions des pollens et qualité de l'air (Atmo France) | [krissen/pollenprognos-card](https://github.com/krissen/pollenprognos-card) | 🔧 HACS |
| Somfy Protexial Card | 1 | Contrôle de l'alarme Somfy Protexial (capteurs, GSM) | [developpeurbox/somfy-protexial-card](https://github.com/developpeurbox/somfy-protexial-card) | 🔧 HACS Communauté |
| Stack In Card | — | Regroupe plusieurs cartes en une seule sans bordures | [custom-cards/stack-in-card](https://github.com/custom-cards/stack-in-card) | 🔧 HACS |
| Travel Time Card | 1 | Temps de trajet (durée, distance, itinéraire) — remplace Waze Travel Time Card | [ljmerza/travel-time-card](https://github.com/ljmerza/travel-time-card) | 🔧 HACS |
| WallPanel | — | Mode panneau mural et économiseur d'écran photo | [j-a-n/lovelace-wallpanel](https://github.com/j-a-n/lovelace-wallpanel) | 🔧 HACS |
| WashData Card | 3 | Affichage des cycles de lavage (lave-linge, lave-vaisselle, sèche-linge) | [technogrady/ha_washdata_card](https://github.com/technogrady/ha_washdata_card) | 🔧 HACS Communauté |

---

## 🏗️ Architecture

```
Réseau Z-Wave    → Z-Wave JS UI (zwavejs2mqtt) → MQTT → HA
Réseau Zigbee    → Zigbee2MQTT               → MQTT → HA
EnOcean          → EnOcean MQTT              → MQTT → HA
GAZPAR           → Gazpar2MQTT               → MQTT → HA
Linky            → MyElectricalData          → MQTT → HA
Appareils locaux → Intégrations natives HA
Appareils cloud  → Intégrations HACS
```

---

## 📄 Licence

Cette configuration est partagée sous licence MIT. Libre à vous de l'adapter à votre installation.
