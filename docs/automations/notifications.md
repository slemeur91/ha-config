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
- Chaque vendredi à 19h00

**Fonctionnement :**
1. Parcourt les capteurs de l'intégration Battery Notes et retient ceux dont l'attribut `battery_low` est vrai (nom de l'appareil, niveau, type et quantité de piles).
2. S'arrête sans rien envoyer si aucun appareil n'est en batterie faible.
3. Sinon, compose la liste et envoie un mail récapitulatif (type 'Batteries') via `script.notification_mail`.

**Entités principales :**
- Intégration `battery_notes` : source des niveaux de batterie
- `script.notification_mail` : envoi du mail récapitulatif

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_de_batterie_remplacee` — Batterie Remplacée
> [📄 Voir le YAML](../../automations/notification_de_batterie_remplacee.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `battery_notes_battery_increased` (niveau de batterie en hausse significative)

**Fonctionnement :**
1. Appelle `script.notification_ha` (fire-and-forget via `script.turn_on`) avec un message adapté selon le type de batterie : rechargeable ("rechargée") ou pile ("remplacée"), mentionnant le niveau avant/après.
2. `message_id` stable par appareil (`battery_increased-device_id-source_entity_id`) pour éviter les doublons si l'évènement se répète.

**Entités principales :** `script.notification_ha`, événement `battery_notes_battery_increased`

---

## `automation.notification_de_capteur_deporte_du_chauffage_desactive` — Notification de capteur déporté du chauffage désactivé
> [📄 Voir le YAML](../../automations/notification_du_capteur_deporte_du_chauffage_desactive.yaml)

**Statut :** Finalisé

**Evolution :** Aucune

**Déclencheurs :**

- L'un des 5 capteurs de sonde de température des chauffages de l'étage passe
à « Non Détecté » (off)

- Planification hebdomadaire tous les vendredis à 08h00

- Déclenchement manuel

**Fonctionnement :**

1. Quel que soit le déclencheur → vérifie les 5 capteurs et crée une
notification pour chacun actuellement à off. Le `message_id` évite les
doublons dans l'interface.

**Entités principales :**

- 5 `binary_sensor.*_temperature_sensor` : sondes des chauffages Bureau,
Chambre, Suite parentale, Salle d'eau, Salle de bain

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

**Statut :** En test | **Evolution :** Correction du 11/10/2026 — l'envoi dépendait d'un test sur la variable `message_courrier`, jamais définie ; l'envoi est désormais fait directement dans chaque branche.

**Convention des capteurs :** les deux contacts sont à `on` au repos (fermé) et passent brièvement à `off` à l'ouverture.

**Déclencheurs :**
- Ouverture de la porte principale de la boîte aux lettres (`binary_sensor.porte_boite_aux_lettres` → off) — id: Porte, cas colis
- Ouverture de la trappe à lettres (`binary_sensor.trappe_boite_aux_lettres` → off) — id: Trappe, cas lettre

**Fonctionnement :**
1. Porte principale ouverte → envoie mail + SMS 'La boîte aux lettres a été ouverte : colis'.
2. Trappe à lettres ouverte, uniquement si la porte principale est fermée (`on`) → envoie mail + SMS 'La trappe de la boîte aux lettres a été ouverte : lettre'. Si la porte est ouverte au même moment (relevé du courrier), rien n'est envoyé pour la trappe.
3. Pas de notification vocale.

**Entités principales :**
- `binary_sensor.porte_boite_aux_lettres` : porte principale (colis)
- `binary_sensor.trappe_boite_aux_lettres` : trappe à lettres
- `script.notification_mail` / `script.notification_sms` : envoi des alertes

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

**Statut :** Finalisé | **Evolution :** Correction du 11/10/2026 — la branche de l'onduleur réseau Ups notifiait 'Replace battery!' à chaque changement de son code d'état ; elle est désormais filtrée sur les flags anormaux, comme la branche Eaton_Usb.

**Déclencheurs :**
- Changement d'état de `sensor.ups_code_d_etat` (onduleur réseau Ups, code d'état NUT ups.status) — id: ups_reseau
- Changement d'état de `sensor.eaton_usb_code_d_etat` (onduleur Eaton_Usb, code d'état NUT ups.status) — id: ups_eaton_usb

**Conditions (par branche) :**
- Le code d'état doit contenir au moins un flag hors OL/OB/CHRG/DISCHRG, donc un flag anormal : RB, LB, BYPASS, OFF, OVER, TRIM, BOOST, FSD, CAL.
- Les états `unavailable` / `unknown` sont ignorés pour les deux onduleurs (l'indisponibilité d'Eaton_Usb est traitée par `Correction de l'Onduleur`).

**Fonctionnement :**
1. Onduleur Ups (réseau) → si un flag anormal est présent, traduit chaque code en description lisible (RB = remplacement de la batterie nécessaire, LB = batterie faible, etc.) et notifie.
2. Onduleur Eaton_Usb (USB) → même logique.
3. Les deux branches utilisent `script.notification_ha` avec un `message_id` distinct par onduleur (`ups_reseau_defaut`, `eaton_usb_defaut`) : une nouvelle alerte remplace la précédente au lieu de s'empiler.
4. Un simple passage sur batterie (OB DISCHRG) ne notifie pas : la coupure secteur est couverte par `Notification de coupure de courant EDF`.

**Entités principales :**
- `sensor.ups_code_d_etat` : code d'état NUT de l'onduleur réseau Ups
- `sensor.eaton_usb_code_d_etat` : code d'état NUT de l'onduleur Eaton_Usb
- `script.notification_ha` : envoi des notifications

---

## `automation.notification_d_ouverture_ou_fermeture_des_fenetres` — Notification d'Ouverture ou Fermeture des fenêtres
> [📄 Voir le YAML](../../automations/notification_d_ouverture_ou_fermeture_des_fenetres.yaml)

**Statut :** Finalisé | **Evolution :** Correction — les détecteurs `binary_sensor.do_*` (Somfy Protexial) ont un état principal (on/off) qui ne reflète pas fiablement l'ouverture réelle de la fenêtre (il peut rester bloqué sur "on" alors que l'attribut `Door open` bascule correctement entre `open`/`closed` en continu, cas observé sur `binary_sensor.do_suite_parental`). Toutes les vérifications d'ouverture/fermeture testent désormais l'attribut `Door open` plutôt que l'état principal du binary_sensor.

