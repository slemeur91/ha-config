# Machines (3)

[← Retour README](../../README.md)

---

## `automation.gestion_du_cycle_du_lave_linge` — Gestion du Cycle du Lave Linge
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_lave_linge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_lave_linge` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_lave_linge` passe de En marche à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.multiprise_de_la_salle_de_bain_power_1` repasse sous 5 W pendant 5 min (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_lave_linge_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_lave_linge` : état de l'appareil
- `sensor.multiprise_de_la_salle_de_bain_power_1` / `_energy_1` : puissance / énergie
- `input_boolean.cycle_lave_linge_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_lave_linge_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_lave_linge_conso_au_debut` / `_a_la_fin` : index d'énergie au début/fin du dernier cycle

---

## `automation.gestion_du_cycle_du_lave_vaisselle` — Gestion du Cycle du Lave Vaisselle
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_lave_vaisselle.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_lave_vaisselle` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_lave_vaisselle` passe de En marche à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.prise_du_lave_vaisselle_power` repasse sous 3 W pendant 5 min (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_lave_vaisselle_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_lave_vaisselle` : état de l'appareil
- `sensor.prise_du_lave_vaisselle_power` / `_energy` : puissance / énergie
- `input_boolean.cycle_lave_vaisselle_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_lave_vaisselle_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_lave_vaisselle_conso_au_debut` / `_a_la_fin` : index d'énergie au début/fin du dernier cycle

---

## `automation.gestion_du_cycle_du_seche_linge` — Gestion du Cycle du Sèche Linge
> [📄 Voir le YAML](../../automations/gestion_du_cycle_du_seche_linge.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.etat_seche_linge` passe de Éteint/Veille à En marche (anti-rebond 20s) → début de cycle
- `sensor.etat_seche_linge` passe de En marche ou Anti-froissage à Éteint/Veille (anti-rebond 20s) → fin de cycle
- `sensor.multiprise_de_la_salle_de_bain_power_2` repasse sous 3 W pendant 30s (désactivé) → détection alternative de fin de cycle par consommation
- `input_boolean.cycle_seche_linge_en_cours` resté à "on" 4h → filet de sécurité (cycle trop long / fin non détectée)

**Fonctionnement :**
1. Début : si le cycle n'est pas déjà marqué en cours, l'active, enregistre l'index d'énergie de départ et l'horodatage de début.
2. Fin : si le cycle est marqué en cours, enregistre l'horodatage et l'index d'énergie de fin, puis désactive le marqueur "en cours".
3. Trop Long : désactive le marqueur "en cours" sans enregistrer de fin (filet de sécurité si la fin n'a pas été détectée dans les 4h).

**Entités principales :**
- `sensor.etat_seche_linge` : état de l'appareil
- `sensor.multiprise_de_la_salle_de_bain_power_2` / `_energy_2` : puissance / énergie
- `input_boolean.cycle_seche_linge_en_cours` : marqueur de cycle en cours
- `input_datetime.dernier_cycle_seche_linge_debut` / `_fin` : horodatages du dernier cycle
- `input_number.dernier_cycle_seche_linge_conso_au_debut` / `_a_la_fin` : index d'énergie au début/fin du dernier cycle
