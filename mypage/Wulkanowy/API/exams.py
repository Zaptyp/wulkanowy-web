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

def get_exams(register_id, register_r, oun, s, date, school_year):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    exams = s.post(oun+'/Sprawdziany.mvc/Get', cookies=cookies, json={'data': date, 'rokSzkolny': school_year})

    exams_json = exams.json()

    with open('json/exams.json', 'w') as f:
        json.dump(exams_json, f)

def prepare_exams_for_display():
    with open('json/exams.json') as f:
        exams = json.loads(f.read())

    a = 0
    
    for i in range(4):
        print(f'------------TYDZIEŃ {i+1}------------')
        for x in range(5):
            print('------------------------------------------------')
            while True:
                if exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'] != []:
                    print('Przedmiot: '+exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['DisplayValue'])
                    print('Nauczyciel: '+exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['PracownikModyfikujacyDisplay'])
                    print('Opis: '+exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a]['Opis'])
                    print('Data: '+exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Data'])
                    if exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][a] == exams['data'][i]['SprawdzianyGroupedByDayList'][x]['Sprawdziany'][-1]:
                        a = 0
                        break
                    a += 1
                else:
                    break