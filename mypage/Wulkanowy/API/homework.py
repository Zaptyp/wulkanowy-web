import requests
from django import template
import json
import datetime

def get_homework(register_id, register_r, oun, s, school_year):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    now = datetime.datetime.now()
    weekday = now.weekday()

    for x in range(7):
        if weekday == x:
            now1 = now - datetime.timedelta(days=x)
            now2 = now - datetime.timedelta(days=x) + datetime.timedelta(days=7)
            now3 = now - datetime.timedelta(days=x) + datetime.timedelta(days=14)
            now4 = now - datetime.timedelta(days=x) + datetime.timedelta(days=21)

    day1 = str(now1.day)
    month1 = str(now1.month)
    year1 = str(now1.year)
    date1 = year1+'-'+month1+'-'+day1

    day2 = str(now2.day)
    month2 = str(now2.month)
    year2 = str(now2.year)
    date2 = year2+'-'+month2+'-'+day2

    day3 = str(now3.day)
    month3 = str(now3.month)
    year3 = str(now3.year)
    date3 = year3+'-'+month3+'-'+day3

    day4 = str(now4.day)
    month4 = str(now4.month)
    year4 = str(now4.year)
    date4 = year4+'-'+month4+'-'+day4

    homework1 = s.post(oun+'/Homework.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'schoolYear': school_year, 'date': date1, 'statusFilter': '-1'}) #'2020-09-28'
    homework2 = s.post(oun+'/Homework.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'schoolYear': school_year, 'date': date2, 'statusFilter': '-1'})
    homework3 = s.post(oun+'/Homework.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'schoolYear': school_year, 'date': date3, 'statusFilter': '-1'})
    homework4 = s.post(oun+'/Homework.mvc/Get', headers={"User-Agent": "Wulkanowy-web :)"}, cookies=cookies, json={'schoolYear': school_year, 'date': date4, 'statusFilter': '-1'})

    return homework1.json(), homework2.json(), homework3.json(), homework4.json()

def prepare_homework_for_display(register_id, register_r, oun, s, school_year):
    homework = get_homework(register_id, register_r, oun, s, school_year)

    json_homework = {}
    i = 0
    a = 0
    x = 0

    for j in homework:
        json_homework.update({x: {}})
        for i in range(5):
            json_homework[x].update({i: []})
            if j['data'][i]['Homework'] != []:
                while True:
                    json_homework[x][i].append({'Przedmiot': j['data'][i]['Homework'][a]['Subject'],
                    'Nauczyciel': j['data'][i]['Homework'][a]['Teacher'],
                    'Opis': j['data'][i]['Homework'][a]['Description'],
                    'Data': j['data'][i]['Homework'][a]['Date']})
                    if j['data'][i]['Homework'][a] == j['data'][i]['Homework'][-1]:
                        a = 0
                        break
                    else:
                        a += 1
            else:
                json_homework[x][i].append('Brak zadań domowych na ten dzień')
        x += 1

    return json_homework