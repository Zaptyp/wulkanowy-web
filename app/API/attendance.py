import requests
import json

def get_attendance(register_id, students, oun, s, date):
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

    attendance_lessons = requests.post(oun+'/FrekwencjaStatystykiPrzedmioty.mvc/Get', headers=headers, cookies=cookies)
    attendance_json_id = attendance_lessons.json()['data'][0]['Id']
    attendance = requests.post(oun+'/Frekwencja.mvc/Get', headers=headers, cookies=cookies, json={'idTypWpisuFrekwencji': attendance_json_id, 'data': date})

    return [attendance.json(), attendance_lessons.json()]