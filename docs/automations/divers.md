# Divers

[← Retour README](../../README.md)


---

## `automation.gazpar_mise_a_jour_statistiques_journalieres` — GAZPAR – Mise à jour statistiques journalières
> [📄 Voir le YAML](../../automations/gazpar_mise_a_jour_statistiques_journalieres.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Changement de `sensor.gazpar_cheptainville_card` (nouvelles données via Gazpar2MQTT)

**Conditions :** Sensor non indisponible / inconnu

**Fonctionnement :**
1. Lance `pyscript.gazpar_update` pour injecter les données de consommation gaz dans les statistiques long-terme de HA.

**Entrées utilisées :** Aucune entrée helper.
