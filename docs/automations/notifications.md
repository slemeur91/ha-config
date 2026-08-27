# Notifications (15)

[← Retour README](../../README.md)


---

## `automation.notification_appareils_en_batterie_faible` — Notification Batterie Faible
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_threshold` (batterie passée sous le seuil)
- `battery_notes_battery_threshold` (batterie revenue au-dessus du seuil)

**Fonctionnement :**
1. Batterie faible → crée une notification persistante (appareil, niveau, type de pile).
2. Batterie OK → supprime la notification persistante.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_appareils_en_batterie_faible_hebdomadaire` — Vérification Hebdomadaire Batteries
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible_hebdomadaire.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Chaque vendredi à 19h00

**Fonctionnement :**
1. Lance `battery_notes.check_battery_low` pour forcer une vérification complète.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_appareils_en_batterie_faible_mail_hebdomadaire` — Notification Mail Hebdomadaire Batteries
> [📄 Voir le YAML](../../automations/notification_appareils_en_batterie_faible_mail_hebdomadaire.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Hebdomadaire (selon configuration)

**Fonctionnement :**
1. Envoie un mail récapitulatif des appareils dont la batterie est sous le seuil d'alerte.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_batterie_remplacee` — Batterie Remplacée
> [📄 Voir le YAML](../../automations/notification_de_batterie_remplacee.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_increased` (niveau de batterie en hausse significative)

**Fonctionnement :**
1. Appelle `script.notification_ha` (fire-and-forget via `script.turn_on`) avec un message adapté selon le type de batterie : rechargeable ("rechargée") ou pile ("remplacée"), mentionnant le niveau avant/après.
2. `notification_id` stable par appareil (`battery_increased-device_id-source_entity_id`) pour éviter les doublons si l'évènement se répète.

**Entités principales :** `script.notification_ha`, événement `battery_notes_battery_increased`

---

## `automation.notification_de_capteur_deporte_du_chauffage_desactive` — Notification de capteur déporté du chauffage désactivé
> [📄 Voir le YAML](../../automations/notification_du_capteur_deporte_du_chauffage_desactive.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- L'un des 5 capteurs sonde de température des chauffages de l'étage passe à « Non Détecté » (off)
- Planification hebdomadaire tous les vendredis à 08h00
- Déclenchement manuel

**Fonctionnement :**
1. Quel que soit le déclencheur → vérifie les 5 capteurs et crée une notification pour chacun actuellement à off. Le `notification_id` évite les doublons dans l'interface.

**Entités principales :**
- `binary_sensor.chauffage_du_bureau_nodeid_2_temperature_sensor`
- `binary_sensor.chauffage_de_la_chambre_nodeid_6_temperature_sensor`
- `binary_sensor.chauffage_de_la_suite_parentale_nodeid_3_temperature_sensor`
- `binary_sensor.chauffage_de_la_salle_d_eau_nodeid_4_temperature_sensor`
- `binary_sensor.chauffage_de_la_salle_de_bain_nodeid_5_temperature_sensor`
- `script.notification_ha` : création de la notification persistante

---

## `automation.notification_de_defaut_du_refrigerateur` — Notification de défaut du réfrigérateur
> [📄 Voir le YAML](../../automations/notification_de_defaut_du_refrigerateur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de température frigo ou congélateur
- Déconnexion réseau de l'interface du réfrigérateur (`device_tracker.samsung_refrigerator`)

**Fonctionnement :**
1. Si frigo hors [2-4°C] OU congélateur hors [-20 à -18°C] OU interface réseau absente → SMS d'alerte.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_l_horloge` — Notification de l'Horloge
> [📄 Voir le YAML](../../automations/notification_de_l_horloge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Toutes les heures (time_pattern)

**Conditions :** Après 10h30

**Fonctionnement :**
1. Compose le message vocal selon l'heure (midi, minuit, 1h, 21h, ou formule générique).
2. Lance `script.notification_vocale`.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_des_alertes` — Notification des Alertes
> [📄 Voir le YAML](../../automations/notification_des_alertes.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Température/luminosité armoire de brassage et grenier
- Détecteurs d'eau (SdB, Cuisine, Cellier)
- Serveurs réseau (slm-disk3, slm-disk4, ZappitiNAS, Livebox)
- Brouillage RF (`binary_sensor.jamming_0_detector`)
- Détecteurs de fumée (Séjour, Cellier, Étage) — montée et descente

**Fonctionnement :**
1. Chaque alerte compose un message via un `input_boolean` garde-fou anti-doublon.
2. Fuite d'eau → ferme/ouvre automatiquement la vanne d'arrivée d'eau.
3. Si message → notifie via vocal + mail + SMS.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.temperature_armoire` | input_boolean | Garde-fou alerte température |
| `input_boolean.luminosite_armoire` | input_boolean | Garde-fou alerte luminosité |
| `input_boolean.luminosite_grenier` | input_boolean | Garde-fou alerte grenier |
| `input_boolean.fuite_sdb` | input_boolean | Garde-fou fuite SdB |
| `input_boolean.fuite_cuisine` | input_boolean | Garde-fou fuite Cuisine |
| `input_boolean.fuite_cellier` | input_boolean | Garde-fou fuite Cellier |
| `input_boolean.brouillage_reseau` | input_boolean | Garde-fou brouillage RF |
| `input_boolean.etat_zapittinas` | input_boolean | État NAS ZappitiNAS |
| `input_boolean.detection_fumee` | input_boolean | Garde-fou détection de fumée |

---

## `automation.notification_des_poubelles` — Notification des Poubelles
> [📄 Voir le YAML](../../automations/notification_des_poubelles.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.poubelles` (déclenché par calendrier permanent)

**Fonctionnement :**
1. Compose le message selon l'option (Sortir/Rentrer Marron/Verte/Jaune).
2. Notification vocale + SMS.
3. Remet le sélecteur à "Aucune".

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.poubelles` | input_select | Sortir Marron, Rentrer Marron, Sortir Jaune, Rentrer Jaune, Sortir Verte, Rentrer Verte, Aucune |

---

## `automation.notification_du_portier` — Notification du Portier

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Sonnette du portier (`binary_sensor.exterieur_slm_portier_visiteur` → on) — **actif**
- Présence devant le portier (`binary_sensor.exterieur_slm_portier_personne` → on) — désactivé
- Mouvement devant le portier (`binary_sensor.exterieur_slm_portier_mouvement_2`) — désactivé

**Fonctionnement :**
1. Selon le déclencheur, compose la variable `message_portier` : "Appuis sur la sonnette", "Présence devant le portier" ou "Mouvement devant le portier".
2. Appelle `script.notification_snapshot_du_portier` via `script.turn_on` (fire-and-forget) avec le type et le message.

**Entités utilisées :** `binary_sensor.exterieur_slm_portier_visiteur`, `binary_sensor.exterieur_slm_portier_personne`, `binary_sensor.exterieur_slm_portier_mouvement_2`, `script.notification_snapshot_du_portier`

---

## `automation.notification_de_la_boite_aux_lettres` — Notification de la Boîte aux Lettres
> [📄 Voir le YAML](../../automations/notification_de_la_boite_aux_lettres.yaml)

**Statut :** En test | **Evolution :** Corrections

**Déclencheurs :**
- Fermeture de la porte principale (`binary_sensor.porte_boite_aux_lettres` → off) — cas colis
- Fermeture de la trappe à lettres (`binary_sensor.trappe_boite_aux_lettres` → off), uniquement si la porte est déjà fermée — cas lettre

**Fonctionnement :**
1. Porte principale refermée → compose "colis".
2. Trappe refermée (porte déjà fermée) → compose "lettre".
3. Envoie mail + SMS (notification vocale désactivée).

**Entités principales :**
- `binary_sensor.porte_boite_aux_lettres`, `binary_sensor.trappe_boite_aux_lettres`
- `script.notification_mail`, `script.notification_sms`

---

## `automation.notification_de_coupure_de_courant_edf` — Notification de coupure de courant EDF
> [📄 Voir le YAML](../../automations/notification_de_coupure_de_courant_edf.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.ecoflow_ac_in_volts` passe sous 100V pendant 60s (coupure confirmée)
- `sensor.ecoflow_ac_in_volts` repasse au-dessus de 100V pendant 30s (rétablissement)

**Fonctionnement :**
1. Coupure (60s sous 100V) → active le verrou `input_boolean.coupure_edf_en_cours`, notifie le téléphone.
2. Rétablissement (30s au-dessus de 100V) ET verrou actif → désactive le verrou, notifie.

**Note :** Le verrou évite les fausses alertes "rétabli" lors des micro-coupures de communication EcoFlow (~5–10s) qui ne sont pas de vraies coupures secteur.

**Entités principales :**
- `sensor.ecoflow_ac_in_volts` : tension secteur mesurée par l'onduleur EcoFlow DELTA Max
- `input_boolean.coupure_edf_en_cours` : verrou anti-faux-positifs
- `script.notification_telephone` : notification push iPhone

---

## `automation.notification_des_alertes_de_defaut_des_onduleurs_ups` — Notification des Alertes de défaut des Onduleurs - UPS
> [📄 Voir le YAML](../../automations/notification_des_alertes_de_defaut_des_onduleurs_ups.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.reseau_ups_alarmes` passe à "Replace battery!" (onduleur réseau Ups)
- Changement de `sensor.eaton_usb_code_d_etat` (onduleur Eaton_Usb, code NUT ups.status)

**Conditions :**
- Pour Eaton_Usb : le code d'état contient un flag anormal (hors OL/OB/CHRG/DISCHRG : RB, LB, BYPASS, OFF, OVER, TRIM, BOOST, FSD, CAL)

**Fonctionnement :**
1. Onduleur Ups (réseau) : "Replace battery!" détecté → notifie qu'un remplacement de batterie est nécessaire.
2. Onduleur Eaton_Usb : code NUT anormal → traduit chaque flag (RB, LB, BYPASS…) en description lisible et notifie.
3. Deux branches avec `notification_id` distinct pour éviter les doublons.

**Entités principales :**
- `sensor.reseau_ups_alarmes` : alarme texte de l'onduleur réseau
- `sensor.eaton_usb_code_d_etat` : code d'état NUT de l'onduleur Eaton_Usb
- `script.notification_ha` : envoi des notifications

---

## `automation.notification_d_ouverture_ou_fermeture_des_fenetres` — Notification d'Ouverture ou Fermeture des fenêtres
> [📄 Voir le YAML](../../automations/notification_d_ouverture_ou_fermeture_des_fenetres.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement des températures intérieures/extérieure, prévision Météo-France, consignes volet (chaud/froid/pluie), mode été/hiver, indicateurs de pluie (prévision + pluviomètre)
- Changement de `input_select.domicile`

**Conditions :**
- `input_select.domicile` = "Présent"

**Fonctionnement :**
1. Calcule pour chaque pièce (Bureau, Suite parentale, Cellier, Rez-de-chaussée) si une annonce fermeture/ouverture est justifiée : comparaison intérieur/extérieur avec hystérésis à deux seuils, détection d'ouverture via l'attribut `Door open` (`open`/`closed`) des `binary_sensor.do_*` (et non leur état principal, qui peut rester bloqué), garde anti-pluie pour l'ouverture (prévision + pluviomètre), vérification que le volet n'est pas fermé.
2. Regroupe les pièces en deux annonces vocales max (une fermeture, une ouverture), accord singulier/pluriel automatique.
3. Anti-répétition par pièce et par sens : bloqué 15 minutes via horodatage dans des helpers `input_datetime` dédiés.

**Entités principales :**
- `sensor.netatmo_*_temperature`, `sensor.detecteur_du_cellier_nodeid_29_temperature_air` : températures
- `binary_sensor.do_*` : détecteurs d'ouverture
- `input_number.volet_consigne_*` : seuils de déclenchement
- `input_datetime.annonce_fenetre_*` : anti-répétition par pièce/sens
- `script.notification_vocale` : annonce vocale

---

## `automation.suspension_des_notifications_en_mode_invites` — Suspension des Notifications en Mode Invités
> [📄 Voir le YAML](../../automations/suspension_des_notifications_en_mode_invites.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_boolean.invites` passe à "on"
- `input_boolean.invites` passe à "off"

**Fonctionnement :**
1. Invités actifs → désactive `automation.gestion_des_alertes` et `automation.notification_d_ouverture_ou_fermeture_des_fenetres`.
2. Fin mode invités → réactive ces deux automatisations.

**Entités principales :**
- `input_boolean.invites` : déclencheur mode invités
- `automation.gestion_des_alertes`, `automation.notification_d_ouverture_ou_fermeture_des_fenetres` : cibles
