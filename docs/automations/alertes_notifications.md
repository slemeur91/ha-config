# Alertes & Notifications

[← Retour README](../../README.md)


---

## `automation.gestion_des_alertes` — Notification des Alertes

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

## `automation.gestion_de_la_temperature_du_refrigerateur` — Température Réfrigérateur
> [📄 Voir le YAML](../../automations/gestion_de_la_temperature_du_refrigerateur.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de température frigo ou congélateur
- Déconnexion réseau de l'interface du réfrigérateur

**Fonctionnement :**
1. Si frigo hors [2-4°C] OU congélateur hors [-20 à -18°C] OU interface réseau absente → SMS d'alerte.

**Entrées utilisées :** Aucune entrée helper.
