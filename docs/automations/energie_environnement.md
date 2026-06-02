# Énergie & Environnement

[← Retour README](../../README.md)

---

## `automation.gestion_du_soleil` — Gestion du Soleil

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Lever et coucher du soleil
- Température extérieure franchit un seuil (< 7°C ou > 20°C)
- Changement de l'indice UV ou de la condition météo journalière

**Fonctionnement :**
1. Envoie un mail au lever et au coucher du soleil.
2. Recalcule le compteur soleil (3 critères : température > 20°C, UV > 4, condition = Ensoleillé).
3. Active `input_boolean.volets_soleil` si ≥ 2 critères.
4. Positionne `input_select.volets_mode` (Hiver < 7°C, Été > 23°C).

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_soleil` | counter | Incrément 1 |
| `input_boolean.volets_soleil` | input_boolean | on/off |
| `input_select.volets_mode` | input_select | Été, Hiver |

---

## `automation.gestion_de_la_qualite_de_l_air` — Gestion de la Qualité de l'Air

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Capteurs PM2.5 (3 appareils), PM10, VOC, NO2

**Fonctionnement :**
1. Seuils dépassés (PM2.5 > 40, PM10 > 60, VOC > 6, NO2 > 6) → allume purificateurs.
2. Tous sous les seuils bas → éteint purificateurs, coupe switches si alarme armée.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.purification` | input_boolean | on/off |

---

## `automation.gestion_de_l_activation_de_l_arrosage` — Gestion de l'Arrosage

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `input_select.arrosage` → "Actif"
- `timer.arrosage_timer` terminé

**Fonctionnement :**
1. Timer terminé → ferme vanne, remet à "Inactif", mail.
2. Activation → vérifie pluviométrie, ouvre vanne, lance timer, mail.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_select.arrosage` | input_select | Actif, Inactif |
| `timer.arrosage_timer` | timer | Durée configurée |

---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR Statistiques

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.gazpar_cheptainville_card`

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données gaz dans les statistiques HA.

**Entrées utilisées :** Aucune entrée helper.
