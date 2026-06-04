import requests


# Parametres
# actionRecord : start / stop recording
# CamerasnUM
# ID 1 => Camera 1
# ID 2 => Camera 2
# ID 3 => Camera 3
# ID 4 => Camera 4
# ID 5 => Camera 5
# ID 6 => Portier
# ID 7 => Camera 6
# ID 8 => Camera 7

# Paramètres de configuration
serveur_surveillance_station = "http://votre-synology-ip:5000"  # Remplacez par votre serveur
log_surveillance_station = "votre-utilisateur"  # Remplacez par votre log
mdp_surveillance_station = "[MOT_DE_PASSE]"  # Mot de passe pour l'API

# API VERSIONS
# SYNO.API.Auth
vAPIAuth = 6
# SYNO.SurveillanceStation.Camera
vAPICamera = 9
# SYNO.SurveillanceStation.ExternalRecording
vAPIExternalRecording = 2


@service
def surveillance_station_recording(actionRecord='stop', camerasNum={}):
    api = f"{serveur_surveillance_station}/webapi/auth.cgi?api=SYNO.API.Auth"
    payload = { 'method': 'login',
                'version': vAPIAuth,
                'account': log_surveillance_station,
                'passwd': mdp_surveillance_station,
                'session': 'SurveillanceStation',
                'format': 'sid'}
    login_json = task.executor(requests.get, api, params=payload, verify=False).json()

    if not login_json['success']:
        log.info("[surveillance_station] Login error")
    else:
        log.info("[surveillance_station] Login success")
    
    sid = login_json['data']['sid']
    if sid:
        api = f"{serveur_surveillance_station}/webapi/entry.cgi?api=SYNO.SurveillanceStation.Camera"
        payload = { 'version': vAPICamera,
                    'method': 'List',
                    'privCamType': 1,
                    'camStm': 0,
                    '_sid': sid}
        listcam_json = task.executor(requests.get, api, params=payload).json()
    
        cameras = listcam_json['data']['cameras']
    
        api = f"{serveur_surveillance_station}/webapi/entry.cgi?api=SYNO.SurveillanceStation.ExternalRecording"
        for camera in cameras:  # Traiter chaque camera
            id_cam = camera['id']

            for IDCam in camerasNum:
                if IDCam == id_cam:
                    log.info("[surveillance_station] Camera a traiter")

                    payload = { 'version': vAPIExternalRecording,
                                'method': 'Record',
                                'cameraId': id_cam,
                                'action': actionRecord,
                                '_sid': sid}
                    set_record_json = task.executor(requests.get, api, params=payload).json()
        
                    if set_record_json['success']:
                        log.info("[surveillance_station] Camera correctement positionnée")
                    else:
                        log.info("[surveillance_station] Camera non positionnée")
            
        api = f"{serveur_surveillance_station}/webapi/auth.cgi?api=SYNO.API.Auth"
        payload = { 'version': vAPIAuth,
                    'method': 'logout',
                    'session': 'SurveillanceStation',
                    '_sid': sid}
        logout_json = task.executor(requests.get, api, params=payload).json()
        log.info("[surveillance_station] Logout")
