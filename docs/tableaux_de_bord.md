# 🖥️ Tableaux de bord (3)

[← Retour README](../README.md)

> Tous les tableaux de bord sont en mode **storage** (édités depuis l'interface) et masqués de la barre latérale. Le tableau de bord par défaut n'a pas de configuration enregistrée : Home Assistant affiche sa vue générée automatiquement.

| Tableau de bord | URL | Vues | Statut |
|---|---|---|---|
| [Surveillance HA](#surveillance-ha) | `/dashboard-surveillance` | 12 | En service |
| [iPad](#ipad) | `/tablette-ipad` | 1 (panneau) | 🚧 En cours de construction |
| [Carte](#carte) | `/map` | 1 | En service (administrateurs uniquement) |

---

## Surveillance HA

Tableau de bord principal, organisé en 12 vues.

| Vue | Contenu | Cartes personnalisées |
|---|---|---|
| Home | Processeur (température, charge), trajets, SONOS, HiFi, arrosage, pollution, Zigbee2MQTT et capteurs Zigbee en erreur, vigilance météo | Pollenprognos Card, Travel Time Card, carte Vigilance Météo France |
| Volets | Présence par pièce, modes des volets, pilotage CoverAutomatic | carte CoverAutomatic |
| Chauffage | Domicile, chauffage RDC et étage, climatisation, poêle | — |
| Alarme | Contrôle de l'alarme Somfy Protexial et état des éléments | Somfy Protexial Card (carte principale + éléments) |
| Energie | Consommations gaz et électricité | GrDF Gazpar card, Linky Content Card |
| Eau chaude | Eau chaude vs chauffe-eau, comparaison Linky / télé-info, vue 2.5D de la maison | apexcharts-card, Helios |
| Monitoring | NAS slm-disk3 et slm-disk4, imprimante, score de santé HAGHS, stock de granulés | HA Printer Card, carte Suivi Stock Pellet |
| Batteries | Stock de piles nécessaire, état des batteries | card-mod, Battery State Card |
| Lave Vaisselle | Cycles du lave-vaisselle, du lave-linge et du sèche-linge : état, puissance, début, fin, durée, consommation et coût | WashData Card, HA Appliance Card, button-card, Mushroom, apexcharts-card |
| Streaming | Classement et catalogue des films et séries | cartes Streaming Top FR |
| Cave à vin | Inventaire de la cave | cartes Cork Dork et Millésime |
| Météo | Météo et confort intérieur | cartes Hestia Weather (météo, confort maison, confort par pièce) |

---

## iPad

> 🚧 Tableau de bord en cours de construction : son contenu peut encore évoluer.

Tableau de bord en une seule vue « panneau », conçu pour la tablette murale. Il utilise le mode **WallPanel** (économiseur d'écran) et des cartes stylées avec **card-mod**.

Contenu : horloge, plan 3D de la maison, présence, volets (carte CoverAutomatic), domicile, chauffage RDC et étage, climatisation, poêle, alarme Somfy Protexial, consommations Linky et GAZPAR, charge et température du processeur.

---

## Carte

Carte native de Home Assistant (`map`) affichant les zones et les personnes suivies. Réservée aux administrateurs.

---

## Cartes fournies par les intégrations

En plus des [cartes Lovelace HACS](hacs.md), plusieurs intégrations installent leur propre carte :

| Carte | Intégration | Utilisation |
|---|---|---|
| `custom:cover-automatic-card` | CoverAutomatic | 2 (Surveillance HA, iPad) |
| `custom:meteo-france-vigilance-card` | Vigilance Météo France | 1 |
| `custom:suivi-stock-pellet-card` | Suivi Stock Pellet | 1 |
| `custom:streaming-top-fr-card`, `custom:streaming-top-fr-catalog-card` | Streaming Top FR | 2 |
| `custom:wine-cellar-card` | Cork Dork | 1 |
| `custom:millesime-card` | Millésime — Cave à Vin | 1 |
| `custom:hestia-weather-card`, `custom:hestia-comfort-home-card`, `custom:hestia-comfort-card` | Hestia Weather | 3 |

Une ressource est écrite à la main (ressource « inline ») : la traduction française de la carte Cork Dork, surcouche personnelle qui traduit l'interface sans modifier le fichier d'origine.
