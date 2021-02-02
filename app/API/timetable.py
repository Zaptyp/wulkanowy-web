import json
import requests
from bs4 import BeautifulSoup
from .generate_cookies import autogenerate_cookies

def get_timetable(register_id, students, oun, s, date):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    timetable = requests.post(oun+'/PlanZajec.mvc/Get', headers=headers, cookies=cookies, json={'data': date})

    return timetable.json()