**Déclencheurs :**
- Changement des températures intérieures/extérieure, de la prévision Météo-France, des consignes volet (chaud/froid/pluie), du mode été/hiver, ou des indicateurs de pluie (prévision + pluviomètre)
- Changement de `input_select.domicile`

**Conditions :**
- `input_select.domicile` = "Présent"

**Fonctionnement :**
1. Calcule pour chaque pièce (Bureau, Suite parentale, Cellier, Rez de chaussée = Cuisine+Salon+Séjour) si une annonce de fermeture ou d'ouverture de fenêtre est justifiée : détection d'ouverture via l'attribut `Door open` (`open`/`closed`) des `binary_sensor.do_*`, comparaison intérieur/extérieur avec hystérésis à deux seuils et mémoire de la dernière annonce ; pour l'ouverture, ajoute une garde anti-pluie (prévision + pas de pluie actuelle) et vérifie que le volet correspondant n'est pas fermé.
2. Regroupe les pièces concernées en deux annonces vocales au maximum par déclenchement (une pour les fermetures, une pour les ouvertures), avec accord singulier/pluriel automatique (ex : "C'est le moment de fermer les fenêtres du Bureau, de la Suite parentale et du Rez de chaussée").
3. Anti-répétition : chaque sens (fermer/ouvrir) est bloqué par pièce si la même annonce a déjà été faite il y a moins de 15 minutes (horodatage par pièce et par sens dans des helpers `input_datetime` dédiés, mis à jour uniquement pour les pièces citées).
4. Choix assumé : l'annonce de fermeture est toujours prononcée, quel que soit `input_boolean.annonces_volets` (protection contre la chaleur ou le froid), alors que l'annonce d'ouverture n'est prononcée que si `input_boolean.annonces_volets` est à on. Dans les deux cas l'horodatage anti-répétition est mis à jour.

**Entités principales :**
- `input_boolean.annonces_volets` : autorise l'annonce d'ouverture
- `sensor.netatmo_*_temperature`, `sensor.detecteur_du_cellier_nodeid_29_temperature_air` : températures
- `binary_sensor.do_*` (attribut `Door open`) : détecteurs d'ouverture
- `input_number.volet_consigne_*` : seuils de déclenchement
- `input_datetime.annonce_fenetre_*` : anti-répétition par pièce/sens
- `script.notification_vocale` : annonce

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
