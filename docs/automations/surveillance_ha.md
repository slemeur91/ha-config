# Surveillance HA (4)

[← Retour README](../../README.md)


---

## `automation.surveillance_automatisations_desactivees` — Surveillance - Automatisations désactivées
> [📄 Voir le YAML](../../automations/surveillance_automatisations_desactivees.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque jour à 8h00

**Conditions :** Au moins une automatisation désactivée

**Fonctionnement :**
1. Pour chaque automatisation désactivée, envoie une notification HA (`script.notification_ha`) avec un `notification_id` stable par automatisation (mise à jour, pas de doublon si toujours désactivée le lendemain).

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.surveillance_automatisations_et_scripts_en_defaut` — Surveillance - Automatisations et Scripts en Défaut
> [📄 Voir le YAML](../../automations/surveillance_automatisations_et_scripts_en_defaut.yaml)

**Statut :** Finalisé

**Déclencheurs :**
- Erreur d'exécution loggée par le composant `automation`
- Erreur d'exécution loggée par le composant `script`

**Fonctionnement :**
1. Détecte chaque erreur loggée (`system_log_event`, niveau `ERROR`) provenant des composants `automation` ou `script`.
2. Envoie une notification HA (`script.notification_ha`) avec le type (Automatisation/Script) et le message d'erreur, avec un `notification_id` stable basé sur le contenu pour éviter les doublons en cas de répétition rapide de la même erreur.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.surveillance_automatisations_sans_declenchement_recent` — Surveillance - Automatisations sans déclenchement récent
> [📄 Voir le YAML](../../automations/surveillance_automatisations_sans_declenchement_recent.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque jour à 9h00

**Conditions :** Au moins une automatisation jamais déclenchée, ou non déclenchée depuis 7 jours (hors `automation.alarme_declenchement`, `automation.alarme_sabotage` et `automation.gestion_de_la_telecommande_hifi` — déclenchée uniquement par appui sur la télécommande HiFi, peut rester longtemps sans déclenchement sans que ce soit anormal)

**Fonctionnement :**
1. Pour chaque automatisation jamais déclenchée ou inactive depuis 7 jours (hors exclusions alarme), envoie une notification HA (`script.notification_ha`) avec un `notification_id` stable par automatisation et la date du dernier déclenchement (ou "jamais déclenchée") dans le message.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.surveillance_recharger_les_integrations_en_defaut` — Surveillance - Recharger les intégrations en défaut
> [📄 Voir le YAML](../../automations/surveillance_recharger_les_integrations_en_defaut.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- 5 minutes après le démarrage de Home Assistant
- Détection d'un nouveau problème dans Repairs (`event.repair`, event_type = create)
- Vérification périodique toutes les 15 minutes

**Fonctionnement :**
1. Recherche les entrées de configuration via les entités existantes (`config_entry_id`).
2. Détecte deux types de panne : erreur officielle (état `setup_error`, `setup_retry`, `failed_unload` ou `migration_error`) ou panne silencieuse (intégration déclarée « loaded » mais dont 100% des entités sont « unavailable » depuis plus de 10 minutes — ex : Netatmo dont toutes les sondes tombent indisponibles sans que l'intégration ne passe en erreur). Les intégrations média/TV (dlna_dmr, cast, braviatv, apple_tv, androidtv, samsungtv, roku, webostv, kodi, lg_netcast, philips_js, firetv) sont exclues car elles s'éteignent normalement.
3. Recharge chaque entrée en erreur ou en panne silencieuse via `homeassistant.reload_config_entry`.
4. Envoie une notification HA (`script.notification_ha`) pour chaque panne silencieuse détectée, avec un `notification_id` stable par intégration (pas de doublon si le problème persiste).

**Entrées utilisées :** Aucune entrée helper.
