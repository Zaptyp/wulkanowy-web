import json
import requests
import re
from bs4 import BeautifulSoup
from .generate_cookies import autogenerate_cookies

def get_dashboard(register_id, students, s, diary_url, symbol):
    if diary_url != 'http://cufs.fakelog.cf/':
        diary_url = 'http://uonetplus.vulcan.net.pl/'
    else:
        diary_url = 'http://uonetplus.fakelog.cf/'
        
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    index = requests.get(f'{diary_url}{symbol}/Start.mvc/Index', headers=headers, cookies=cookies)
    permissions_value = re.search("permissions: '(.)*'", index.text)
    permissions_value = permissions_value.group()
    permissions_value = permissions_value.replace('permissions: ', '').replace("'", "")

    permissions = {
        "permissions": permissions_value
    }

    last_notes = requests.post(f'{diary_url}{symbol}/Start.mvc/GetLastNotes', headers=headers, cookies=cookies, json=permissions)
    free_days = requests.post(f'{diary_url}{symbol}/Start.mvc/GetFreeDays', headers=headers, cookies=cookies, json=permissions)
    lucky_number = requests.post(f'{diary_url}{symbol}/Start.mvc/GetKidsLuckyNumbers', headers=headers, cookies=cookies, json=permissions)
    
    return_data = {
        "last_notes": last_notes.json(),
        "free_days": free_days.json(),
        "lucky_number": lucky_number.json()
    }

    return return_data