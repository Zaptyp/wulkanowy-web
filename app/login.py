import os
import sys
import requests
from django.contrib.sessions.models import Session
from django.http import JsonResponse
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json
import requests
from django.shortcuts import redirect
from bs4 import BeautifulSoup
import datetime

def sender(url, loginName, Password, params_names, fail_phrase, symbol, diary_url, s):
    data = [params_names[0], loginName, params_names[1], Password]

    sender_return = send(url, data, fail_phrase, diary_url, symbol, s)
    if sender_return == {'success': False}:
        return {'success': False}
    else:
        return sender_return

def send(url, data, fail, diary_url, symbol, s):
    ready_data = {data[0]: data[1], data[2]: data[3]}
    page = s.post(url=url, data=ready_data)
    if fail in page.text:
        return {'success': False}
    else:
        if diary_url == 'http://cufs.fakelog.cf/':
            page = s.get('http://cufs.fakelog.cf/powiatwulkanowy/FS/LS?wa=wsignin1.0&wtrealm=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx&wctx=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx')
        bs = BeautifulSoup(page.text, 'html.parser')
        wa = bs.find('input', {'name': 'wa'})['value']
        cert = bs.find('input', {'name': 'wresult'})['value']
        wctx = bs.find('input', {'name': 'wctx'})['value']

        crtr = s.post(url=wctx, headers={"User-Agent": "Wulkanowy-web :)"}, data={"wa": wa, "wresult": cert, "wctx": wctx})

        bs = BeautifulSoup(crtr.content, 'html.parser')
        for a in bs.find_all('a', title='Uczeń'):
            oun = a['href']
            break

        if diary_url == 'http://cufs.fakelog.cf/':
            oun = 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458'

        cookies = get_cookies(symbol, oun, s, diary_url)

        return cookies

def get_cookies(symbol, oun, s, diary_url):
    register_r = s.post(oun+'/UczenDziennik.mvc/Get')
    register_id = register_r.json()['data'][0]['Okresy'][0]['Id']
            
    now = datetime.datetime.now()
    weekday = now.weekday()

    for x in range(7):
        if weekday == x:
            now = now - datetime.timedelta(days=x)

    day = now.day
    month = now.month
    year = now.year

    date = datetime.date(year, month, day).isoformat()

    date = f'{date}T00:00:00'

    school_year = register_r.json()['data'][0]['DziennikRokSzkolny']

    data = {
        'register_id': register_id,
        'register_r': register_r.json(),
        'oun': oun,
        'date': str(date),
        'school_year': school_year,
        'symbol': symbol,
        's': s.cookies.get_dict(),
        'diary_url': diary_url
    }

    return data