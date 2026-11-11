# Notifications (9)

[← Retour README](../../README.md)

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

## `automation.notification_de_defaut_du_refrigerateur` — Notification de défaut du réfrigérateur
> [📄 Voir le YAML](../../automations/notification_de_defaut_du_refrigerateur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de la température du frigo ou du congélateur
- Déconnexion réseau de l'interface du réfrigérateur (device tracker passe de "home")

**Conditions :**
- Les capteurs de température et le device_tracker ne doivent pas être à unknown/unavailable

**Fonctionnement :**
1. Si la température du frigo est hors plage [2-4°C] OU le congélateur hors plage [-20 à -18°C] et que l'entrée Défaut température réfrigérateur est à off → l'entrée passe à on et un SMS d'alerte est envoyé.
2. Quand les deux températures reviennent dans la plage et que l'entrée est à on → l'entrée repasse à off et un SMS de retour à la normale est envoyé.
3. Si l'interface réseau du frigo n'est plus détectée → SMS d'alerte.

**Entités principales :**
- `sensor.refrigerateur_temperature_du_frigo` / `sensor.refrigerateur_temperature_du_congelateur` : températures
- `device_tracker.samsung_refrigerator` : supervision réseau du frigo
- `input_boolean.defaut_temperature_refrigerateur` : mémorisation du défaut de température

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
