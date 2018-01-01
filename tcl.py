import base64
import requests
import html

API_BASE_URI = 'http://plan-interactif.tcl.fr/Proxy/ws.php'
STATION_IDS = {'Club': '32135', 'Maison': '32110'}

def _get_data(resource_name):
    session = requests.Session()

    if resource_name in STATION_IDS:
        resource_id = STATION_IDS[resource_name]
    else:
        return 'Error';

    payload = {
        'ws': 'horaire',
        'id': resource_id
    }

    req = session.post(API_BASE_URI, allow_redirects=False, data=payload)

    res = req.json()

    return res


r = _get_data('Club')
print(r)
