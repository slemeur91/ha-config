# Maintenance & Corrections

[← Retour README](../../README.md)


---

## `automation.corrections_du_klf200_pour_les_velux` — Corrections KLF200
> [📄 Voir le YAML](../../automations/corrections_du_klf200_pour_les_velux.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage HA (id: ha_start)
- Ping KLF200 perdu (id: ping_lost)
- Switch KLF200 éteint 5 min (id: switch_off)

**Fonctionnement :**
1. Démarrage HA → attente 60 s.
2. Autre déclencheur → attente 5 s.
3. Switch ON + KLF mort → éteint le switch (début cycle redémarrage).
4. Switch OFF depuis 5 min → rallume + recharge intégration.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.maintien_des_prises_et_appareils_allumes` — Maintien des Prises et Appareils allumés
> [📄 Voir le YAML](../../automations/maintien_des_prises_et_appareils_allumes.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Switches critiques éteints 30 s (réfrigérateur, multimédia, informatique, cellier, routeur, ventilateur, ZappitiNAS)
- Changement d'état purificateur ou ventilateur
- Changement device tracker ZappitiNAS

**Fonctionnement :**
1. Après 5 s, vérifie et rallume tout switch critique éteint.
2. ZappitiNAS absent 2 min → Wake-on-LAN.
3. Active/désactive intégrations purificateur et ventilateur selon leur switch physique.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.corrections_des_appareils_ecoflow` — Corrections EcoFlow
> [📄 Voir le YAML](../../automations/corrections_des_appareils_ecoflow.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.powerstream_6231_status` ou `sensor.ecoflow_status` → "assume_offline"
- Lever du soleil

**Fonctionnement :**
1. Attend 5 s.
2. PowerStream offline + soleil levé → cycle désactivation/réactivation (15 s).
3. EcoFlow offline → même cycle.

**Entrées utilisées :** Aucune entrée helper.

---

## `automation.gestion_du_poele_et_de_la_climatisation` — Poêle & Climatisation
> [📄 Voir le YAML](../../automations/gestion_du_poele_et_de_la_climatisation.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- `sensor.poele_status` (avec ou sans délai 30 min)
- `sensor.poele_smoke_temperature` < 78°C
- Changement climatisations (délai 5 min)
- Changement `input_boolean.alarme`

**Fonctionnement :**
1. Gère flag `input_boolean.poele` (allumage/stand-by/extinction).
2. Gère flag `input_boolean.climatisation`.
3. Alarme armée-absent → éteint toutes les climatisations.
4. Alarme désarmée → rallume contacteur climatisation.
5. Tout éteint + absent → coupe contacteur.

**Entrées utilisées :**

| Entrée | Type | Config |
|---|---|---|
| `input_boolean.poele` | input_boolean | on/off |
| `input_boolean.climatisation` | input_boolean | on/off |
| `input_boolean.alarme` | input_boolean | on/off |

---

## `automation.correction_tuya` — Correction Tuya
> [📄 Voir le YAML](../../automations/correction_tuya.yaml)

**Statut :** Finalisé | **Evolution :** Aucune

**Déclencheurs :**
- Démarrage HA

**Fonctionnement :**
1. Attend 5 minutes (initialisation Tuya).
2. Force l'activation du switch USB de la multiprise garage.

**Entrées utilisées :** Aucune entrée helper.
