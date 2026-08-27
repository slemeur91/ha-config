# Corrections (9)

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

## `automation.correction_de_l_integration_du_klf200_passerelle_des_volets_velux` — Correction de l'intégration KLF200 — Passerelle des Volets/Velux
> [📄 Voir le YAML](../../automations/correction_de_l_integration_du_klf200_passerelle_des_volets_velux.yaml)

**Statut :** Finalisé | **Evolution :** Remise sous tension après coupure prolongée déplacée dans `automation.securite_klf200_remise_sous_tension` pour garantir qu'elle se déclenche toujours même si cette file d'attente est saturée.

**Déclencheurs :**
- Démarrage de Home Assistant
- Vérification périodique toutes les 15 minutes
- `binary_sensor.192_168_52_67` (ping KLF200) passe à off/unknown/unavailable
- `button.klf_200_gateway_redemarrer` passe à indisponible
- Une des 7 entités Velux/volets passe à indisponible

**Fonctionnement :**
1. Démarrage HA → attend 3 minutes ; si la prise est éteinte → la rallume, attend 2 mn, recharge l'intégration, arrête.
2. Signal de défaut → attend 4 minutes.
3. Vérifie si la passerelle est réellement en défaut (ping perdu OU bouton indisponible OU les 7 volets/Velux tous indisponibles) :
   - Si oui : recharge l'intégration, attend 3 minutes, revérifie ; si toujours en défaut → coupe la prise et arrête (la remise sous tension est prise en charge par `Sécurité KLF200`).
   - Si non : rien.

**Mode :** `queued`, max 10, `max_exceeded: warning` — plusieurs signaux simultanés (7 volets qui passent indisponibles en même temps) sont mis en file et exécutés séquentiellement.

**Entités principales :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200`, `binary_sensor.192_168_52_67`, `button.klf_200_gateway_redemarrer`
- 7 `cover.*` (Velux/volets/pergola)
- Intégration KLF200 (entry_id `01K2GS1XM2TFEEMYCJBXSQQJHQ`)

---

## `automation.securite_klf200_remise_sous_tension` — Sécurité KLF200 - Remise sous tension
> [📄 Voir le YAML](../../automations/securite_klf200_remise_sous_tension.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheur :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200` reste éteinte 5 minutes

**Fonctionnement :**
Filet de sécurité totalement indépendant de `Correction de l'intégration du KLF200`. Dès que la prise reste éteinte 5mn (coupure délibérée par l'automatisation de correction, coupure secteur, ou toute autre cause) → rallume, attend 3 minutes, recharge l'intégration KLF200.

**Pourquoi une automatisation séparée :** avant le 9 août 2026, cette logique faisait partie de `Correction KLF200` (mode `queued`). Le déclencheur de remise sous tension pouvait être perdu si la file était pleine — la prise est restée éteinte plusieurs heures dans la nuit du 9 août. En mode `single` indépendant, il ne peut plus être mis en concurrence.

**Entités principales :**
- `switch.reseau_multiprise_de_l_informatique_2_klf_200`
- Intégration KLF200 (entry_id `01K2GS1XM2TFEEMYCJBXSQQJHQ`)

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
- Démarrage de Home Assistant
- `sensor.system_monitor_utilisation_du_processeur` dépasse 30% pendant 2 minutes (surveillance continue)

**Conditions :**
- `sensor.system_monitor_utilisation_du_processeur` dépasse 30% au moment d'agir

**Fonctionnement :**
1. Si démarrage HA → attend 4 minutes (laisse le temps aux add-ons/intégrations de se stabiliser).
2. Si CPU > 30% → redémarre l'add-on OpenThread Border Router (connu pour rester bloqué à haute consommation après certains redémarrages) puis envoie une notification persistante.

**Entités principales :**
- `sensor.system_monitor_utilisation_du_processeur`
- Add-on `core_openthread_border_router`

---

## `automation.correction_du_mi_air_purifier` — Correction du Mi Air Purifier
> [📄 Voir le YAML](../../automations/correction_du_mi_air_purifier.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheur :**
- `fan.zhimi_m1_6186_air_purifier` passe à indisponible 30s (le purificateur ne répond plus)

**Fonctionnement :**
1. Si `switch.multiprise_du_salon_droite_2_purificateur` est allumée → l'éteint, attend 1mn, la rallume puis réactive le device (cycle d'alimentation pour forcer la reconnexion).
2. Si déjà éteinte → ne fait rien.

**Entités principales :**
- `fan.zhimi_m1_6186_air_purifier`, `switch.multiprise_du_salon_droite_2_purificateur`

---

## `automation.correction_de_l_onduleur` — Correction de l'Onduleur
> [📄 Voir le YAML](../../automations/correction_de_l_onduleur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage de Home Assistant (avec délai 4 mn)
- `sensor.eaton_usb_etat` ou `sensor.eaton_usb_code_d_etat` passe à unavailable/unknown 2mn

**Fonctionnement :**
1. Vérifie si l'un des deux sensors est en défaut.
2. Si oui → redémarre l'add-on Network UPS Tools (`a0d7b954_nut`).

**Entités principales :**
- `sensor.eaton_usb_etat`, `sensor.eaton_usb_code_d_etat`, add-on `a0d7b954_nut`

---

## `automation.maintien_des_prises_et_appareils_allumes` — Maintien des Prises et Appareils allumés
> [📄 Voir le YAML](../../automations/maintien_des_prises_et_appareils_allumes.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Switches critiques éteints 30 s (réfrigérateur, multimédia, informatique, cellier, routeur, ventilateur, ZappitiNAS)
- Changement d'état purificateur ou ventilateur
- Changement device tracker ZappitiNAS

**Fonctionnement :**
1. Après 5 s, vérifie et rallume tout switch critique éteint.
2. ZappitiNAS absent 2 min → Wake-on-LAN.
3. Active/désactive intégrations purificateur et ventilateur selon leur switch physique.

**Entrées utilisées :** Aucune entrée helper.
