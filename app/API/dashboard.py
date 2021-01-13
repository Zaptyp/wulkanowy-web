import json
import requests
import re
from bs4 import BeautifulSoup

def get_dashboard(register_id, register_r, s, diary_url, symbol):
    cookies = s
    if diary_url != 'http://cufs.fakelog.cf/':
        cookies.update({
            "biezacyRokSzkolny": f"{register_r['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyDziennikWychowankowie": f"{register_r['data'][0]['IdWychowankowieDziennik']}",
            "idBiezacyUczen": f"{register_r['data'][0]['IdUczen']}"
        })
        diary_url = 'http://uonetplus.vulcan.net.pl/'
    else:
        cookies.update({
            "biezacyRokSzkolny": f"{register_r['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyUczen": f"{register_r['data'][0]['IdUczen']}"
        })
        diary_url = 'http://uonetplus.fakelog.cf/'

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    index = requests.get(f'{diary_url}{symbol}/Start.mvc/Index', headers=headers, cookies=cookies)
    permissionsValue = re.search("permissions: '(.)*'", index.text)
    permissionsValue = permissionsValue.group()
    print(permissionsValue)

    return {"dupa": "dupa"}