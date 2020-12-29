import requests
import json

def get_attendance(register_id, register_r, oun, s, date):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    attendance_lessons = s.post(oun+'/FrekwencjaStatystykiPrzedmioty.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies)
    attendance_json_id = attendance_lessons.json()['data'][0]['Id']
    attendance = s.post(oun+'/Frekwencja.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'idTypWpisuFrekwencji': attendance_json_id, 'data': date})

    return [attendance.json(), attendance_lessons.json()]


def prepare_attendance_for_display(register_id, register_r, oun, s, date):
    json = get_attendance(register_id, register_r, oun, s, date)
    attendance = json[0]
    #attendance_lessons = json[1]
    i = 0
    a = 0

    json_attendance = {0: []}

    print(attendance)

    if attendance['data']['Frekwencje'] != []:
        while True:
            json_attendance[a].append({'Content': attendance['data']['Frekwencje'][i]['Symbol'],
            'Lesson': attendance['data']['Frekwencje'][i]['PrzedmiotNazwa']})
            if attendance['data']['Frekwencje'][i] == attendance['data']['Frekwencje'][-1]:
                i = 0
                break
            if attendance['data']['Frekwencje'][i]['NrDnia'] != attendance['data']['Frekwencje'][i+1]['NrDnia']:
                a += 1
                json_attendance.update({a: []})
            i += 1
    else:
        json_attendance[a].append({'Content': 'Brak danych o frekwencji', 'Lesson': ''})

    return json_attendance