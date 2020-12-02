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

    attendance_lessons = s.post(oun+'/FrekwencjaStatystykiPrzedmioty.mvc/Get', cookies=cookies)

    attendance_lessons_json = attendance_lessons.json()

    attendance_json_id = attendance_lessons.json()['data'][0]['Id']

    attendance = s.post(oun+'/Frekwencja.mvc/Get', cookies=cookies, json={'idTypWpisuFrekwencji': attendance_json_id, 'data': date})

    attendance_json = attendance.json()

    with open('json/attendance_lessons.json', 'w') as f:
        json.dump(attendance_lessons_json, f)

    with open('json/attendance.json', 'w') as f:
        json.dump(attendance_json, f)