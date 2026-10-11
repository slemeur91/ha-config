# Alarme (3)

[← Retour README](../../README.md)

---

## `automation.alarme_declenchement` — Alarme Déclenchement
> [📄 Voir le YAML](../../automations/alarme_declenchement.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Alarme déclenchée (`alarm_control_panel.alarme` → triggered)
- Ouverture détectée (`binary_sensor.porte_ou_fenetre` → on) ou mouvement détecté (`binary_sensor.mouvement_detecte` → on)
- Fin de `timer.alarme_declenchement`

**Condition :** l'alarme ne doit pas être désarmée (aucune action si elle l'est).

**Fonctionnement :**
1. Déclenchement initial → remet le compteur à zéro, envoie vocal + mail + SMS, démarre l'enregistrement des caméras 1/2/4, lance `script.notification_snapshot_des_cameras`, démarre le timer pour 1 minute.
2. Timer terminé et compteur ≤ 8 → incrémente le compteur, envoie de nouveaux snapshots, relance le timer pour 1 minute.
3. Timer terminé et compteur > 8, ou alarme revenue en armé → snapshot final, notifications de fin d'alerte, arrêt de l'enregistrement des caméras 1/2/4 si l'alarme est en mode nuit.

**Cycle de répétition (corrigé le 11/10/2026) :** le déclenchement initial démarre `timer.alarme_declenchement` pour 1 minute ; chaque fin de timer envoie un snapshot et relance le timer, soit un snapshot par minute pendant 10 minutes (11 mails au total, snapshot initial et final compris), puis les notifications de fin. Le cycle s'arrête plus tôt, dès la première fin de timer, si la centrale n'est plus à l'état déclenché (revenue à armé). Mode `restart` : un nouveau déclenchement pendant le cycle le reprend à zéro.

**Entités principales :**
- `counter.compteur_alarme` : comptage des cycles d'alerte (environ 10 min)
- `timer.alarme_declenchement` : rythme des notifications
- `script.notification_snapshot_des_cameras` : captures caméras
- `script.notification_vocale` / `script.notification_mail` / `script.notification_sms` : notifications

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_alarme` | counter | Max 10 cycles |
| `timer.alarme_declenchement` | timer | 1 minute |

---

## `automation.alarme_sabotage` — Alarme Sabotage
> [📄 Voir le YAML](../../automations/alarme_sabotage.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `binary_sensor.boitier` passe à ON (sabotage du boîtier d'alarme)
- Fin de `timer.alarme_sabotage`

**Condition :** l'alarme ne doit pas être désarmée (aucune action si elle l'est).

**Fonctionnement :**
1. Sabotage initial → remet le compteur à zéro, envoie vocal + mail + SMS, démarre l'enregistrement des caméras 1/2/4, lance `script.notification_snapshot_des_cameras`, démarre le timer pour 1 minute.
2. Timer terminé et compteur ≤ 8 → incrémente le compteur, envoie de nouveaux snapshots, relance le timer pour 1 minute.
3. Timer terminé et compteur > 8, ou alarme revenue en armé → snapshot final, notifications de fin, arrêt de l'enregistrement des caméras 1/2/4 si l'alarme est en mode nuit.

**Cycle de répétition (corrigé le 11/10/2026) :** le sabotage initial démarre `timer.alarme_sabotage` pour 1 minute ; chaque fin de timer envoie un snapshot et relance le timer, soit un snapshot par minute pendant 10 minutes (11 mails au total, snapshot initial et final compris), puis les notifications de fin. Le cycle s'arrête plus tôt, dès la première fin de timer, si la centrale est à l'état armé (et non déclenché). Mode `restart` : un nouveau sabotage pendant le cycle le reprend à zéro.

**Entités principales :**
- `counter.compteur_sabotage` : comptage des cycles (environ 10 min)
- `timer.alarme_sabotage` : rythme des notifications
- `script.notification_snapshot_des_cameras` : captures caméras
- `script.notification_vocale` / `script.notification_mail` / `script.notification_sms` : notifications

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `counter.compteur_sabotage` | counter | Max 10 cycles |
| `timer.alarme_sabotage` | timer | 1 minute |

---

## `automation.alarme` — Gestion de l'Alarme
> [📄 Voir le YAML](../../automations/gestion_de_l_alarme.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `alarm_control_panel.alarme` passe de désarmé à armé (absent ou nuit) — id: Activation
- `alarm_control_panel.alarme` passe d'armé à désarmé — id: Désactivation
- Appui sur `input_button.alarme_desactivee` — id: Désactivation
- Appui sur `input_button.alarme_activee` — id: BoutonActivation (traité comme une activation en mode absent)

**Fonctionnement :**
1. Activation (absent ou bouton), si le flag `input_boolean.alarme` est à off → met le domicile en Vacances si `input_select.calendrier` vaut Absent, sinon en Absent ; démarre l'enregistrement des caméras 1/2/4 (pyscript Surveillance Station + mode `always`) ; active le flag.
2. Activation (nuit) → met le domicile en Nuit, arrête l'enregistrement des caméras 1/2/4 (mode `never`), active le flag.
3. Désactivation, si le flag est à on → met le domicile en Présent, arrête l'enregistrement des caméras 1/2/4, désactive le flag.
4. Dans tous les cas → lance l'enregistrement permanent des caméras extérieures (pyscript : caméras 3/5/6/7/8/10 ; mode `always` sur les caméras 3/5/6/7 et le portier), puis met à jour `input_select.presence_action` selon l'état du domicile (Nuit → Couché ; Absent/Vacances → Extinction ; Présent → Réveil si on était Couché, Arrivée si on était en Extinction, sinon Présent).

**Entités principales :**
- `alarm_control_panel.alarme` : centrale d'alarme Somfy Protexial
- `input_boolean.alarme` / `input_select.domicile` : flags d'état
- `input_select.presence_action` : action de présence transmise aux autres automatisations
- `pyscript.surveillance_station_recording` et `select.slm_camera*_mode_enregistrement` : enregistrement des caméras

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.alarme` | input_boolean | on/off |
| `input_select.domicile` | input_select | Absent, Présent, Nuit, Vacances |
| `input_select.presence_action` | input_select | Présent, Couché, Réveil, Extinction, Arrivée |
| `input_select.calendrier` | input_select | Absent, TéléTravail, Travail, Repos |
| `input_button.alarme_activee` | input_button | — |
| `input_button.alarme_desactivee` | input_button | — |
| `input_button.volets_reactivation` | input_button | — |

---

