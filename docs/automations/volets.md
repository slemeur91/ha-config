# Volets (1)

[← Retour README](../../README.md)

> ℹ️ Le pilotage des volets, des velux et du store de la pergola est désormais assuré par l'intégration **[CoverAutomatic](../hacs.md)** (13 ouvrants, 10 façades). Les 12 automatisations par volet et velux, `Volets Ouvrir` et la suspension du volet de la Suite parentale ont été supprimées de Home Assistant. Il ne reste qu'une automatisation, qui sélectionne le scénario de l'intégration.

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

