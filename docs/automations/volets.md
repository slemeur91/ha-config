# Volets (2)

[← Retour README](../../README.md)

> ℹ️ Le pilotage des volets, des velux et du store de la pergola est désormais assuré par l'intégration **[CoverAutomatic](../hacs.md)** (13 ouvrants, 10 façades). Les 12 automatisations par volet et velux, `Volets Ouvrir` et la suspension du volet de la Suite parentale ont été supprimées de Home Assistant. La catégorie contient l'automatisation qui sélectionne le scénario de l'intégration et la notification d'ouverture ou de fermeture des fenêtres.

---

## `automation.notification_d_ouverture_ou_fermeture_des_fenetres` — Notification d'Ouverture ou Fermeture des fenêtres
> [📄 Voir le YAML](../../automations/notification_d_ouverture_ou_fermeture_des_fenetres.yaml)

**Statut :** Finalisé | **Evolution :** Correction — les détecteurs `binary_sensor.do_*` (Somfy Protexial) ont un état principal (on/off) qui ne reflète pas fiablement l'ouverture réelle de la fenêtre (il peut rester bloqué sur "on" alors que l'attribut `Door open` bascule correctement entre `open`/`closed` en continu, cas observé sur `binary_sensor.do_suite_parental`). Toutes les vérifications d'ouverture/fermeture testent désormais l'attribut `Door open` plutôt que l'état principal du binary_sensor.

**Déclencheurs :**
- Changement des températures intérieures/extérieure, de la prévision Météo-France, des consignes CoverAutomatic (froide/chaude A et B), de la consigne de pluie, du mode été/hiver, ou des indicateurs de pluie (prévision + pluviomètre)
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
- `number.information_volets_auto_consigne_froide_a/b` et `..._chaude_a/b` (CoverAutomatic) : consignes, profil A en mode Eté, profil B sinon
- `input_number.volet_consigne_risque_de_pluie` : seuil de pluie
- `input_datetime.annonce_fenetre_*` : anti-répétition par pièce/sens
- `script.notification_vocale` : annonce

---

## `automation.scenario_coverautomatic` — Scénario coverAutomatic
> [📄 Voir le YAML](../../automations/scenario_coverautomatic.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `input_select.volets_mode` (Eté / Hiver)
- Changement de `input_select.domicile`

**Fonctionnement :**
Sélectionne le scénario de l'intégration Cover Automatic via `select.cuisine_volet_de_la_cuisine_auto_scenario`, par ordre de priorité :
1. Domicile = Vacances → scénario `vacation`.
2. Sinon, volets en mode Eté → scénario `summer`.
3. Sinon, volets en mode Hiver → scénario `winter`.

**Remarque :** seul le sélecteur de scénario du volet de la cuisine est piloté ici ; au retour de vacances, le scénario saisonnier est rétabli puisque le changement de `input_select.domicile` relance l'évaluation.

**Entités principales :**
- `input_select.volets_mode` : mode saisonnier des volets
- `input_select.domicile` : état du domicile
- `select.cuisine_volet_de_la_cuisine_auto_scenario` : scénario Cover Automatic
