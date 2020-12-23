import json
import requests

def get_exams(register_id, register_r, oun, s, date, school_year):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    exams = s.post(oun+'/Sprawdziany.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'data': date, 'rokSzkolny': school_year})

    return exams.json()

def prepare_exams_for_display(register_id, register_r, oun, s, date, school_year):
    exams = get_exams(register_id, register_r, oun, s, date, school_year)

    json_exams = {}

    a = 0
    
    for i in range(4):
        json_exams.update({i: {}})
        for x in range(5):
            json_exams[i].update({x: {}})
            while True:
                if exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'] != []:
                    json_exams[i][x].update({a: {}})
                    json_exams[i][x][a].update({'Przedmiot': exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['DisplayValue'],
                    'Nauczyciel': exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['PracownikModyfikujacyDisplay'],
                    'Opis': exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['Opis'],
                    'Data': exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Data']})
                    if exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a] == exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][-1]:
                        a = 0
                        break
                    a += 1
                else:
                    break

    return json_exams