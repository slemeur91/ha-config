# Corrections (10)

[← Retour README](../../README.md)

---

## `automation.corrections_des_appareils_ecoflow` — Corrections EcoFlow
> [📄 Voir le YAML](../../automations/corrections_des_appareils_ecoflow.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.powerstream_6231_status` ou `sensor.ecoflow_status` → "assume_offline"
- Lever du soleil

**Fonctionnement :**
1. Attend 5 s.
2. PowerStream offline + soleil levé → cycle désactivation/réactivation (15 s).
3. EcoFlow offline → même cycle.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.klf200_filet_de_securite_de_la_prise` — KLF200 - Filet de sécurité de la prise
> [📄 Voir le YAML](../../automations/klf200_filet_de_securite_de_la_prise.yaml)

**Statut :** Nouveau (créé le 11/10/2026, désactivé en attente de validation) — remplace `Sécurité KLF200 - Remise sous tension` | **Evolution :** Aucune

**Rôle :** garantit que la prise du KLF200 ne reste jamais éteinte, quelle qu'en soit la cause (coupure manuelle oubliée, échec de la remise sous tension dans `KLF200 - Surveillance et réparation graduée`, redémarrage de HA pendant une coupure). Totalement indépendante de l'automatisation de réparation : celle-ci ne coupe que 30 secondes, donc les deux n'entrent jamais en concurrence.

**Déclencheurs :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200` éteinte depuis 5 minutes — id: off_5min
- Démarrage de Home Assistant — id: start

**Fonctionnement :**
1. Démarrage HA → attend 5 minutes (le temps que la multiprise soit joignable).
2. Si la prise est éteinte → la rallume, attend 3 minutes, puis recharge l'intégration Velux.
3. Si elle est allumée → ne fait rien.

**Entités principales :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200` : alimentation de la passerelle KLF200
- Intégration Velux (entry_id `01K2GS1XM2TFEEMYCJBXSQQJHQ`)

---

## `automation.klf200_redemarrage_de_la_passerelle_a_l_arret_de_ha` — KLF200 - Redémarrage de la passerelle à l'arrêt de HA
> [📄 Voir le YAML](../../automations/klf200_redemarrage_de_la_passerelle_a_l_arret_de_ha.yaml)

**Statut :** Nouveau (créé le 11/10/2026, désactivé en attente de validation) — à vérifier sur un redémarrage réel | **Evolution :** Aucune

**Rôle :** prévention. Le KLF200 n'accepte qu'une ou deux connexions et ne libère pas toujours celle de Home Assistant quand celui-ci s'arrête ; il peut alors refuser la reconnexion au démarrage suivant. Redémarrer la passerelle au moment où HA s'arrête la laisse propre pour le retour. C'est l'ancien correctif de la documentation officielle (`velux.reboot_gateway`), adapté au bouton qui a remplacé cette action.

**Déclencheurs :**
- Arrêt de Home Assistant (`homeassistant shutdown`)

**Fonctionnement :**
1. Appuie sur `button.klf_200_gateway_redemarrer`.

**Limite :** à l'arrêt, HA ne laisse qu'environ 20 secondes aux automatisations ; il faut vérifier sur un redémarrage que l'appui a bien le temps d'aboutir (horodatage du bouton mis à jour).

**Entités principales :**
- `button.klf_200_gateway_redemarrer` : redémarrage logiciel de la passerelle

---

## `automation.klf200_surveillance_et_reparation_graduee` — KLF200 - Surveillance et réparation graduée
> [📄 Voir le YAML](../../automations/klf200_surveillance_et_reparation_graduee.yaml)

**Statut :** Nouveau (créé le 11/10/2026, désactivé en attente de validation) — remplace `Correction de l'intégration du KLF200` et `KLF200 - Surveillance et réparation automatique` | **Evolution :** À l'activation, exclure l'intégration Velux de `Rechargement des intégrations en défaut` pour qu'une seule automatisation s'en occupe.

**Principe :** détection patiente (5 min), réparation du plus doux au plus fort, nombre d'essais limité. Les anciennes versions coupaient la prise avant que la passerelle ait fini de se reconnecter (environ 3 min après remise sous tension), ce qui entretenait des cycles de coupure.

**Déclencheurs :**
- Démarrage de Home Assistant — id: start
- Ping du KLF200 (`binary_sensor.192_168_52_67`) à off depuis 5 minutes — id: fault
- Un des 7 volets/Velux indisponible depuis 5 minutes — id: fault

**Défaut avéré :** ping perdu OU les 7 volets/Velux tous indisponibles. Ce test est refait avant chaque étape ; dès qu'il est faux, l'automatisation s'arrête.

**Fonctionnement :**
1. Démarrage HA → attend 10 minutes avant tout contrôle (en mode `single`, les signaux de défaut reçus pendant ce délai sont ignorés).
2. Étape 1, si le ping répond → recharge l'intégration Velux, attend 5 minutes.
3. Étape 2, si le ping répond et que le bouton est disponible → redémarre la passerelle par `button.klf_200_gateway_redemarrer`, attend 5 minutes.
4. Étape 3, jusqu'à 3 fois tant que le défaut persiste → coupe la prise 30 secondes, la rallume, attend 2 minutes, recharge l'intégration, puis attend 5, 10 puis 15 minutes selon l'essai.
5. Bilan → si le défaut persiste : notification HA + téléphone et arrêt (pas de nouvel essai tant qu'un nouveau signal de défaut n'apparaît pas) ; sinon : notification HA de réparation réussie.

**Mode `single` (max_exceeded silencieux) :** un seul cycle à la fois, d'une durée maximale d'environ 1 heure.

**Entités principales :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200` : alimentation de la passerelle KLF200
- `binary_sensor.192_168_52_67` : ping réseau du KLF200
- `button.klf_200_gateway_redemarrer` : redémarrage logiciel de la passerelle
- 7 `cover.*` (Velux/volets/pergola) : signal de bon fonctionnement de l'intégration
- Intégration Velux (entry_id `01K2GS1XM2TFEEMYCJBXSQQJHQ`)
- `script.notification_ha` / `script.notification_telephone` : bilan

---

## `automation.rechargement_de_l_integration_localtuya` — Rechargement de l'intégration LocalTuya
> [📄 Voir le YAML](../../automations/rechargement_de_l_integration_localtuya.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant

**Fonctionnement :**
1. Attend 4 minutes après le démarrage de HA (laisse le temps au réseau/aux appareils Tuya locaux d'être joignables).
2. Recharge l'intégration LocalTuya (`localtuya.reload`).

**Entités principales :**
- Intégration LocalTuya

---

## `automation.rechargement_de_l_integration_netatmo` — Rechargement de l'intégration Netatmo
> [📄 Voir le YAML](../../automations/rechargement_de_l_integration_netatmo.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant
- Vérification périodique toutes les 15 minutes

**Conditions :**
- Les 7 entités Connectivité Netatmo (une par module) sont toutes indisponibles

**Fonctionnement :**
1. Démarrage HA → attend 3 minutes (laisse le temps à l'intégration de remonter son état).
2. Si les 7 entités Connectivité sont indisponibles → recharge l'intégration Netatmo puis envoie une notification persistante.

**Entités principales :**
- `binary_sensor.netatmo_*_connectivite` (7 modules)
- Intégration Netatmo

---

## `automation.redemarrage_de_l_integration_otbr_sur_cpu_eleve` — Redémarrage de l'intégration OTBR sur CPU élevé
> [📄 Voir le YAML](../../automations/redemarrage_de_l_integration_otbr_sur_cpu_eleve.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant — id: Démarrage
- `sensor.system_monitor_utilisation_du_processeur` au-dessus de 30% pendant 2 minutes (à tout moment)

**Conditions :**
- `sensor.system_monitor_utilisation_du_processeur` dépasse 30% au moment du contrôle

**Fonctionnement :**
1. Si le déclencheur est le démarrage de HA, attend 4 minutes (laisse le temps aux apps/intégrations de se stabiliser).
2. Si le CPU global dépasse 30% → redémarre l'app OpenThread Border Router (connue pour parfois rester bloquée à haute consommation CPU) puis envoie une notification persistante.

**Remarque :** le texte de la notification mentionne '4 minutes après le démarrage de HA' même lorsque le déclencheur est le dépassement CPU en cours de fonctionnement.

**Entités principales :**
- `sensor.system_monitor_utilisation_du_processeur`
- App `core_openthread_border_router`

---

## `automation.correction_du_mi_air_purifier` — Correction du Mi Air Purifier
> [📄 Voir le YAML](../../automations/correction_du_mi_air_purifier.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheur :**
- `fan.zhimi_m1_6186_air_purifier` reste indisponible pendant 30 secondes (le purificateur ne répond plus)

**Condition :** le purificateur est toujours indisponible au moment de l'exécution.

**Fonctionnement :**
1. Vérifie l'état de `switch.multiprise_du_salon_droite_2_purificateur` (Prise 2 - Purificateur).
2. Si elle est allumée : l'éteint, attend 1 minute, la rallume, réactive l'appareil dans Home Assistant (`homeassistant.enable_device`), puis attend encore 1 minute (temporisation qui, en mode `single`, bloque tout nouveau cycle pendant ce temps).
3. Si elle est déjà éteinte : ne fait rien.

**Entités principales :**
- `fan.zhimi_m1_6186_air_purifier` : signal de bon fonctionnement du purificateur
- `switch.multiprise_du_salon_droite_2_purificateur` : alimentation du purificateur (Prise 2 de la multiprise du salon droite)

---

## `automation.correction_de_l_onduleur` — Correction de l'Onduleur
> [📄 Voir le YAML](../../automations/correction_de_l_onduleur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune.

**Déclencheurs :**
- Démarrage de Home Assistant (`homeassistant start`) — id: Démarrage
- `sensor.eaton_usb_etat` reste `unavailable`/`unknown` pendant 2 minutes
- `sensor.eaton_usb_code_d_etat` reste `unavailable`/`unknown` pendant 2 minutes

**Fonctionnement :**
1. Si le déclencheur est le démarrage de HA, attend 4 minutes (le temps que l'intégration NUT tente de se reconnecter à l'onduleur).
2. Vérifie l'état de l'onduleur Eaton_Usb (`sensor.eaton_usb_etat` et `sensor.eaton_usb_code_d_etat`).
3. Si l'un des deux est `unavailable`/`unknown` (intégration NUT en défaut), redémarre l'app 'Network UPS Tools' (`a0d7b954_nut`).
4. Sinon, ne fait rien.

**Entités principales :**
- `sensor.eaton_usb_etat` : état de l'onduleur Eaton_Usb
- `sensor.eaton_usb_code_d_etat` : code d'état NUT de l'onduleur Eaton_Usb
- App `Network UPS Tools` (`a0d7b954_nut`) : redémarrée en cas de défaut

---

## `automation.maintien_des_prises_et_appareils_allumes` — Maintien des Prises et Appareils allumés
> [📄 Voir le YAML](../../automations/maintien_des_prises_et_appareils_allumes.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Prises critiques éteintes depuis 30 secondes (réfrigérateur, multimédia, informatique, cellier)
- Changement d'état stable 30 secondes des prises routeur 4G et ZappitiNAS ; changement immédiat de la prise du ventilateur de l'informatique
- Changement d'état stable 30 secondes de la prise du purificateur (id: Purificateur) ou du ventilateur du salon (id: Ventilateur)
- Changement du device tracker ZappitiNAS

**Fonctionnement :**
1. Après 5 secondes de délai, vérifie en parallèle chaque appareil.
2. Rallume automatiquement tout switch critique qui serait éteint (protection coupures accidentelles).
3. Si ZappitiNAS ne répond plus depuis 2 min alors que le switch est allumé → force le Wake-on-LAN via `switch.zappitinas`.
4. Sur déclencheur Purificateur : active/désactive l'appareil purificateur (Mi Air) dans HA selon l'état de sa prise.
5. Sur déclencheur Ventilateur : active/désactive l'intégration du ventilateur (Dyson) selon l'état de sa prise.

**Entités principales :**
- `switch.prise_du_refrigerateur_switch` / `prise_du_multimedia_switch` / `prise_de_l_informatique` : prises critiques
- `switch.zappitinas` : Wake-on-LAN NAS
- `device_tracker.zappitinas_zappitinas` : supervision réseau NAS

**Entrées utilisées :** Aucune entrée helper.

---

