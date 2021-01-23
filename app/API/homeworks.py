import requests
import json

def get_homeworks(register_id, register_r, oun, s, date, school_year):
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

    headres = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'Wulkanowy-web :)'
    }

    homeworks = requests.post(oun+'/Homework.mvc/Get', headers=headres, cookies=cookies, json={'schoolYear': school_year, 'date': date, 'statusFilter': '-1'})

    return homeworks.json()