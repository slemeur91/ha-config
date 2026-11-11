# Surveillance HA (4)

[← Retour README](../../README.md)

---

## `automation.notification_des_automatisations_desactivees` — Notification des Automatisations désactivées
> [📄 Voir le YAML](../../automations/notification_des_automatisations_desactivees.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque jour à 8h00

**Conditions :** Au moins une automatisation désactivée

**Fonctionnement :**
1. Pour chaque automatisation désactivée, envoie une notification HA (`script.notification_ha`) avec un `message_id` stable par automatisation (mise à jour, pas de doublon si toujours désactivée le lendemain).

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_des_automatisations_et_scripts_en_defaut` — Notification des Automatisations et Scripts en Défaut
> [📄 Voir le YAML](../../automations/notification_des_automatisations_et_scripts_en_defaut.yaml)

**Statut :** Finalisé

**Prérequis (configuration.yaml) — 🚨 Événements de log — System Log :**
Nécessaire pour que cette automatisation puisse détecter les erreurs : par défaut, `fire_event` est à `false` et l'événement `system_log_event` n'est jamais émis sur le bus, donc aucun trigger basé sur cet événement ne se déclenche (testé et confirmé le 19/06/2026).

```yaml
system_log:
  fire_event: true
```

**Redémarrage requis** après ajout (composant non rechargeable à chaud).

**Déclencheurs :**
- Erreur d'exécution loggée par le composant `automation`
- Erreur d'exécution loggée par le composant `script`

**Fonctionnement :**
1. Détecte chaque erreur loggée (`system_log_event`, niveau `ERROR`) provenant des composants `automation` ou `script`.
2. Envoie une notification HA (`script.notification_ha`) avec le type (Automatisation/Script) et le message d'erreur, avec un `message_id` stable basé sur le contenu pour éviter les doublons en cas de répétition rapide de la même erreur.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.notification_des_automatisations_sans_declenchement_recent` — Notification des Automatisations sans déclenchement récent
> [📄 Voir le YAML](../../automations/notification_des_automatisations_sans_declenchement_recent.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Chaque jour à 9h00

**Conditions :**
- Au moins une automatisation jamais déclenchée, ou non déclenchée depuis 7 jours (hors exclusions)

**Fonctionnement :**
1. Pour chaque automatisation jamais déclenchée ou non déclenchée depuis 7 jours (en excluant `automation.alarme_declenchement`, `automation.alarme_sabotage`, `automation.gestion_de_la_telecommande_hifi`, `automation.notification_de_la_boite_aux_lettres`, `automation.gestion_de_la_charge_batterie_de_l_ipad`, `automation.suspension_des_notifications_en_mode_invites`, `automation.notification_des_alertes_de_defaut_des_onduleurs_ups`, `automation.notification_de_batterie_remplacee`, `automation.notification_du_portier`, `automation.notification_de_defaut_du_refrigerateur`, `automation.notification_de_coupure_de_courant_edf`, `automation.notification_de_capteur_deporte_du_chauffage_desactive`, `automation.gestion_de_l_activation_de_l_imprimante_canon_mf650c`, `automation.gestion_de_la_lumiere_de_l_entree`, `automation.notification_des_automatisations_desactivees`, `automation.gestion_du_cycle_du_lave_linge`, `automation.gestion_du_cycle_du_seche_linge`, `automation.gestion_du_cycle_du_lave_vaisselle`, `automation.correction_du_mi_air_purifier`, `automation.maj_auto_prises_ll_sl_zigbee2mqtt`, `automation.notification_de_slm_camera5` et `automation.notification_de_slm_camera6` — déclenchements normalement irréguliers ou liés à des événements peu fréquents, peuvent rester longtemps sans déclenchement sans que ce soit anormal), appelle `script.notification_ha` avec un `message_id` stable par automatisation (mise à jour, pas de doublon si toujours sans déclenchement le lendemain) et la date du dernier déclenchement (ou mention "jamais déclenchée") dans le message.

**Entités principales :**
- `automation.*` : ensemble des automatisations surveillées (attribut last_triggered)
- `script.notification_ha` : création des notifications

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.rechargement_des_integrations_en_defaut` — Rechargement des intégrations en défaut
> [📄 Voir le YAML](../../automations/rechargement_des_integrations_en_defaut.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- 12 minutes après le démarrage de Home Assistant
- Détection d'un nouveau problème dans Repairs (`event.repair`, event_type = create)
- Vérification périodique toutes les 15 minutes

**Fonctionnement :**
1. Recherche les entrées de configuration via les entités existantes (`config_entry_id`).
2. Détecte deux types de panne :
   - Erreur officielle : état setup_error, setup_retry, failed_unload ou migration_error.
   - Panne silencieuse : intégration déclarée "loaded" mais dont 100% des entités sont "unavailable" depuis plus de 10 minutes (ex : Netatmo dont toutes les sondes tombent indisponibles sans que l'intégration ne passe en erreur). Les intégrations média/TV (dlna_dmr, cast, braviatv, apple_tv, androidtv, samsungtv, roku, webostv, kodi, lg_netcast, philips_js, firetv) sont exclues car elles s'éteignent normalement. Certaines entrées sont aussi exclues individuellement via `exclusions_entries` (ex : template GAZPAR Cheptainville Énergie, dont la source Gazpar2MQTT n'est rafraîchie que toutes les 8 h).
3. Recharge chaque entrée en erreur ou en panne silencieuse via `homeassistant.reload_config_entry`.
4. Envoie une notification HA (`script.notification_ha`) pour chaque panne silencieuse détectée, avec un `message_id` stable par intégration (pas de doublon si le problème persiste).

**Entités principales :**
- `event.repair` : déclencheur sur détection d'un problème Repairs
- Liste des intégrations en erreur/panne calculée dynamiquement (aucune entité fixe ciblée)
- `script.notification_ha` : notification des pannes silencieuses

**Entrées utilisées :** Aucune entrée helper.
