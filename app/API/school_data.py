import json
import requests
from .generate_cookies import autogenerate_cookies

def get_school_data(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    school_data = requests.post(oun+'/SzkolaINauczyciele.mvc/Get', headers=headers, cookies=cookies)

    return school_data.json()