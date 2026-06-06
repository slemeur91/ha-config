# Énergie & Environnement (3)

[← Retour README](../../README.md)


---

## `automation.gestion_du_soleil` — Gestion du Soleil
> [📄 Voir le YAML](../../automations/gestion_du_soleil.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Lever et coucher du soleil
- Température extérieure franchit un seuil (< 7°C ou > 20°C)
- Changement de l'indice UV ou de la condition météo journalière

**Fonctionnement :**
1. Envoie un mail d'information au lever et au coucher du soleil.
2. Recalcule en parallèle le compteur soleil (3 critères : température > 20°C, UV > 4, condition = Ensoleillé).
3. Active `input_boolean.volets_soleil` si le compteur atteint au moins 2 critères, le désactive sinon.
4. Positionne `input_select.volets_mode` selon la température : Hiver si < 7°C, Été si > 23°C.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_soleil` | counter | Incrément 1 |
| `input_boolean.volets_soleil` | input_boolean | on/off |
| `input_select.volets_mode` | input_select | Été, Hiver |

---

## `automation.gestion_de_l_activation_de_l_arrosage` — Gestion de l'activation de l'Arrosage
> [📄 Voir le YAML](../../automations/gestion_de_l_activation_de_l_arrosage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_select.arrosage` passe à "Actif"
- `timer.arrosage_timer` se termine

**Fonctionnement :**
1. Timer terminé → ferme la vanne, remet le sélecteur à "Inactif", envoie un mail de confirmation.
2. Activation → vérifie la pluviométrie (Netatmo) : arrête si précipitations > 2 mm aujourd'hui ou en cours.
3. Sinon, ouvre la vanne, lance le timer, envoie un mail de déclenchement.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.arrosage` | input_select | Actif, Inactif |
| `timer.arrosage_timer` | timer | Durée configurée |

---

## `automation.gestion_de_la_qualite_de_l_air` — Gestion de la Qualité de l'Air
> [📄 Voir le YAML](../../automations/gestion_de_la_qualite_de_l_air.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Capteurs PM2.5 (moniteur Xiaomi, purificateur Mi Air, Dyson Salon), PM10, VOC, NO2
- Attribut PM2.5 du moniteur Xiaomi passe sous 0 (détection indisponibilité appareil)

**Fonctionnement :**
1. Seuils dépassés (PM2.5 > 40, PM10 > 60, VOC > 6 ou NO2 > 6) → allume les purificateurs (Mi Air + Dyson Salon) s'ils sont éteints, active le flag purification.
2. Tous les seuils en dessous des valeurs basses → éteint les purificateurs, coupe les switches physiques si alarme armée, désactive le flag.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.purification` | input_boolean | on/off |
