# ⚙️ Configuration principale — configuration.yaml

[← Retour README](../README.md)

---

## 📧 Notifications — SMTP (email)

Déclaré dans `configuration.yaml` sous la clé `notify`.

```yaml
notify:
  - name: "email"
    platform: smtp
    server: "votre-serveur.domaine.fr"
    port: 25
    timeout: 15
    user: "votre-utilisateur"
    password: "[MOT_DE_PASSE]"
    encryption: none
    sender_name: "Home Assistant"
    sender: "votre-email@domaine.fr"
    recipient: "votre-email@domaine.fr"
```

**Utilisation :** Le service `notify.email` est appelé par les scripts `notification_mail` et `notification_snapshot` pour envoyer des alertes, des récapitulatifs batteries, et des captures caméras.

**Serveur :** SMTP local auto-hébergé (NAS Synology), sans chiffrement (port 25, réseau interne).

---

## 🐛 Débogage — Logger

Configuration à activer temporairement dans `configuration.yaml` pour le diagnostic.

```yaml
logger:
  default: info
  logs:
    custom_components.somfy_protexial: debug
    custom_components.local_agenda: debug
#    components.husqvarna_automower_ble: debug
    homeassistant.components.apple_tv: debug
    pyatv: debug
```

---
