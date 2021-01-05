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

oun = ''
s = requests.Session()
symbol = ''

def sender(url, loginName, Password, params_names, fail_phrase, sym, diary_url):
    global symbol
    data = []
    data.append((params_names[0], loginName, params_names[1], Password))
    symbol = sym

    for index, single_data in enumerate(data):
        index += 1
        if send(url, single_data, fail_phrase, diary_url):
            return True
        else:
            return False
                
def send(url, data, fail, diary_url):
    ready_data = {data[0]: data[1], data[2]: data[3]}
    page = s.post(url=url, data=ready_data)
    print(page.text)
    if fail in page.text:
        return False
    else:
        global symbol
        if diary_url == 'http://cufs.fakelog.cf/':
            page = s.get('http://cufs.fakelog.cf/powiatwulkanowy/FS/LS?wa=wsignin1.0&wtrealm=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx&wctx=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx')
        bs = BeautifulSoup(page.text, 'html.parser')
        wa = bs.find('input', {'name': 'wa'})['value']
        cert = bs.find('input', {'name': 'wresult'})['value']
        wctx = bs.find('input', {'name': 'wctx'})['value']

        print(wa)
        print('------------------------------------------------------------')
        print(cert)
        print('------------------------------------------------------------')
        print(wctx)
        print('------------------------------------------------------------')

        crtr = s.post(url=wctx, headers={"User-Agent": "Wulkanowy-web :)"}, data={"wa": wa, "wresult": cert, "wctx": wctx})
            
        bs = BeautifulSoup(crtr.content, 'html.parser')
        global oun
        for a in bs.find_all('a', title='Uczeń'):
            oun = a['href']
            break

        if diary_url == 'http://cufs.fakelog.cf/':
            oun = 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458'

        return True 

def get_cookies():
    global symbol
    global oun
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

    return [register_id, register_r, oun, s, date, school_year, symbol]