import json
import requests
import re
from bs4 import BeautifulSoup
from .generate_cookies import autogenerate_cookies

def get_dashboard(register_id, students, s, diary_url, symbol):
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    index = requests.get(f'{diary_url}{symbol}/Start.mvc/Index', headers=headers, cookies=cookies)
    permissions_value = re.search("permissions: '(.)*'", index.text)
    permissions_value = permissions_value.group()
    permissions_value = permissions_value.replace('permissions: ', '').replace("'", "")

    json = {
        "permissions": permissions_value
    }

    last_notes = requests.post(f'{diary_url}{symbol}/Start.mvc/GetLastNotes', headers=headers, cookies=cookies, json=json)
    free_days = requests.post(f'{diary_url}{symbol}/Start.mvc/GetFreeDays', headers=headers, cookies=cookies, json=json)
    lucky_number = requests.post(f'{diary_url}{symbol}/Start.mvc/GetKidsLuckyNumbers', headers=headers, cookies=cookies, json=json)
    
    return_data = {
        "last_notes": last_notes.json(),
        "free_days": free_days.json(),
        "lucky_number": lucky_number.json()
    }

    return return_data