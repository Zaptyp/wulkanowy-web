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
import datetime

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

    print('<--------------------FREKWENCJA-------------------->')
    print('--------------------PONIEDZIAŁEK--------------------')
    while True:
        print('Treść: '+attendance['data']['Frekwencje'][i]['Symbol'])
        print('Przedmiot: '+attendance['data']['Frekwencje'][i]['PrzedmiotNazwa'])
        print('-----------------------------------------------------')
        if attendance['data']['Frekwencje'][i] == attendance['data']['Frekwencje'][-1]:
            i = 0
            break
        if attendance['data']['Frekwencje'][i]['NrDnia'] != attendance['data']['Frekwencje'][i+1]['NrDnia']:
            if attendance['data']['Frekwencje'][i+1]['NrDnia'] == 2:
                print('--------------------WTOREK--------------------')
            elif attendance['data']['Frekwencje'][i+1]['NrDnia'] == 3:
                print('--------------------ŚRODA--------------------')
            elif attendance['data']['Frekwencje'][i+1]['NrDnia'] == 4:
                print('--------------------CZWARTEK--------------------')
            elif attendance['data']['Frekwencje'][i+1]['NrDnia'] == 5:
                print('--------------------PIĄTEK--------------------')
        i += 1