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
from .API.grades import get_grades
from .API.attendance import get_attendance
from .API.exams import get_exams
from .API.homework import get_homework
from .API.messeges import GetMesseges
from .API.timetable import get_timetable
from .API.notes import get_notes

# Create your models here.
class Sender():
    def __init__(self, url, loginName, Password, params_names, fail_phrase, symbol):
        self.url = url
        self.fail = fail_phrase
        self.loginName = loginName
        self.Password = Password
        self.data = []
        self.data.append((params_names[0], self.loginName, params_names[1], self.Password))
        self.symbol = symbol

        for index, single_data in enumerate(self.data):
            index += 1
            if self.send(self.url, single_data, self.fail):
                self.Accepted(self.data)
            else:
                self.Denied()
                
    def send(self, url, data, fail):
        ready_data = {data[0]: data[1], data[2]: data[3]}
        s = requests.Session()
        r = s.post(url=url, data=ready_data)
        if fail in r.text:
            return False
        else:
            page = r
            bs = BeautifulSoup(page.text, 'html.parser')
            wa = bs.find('input', {'name': 'wa'})['value']
            cert = bs.find('input', {'name': 'wresult'})['value']
            wctx = bs.find('input', {'name': 'wctx'})['value']
            cert_url = 'https://uonetplus.vulcan.net.pl/'+self.symbol+'/LoginEndpoint.aspx'

            crtr = s.post(url=cert_url, headers={"User-Agent": "Wulkanowy-web :)"}, data={"wa": wa, "wresult": cert, "wctx": wctx})

            bs = BeautifulSoup(crtr.content, 'html.parser')
            for a in bs.find_all('a', title='Uczeń'):
                oun = a['href']
                break

            register_r = s.post(oun+'/UczenDziennik.mvc/Get')
            register_id = register_r.json()['data'][0]['Okresy'][0]['Id']
            
            now = datetime.datetime.now()
            weekday = now.weekday()

            for x in range(7):
                if weekday == x:
                    now = now - datetime.timedelta(days=x)

            day = str(now.day)
            month = str(now.month)
            year = str(now.year)

            date = year+'-'+month+'-'+day

            school_year = register_r.json()['data'][0]['DziennikRokSzkolny']

            get_grades(register_id, register_r, oun, s)
            get_attendance(register_id, register_r, oun, s, date)
            get_exams(register_id, register_r, oun, s, date, school_year)
            get_homework(register_id, register_r, oun, s, date, school_year)
            GetMesseges(register_id, register_r, oun, s, date)
            get_timetable(register_id, register_r, oun, s, date)
            get_notes(register_id, register_r, oun, s)

            return True
    
    def Denied(self):
        print("Niezalogowano!")
        f = open("data.txt", "w")
        f.write("Denied")
        f.close()

    def Accepted(self, data):
        f = open("data.txt", "w")
        f.write("Accepted")
        f.close()