import json
import requests
from .generate_cookies import autogenerate_cookies

def get_exams(register_id, students, oun, s, date, school_year):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    exams = requests.post(oun+'/Sprawdziany.mvc/Get', headers=headers, cookies=cookies, json={'data': date, 'rokSzkolny': school_year})

    return exams.json()