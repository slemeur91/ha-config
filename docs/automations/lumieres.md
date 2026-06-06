# Lumières (5)

[← Retour README](../../README.md)


---

## `automation.gestion_du_bouton_hue_central_droit` — Bouton Hue Central Droit
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_central_droit.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Appuis sur les 4 boutons du Tap Dial Central Droit

**Fonctionnement :**
- Bouton 1 appui long → HiFi SOURCE (BluRay)
- Bouton 2 appui long → SONOS ON
- Bouton 3 appui long → HiFi OFF
- Bouton 4 appui long → SONOS OFF
- Appuis courts → réservés (non affectés)

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.hifi_action` | input_select | ON, SOURCE, OFF |
| `input_select.hifi_source` | input_select | Zappiti, BluRay, slm-media4 |
| `input_select.sonos_action` | input_select | ON, COUCHE, REVEIL, OFF |

---

## `automation.gestion_du_bouton_hue_central_gauche` — Bouton Hue Central Gauche
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_central_gauche.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Appuis sur les 4 boutons du Tap Dial Central Gauche

**Fonctionnement :** Identique au Bouton Central Droit.

**Entrées utilisées :** Idem Bouton Central Droit.

---

## `automation.gestion_du_bouton_hue_de_l_entree` — Bouton Hue de l'Entrée
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_de_l_entree.yaml)

**Statut :** Finalisé | **Evolution :** En cours d'affectation

**Déclencheurs :** Appuis sur les 4 boutons du Tap Dial côté Entrée

**Fonctionnement :** Détection des appuis, aucune action affectée pour le moment.

**Entrées utilisées :** Aucune.

---

## `automation.gestion_du_bouton_hue_de_l_etage` — Bouton Hue de l'Étage
> [📄 Voir le YAML](../../automations/gestion_du_bouton_hue_de_l_etage.yaml)

**Statut :** Finalisé | **Evolution :** En cours d'affectation

**Déclencheurs :** Appuis sur les 4 boutons du Tap Dial de l'Étage

**Fonctionnement :** Détection des appuis, aucune action affectée pour le moment.

**Entrées utilisées :** Aucune.

---

## `automation.gestion_de_la_lumiere_du_garage` — Lumière du Garage
> [📄 Voir le YAML](../../automations/gestion_de_la_lumiere_du_garage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :** Ouverture de la porte du garage

**Fonctionnement :**
1. Si période sombre (entre coucher et lever du soleil) ET alarme désarmée → allume `light.lumiere_du_garage`.

**Entrées utilisées :** Aucune entrée helper.
