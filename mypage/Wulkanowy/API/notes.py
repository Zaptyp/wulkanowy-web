import json
import requests

def get_notes(register_id, register_r, oun, s):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    notes = s.post(oun+'/UwagiIOsiagniecia.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies)

    return notes.json()

def prepare_notes_for_display(register_id, register_r, oun, s):
    notes = get_notes(register_id, register_r, oun, s)

    list_notes = []
    list_achievements = []

    i = 0

    if notes['data']['Uwagi'] == []:
        list_notes.append({'content': 'Brak uwag!'})
    else:
        while True:
            list_notes.append({'content': notes['data']['Uwagi'][i]['TrescUwagi'],
            'category': notes['data']['Uwagi'][i]['Kategoria'],
            'date': notes['data']['Uwagi'][i]['DataWpisu'],
            'teacher': notes['data']['Uwagi'][i]['Nauczyciel'],
            'points': notes['data']['Uwagi'][i]['Punkty']})
            if notes['data']['Uwagi'][i] == notes['data']['Uwagi'][-1]:
                i = 0
                break
            i += 1
    
    if notes['data']['Osiagniecia'] == []:
        list_achievements.append({'content': 'Brak osiągnięć!'})
    else:
        while True:
            list_achievements.append({'content': notes['data']['Osiagniecia'][i]})
            if notes['data']['Osiagniecia'][i] == notes['data']['Osiagniecia'][-1]:
                i = 0
                break
            i += 1

    return list_notes, list_achievements
