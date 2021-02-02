import json
import requests

def get_registered_devices(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    registered = requests.post(oun+'/ZarejestrowaneUrzadzenia.mvc/Get', headers=headers, cookies=cookies)

    return registered.json()

def register_device(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    register_data = requests.post(oun+'/RejestracjaUrzadzeniaToken.mvc/Get', headers=headers, cookies=cookies)

    return register_data.json()