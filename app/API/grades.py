import json
import requests
from .generate_cookies import autogenerate_cookies

def get_grades(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    grades = requests.post(oun+'/Oceny.mvc/Get', headers=headers, cookies=cookies, json={'okres': register_id})
    print(grades.text)
    
    return grades.json()