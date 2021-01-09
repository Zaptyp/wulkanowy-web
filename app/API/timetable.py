import json
import requests
from bs4 import BeautifulSoup

def get_timetable(register_id, register_r, oun, s, date):
    cookies = s
    if oun != 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        cookies.update({
            "biezacyRokSzkolny": f"{register_r['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyDziennikWychowankowie": f"{register_r['data'][0]['IdWychowankowieDziennik']}",
            "idBiezacyUczen": f"{register_r['data'][0]['IdUczen']}"
        })
    else:
        cookies.update({
            "biezacyRokSzkolny": f"{register_r['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyUczen": f"{register_r['data'][0]['IdUczen']}"
        })

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    timetable = requests.post(oun+'/PlanZajec.mvc/Get', headers=headers, cookies=cookies, json={'data': date})

    return timetable.json()