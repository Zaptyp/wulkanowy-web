import requests
import json
from .generate_cookies import autogenerate_cookies

def get_homeworks(register_id, students, oun, s, date, school_year):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    homeworks = requests.post(oun+'/Homework.mvc/Get', headers=headres, cookies=cookies, json={'schoolYear': school_year, 'date': date, 'statusFilter': '-1'})

    return homeworks.json()