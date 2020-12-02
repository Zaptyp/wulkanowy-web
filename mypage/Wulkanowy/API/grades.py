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

def get_grades(register_id, register_r, oun, s):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    grades = s.post(oun+'/Oceny.mvc/Get', cookies=cookies, json={'okres': register_id})

    grades_json = grades.json()

    with open('json/grades.json', 'w') as f:
        json.dump(grades_json, f)

def prepare_grades_for_display():
    with open('json/grades.json') as f:
        grades = json.loads(f.read())

    i = 0
    a = 0

    lesson_name = []

    while True:
        #lessons = grades.json()['data']['Oceny'][i]['Pozycja']
        lesson_name.append(grades['data']['Oceny'][i]['Przedmiot'])
        print('------------------------------------------------')
        print(lesson_name[i])
        print('------------------------------------------------')
        if grades['data']['Oceny'][i]['OcenyCzastkowe'] != []:
            while True:
                print('<----------------------------------------------------------->')
                print('Ocena: '+grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Wpis'])
                print('Nauczyciel: '+grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Nauczyciel'])
                print('Opis: '+grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['NazwaKolumny'])
                print('Data: '+grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['DataOceny'])
                print('Waga Oceny: '+str(grades['data']['Oceny'][i]['OcenyCzastkowe'][a]['Waga']))
                if grades['data']['Oceny'][i]['OcenyCzastkowe'][a] == grades['data']['Oceny'][i]['OcenyCzastkowe'][-1]:
                    a = 0
                    break
                a += 1
        else:
            print('Brak Ocen!')
        if grades['data']['Oceny'][i]['Pozycja'] == grades['data']['Oceny'][-1]['Pozycja']:
            break
        i += 1