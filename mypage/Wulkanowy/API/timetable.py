import os
import sys
import requests
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json
import requests
from django.shortcuts import redirect
from bs4 import BeautifulSoup

def get_timetable(register_id, register_r, oun, s, date):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    timetable = s.post(oun+'/PlanZajec.mvc/Get', cookies=cookies, json={'data': date})

    timetable_json = timetable.json()
    with open('json/timetable.json', 'w') as f:
        json.dump(timetable_json, f)


def prepare_timetable_for_display():
    with open('json/timetable.json') as f:
        timetable = json.load(f)
    
    hour = []
    monday = []
    tuesday = []
    wednesday = []
    thrusday = []
    friday = []

    a = 0
    x = 0
    i = 0

    while True:
        for x in range(6):
            if x == 0:
                hour.append(timetable['data']['Rows'][a][x])
            elif x == 1:
                monday.append(timetable['data']['Rows'][a][x])
            elif x == 2:
                tuesday.append(timetable['data']['Rows'][a][x])
            elif x == 3:
                wednesday.append(timetable['data']['Rows'][a][x])
            elif x == 4:
                thrusday.append(timetable['data']['Rows'][a][x])
            elif x == 5:
                friday.append(timetable['data']['Rows'][a][x])
        if timetable['data']['Rows'][a] == timetable['data']['Rows'][-1]:
            a = 0
            break
        a += 1

    while True:
        print(hour[i])
        print(monday[i])
        print(tuesday[i])
        print(wednesday[i])
        print(thrusday[i])
        print(friday[i])
        print('-------------------------------------')
        if hour[i] == hour[-1]:
            i = 0
            break
        i += 1