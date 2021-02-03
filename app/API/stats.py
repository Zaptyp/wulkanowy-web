import json
import requests
from .generate_cookies import autogenerate_cookies

def get_partial(register_id, students, oun, s):

    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    partial = requests.post(oun+'/Statystyki.mvc/GetOcenyCzastkowe', headers=headers, cookies=cookies, json={'idOkres': register_id})
    
    return partial.json()

def get_year(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    year = requests.post(oun+'/Statystyki.mvc/GetOcenyRoczne', headers=headers, cookies=cookies, json={'idOkres': register_id})
    
    return year.json()