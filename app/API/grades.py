import json
import requests

def get_grades(register_id, students, oun, s):
    cookies = s
    if oun != 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        cookies.update({
            "biezacyRokSzkolny": f"{students['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{students['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{students['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyDziennikWychowankowie": f"{students['data'][0]['IdWychowankowieDziennik']}",
            "idBiezacyUczen": f"{students['data'][0]['IdUczen']}"
        })
    else:
        cookies.update({
            "biezacyRokSzkolny": f"{students['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{students['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{students['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyUczen": f"{students['data'][0]['IdUczen']}"
        })

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    grades = requests.post(oun+'/Oceny.mvc/Get', headers=headers, cookies=cookies, json={'okres': register_id})
    
    return grades.json()