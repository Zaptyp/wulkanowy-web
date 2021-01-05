import json
import requests

def get_grades(register_id, register_r, oun, s):
    if oun != 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        cookies = {
            "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
            "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
        }
    else:
        cookies = {
            "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
            "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
            "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
            "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
        }

    grades = s.post(oun+'/Oceny.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'okres': register_id})
    
    return grades.json()

def prepare_grades_for_display(register_id, register_r, oun, s):
    grades = get_grades(register_id, register_r, oun, s)

    i = 0
    a = 0

    json_grades = {}

    lesson_name = []

    while True:
        lesson_name.append(grades['data']['Oceny'][i]['Przedmiot'])
        json_grades.update({grades['data']['Oceny'][i]['Przedmiot']: []})
        if grades['data']['Oceny'][i]['OcenyCzastkowe'] != []:
            while True:
                json_grades[lesson_name[i]].append({'Ocena': grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Wpis'],
                'Nauczyciel': grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Nauczyciel'],
                'Opis': grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['NazwaKolumny'],
                'Data': grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['DataOceny'],
                'Waga Oceny': grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Waga']})
                if grades['data']['Oceny'][i]['OcenyCzastkowe'][a] == grades['data']['Oceny'][i]['OcenyCzastkowe'][-1]:
                    a = 0
                    break
                a += 1
        if grades['data']['Oceny'][i]['Pozycja'] == grades['data']['Oceny'][-1]['Pozycja']:
            break
        i += 1

    return [json_grades, lesson_name]