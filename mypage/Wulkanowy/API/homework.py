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

def get_homework(register_id, register_r, oun, s, date, school_year):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    homework = s.post(oun+'/Homework.mvc/Get', cookies=cookies, json={'schoolYear': school_year, 'date': date, 'statusFilter': '-1'})

    homework_json = homework.json()

    with open('json/homework.json', 'w') as f:
        json.dump(homework_json, f)

def prepare_homework_for_display():
    with open('json/homework.json') as f:
        homework = json.loads(f.read())

    i = 0
    a = 0

    for i in range(5):
        print('------------------------------------------------')
        if i == 0:
            print('PONIEDZIAŁEK')
        elif i == 1:
            print('WTOREK')
        elif i == 2:
            print('ŚRODA')
        elif i == 3:
            print('CZWARTEK')
        elif i == 4:
            print('PIĄTEK')
        print('------------------------------------------------')
        if homework['data'][i]['Homework'] != []:
            print('Przedmiot: '+homework['data'][i]['Homework'][a]['Subject'])
            print('Nauczyciel: '+homework['data'][i]['Homework'][a]['Teacher'])
            print('Opis: '+homework['data'][i]['Homework'][a]['Description'])
            print('Data: '+homework['data'][i]['Homework'][a]['Date'])
            print('------------------------------------------------')
            if homework['data'][i]['Homework'][a] == homework['data'][i]['Homework'][-1]:
                a = 0
            else:
                a += 1
        else:
            print('Brak zadań domowych na ten dzień')