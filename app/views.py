from requests import get
from cryptography.fernet import Fernet
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import requests
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from .login import sender
from .API.grades import get_grades
from .API.exams import get_exams
from .API.timetable import get_timetable
from .API.notes import get_notes
from .API.attendance import get_attendance
from .API.messages import get_received_messages, get_sent_messages, get_deleted_messages, get_recipients, send_message, get_message_content
from .API.homeworks import get_homeworks
from .API.mobile_access import get_registered_devices, register_device
from .API.school_data import get_school_data
from .API.dashboard import get_dashboard
from .decrypt import decrypt_cookies

#API
def login(request, *args, **kwargs):
    data = json.loads(request.body)
    loginName = data['loginName']
    Password = data['Password']
    symbol = data['Symbol']
    diary_url = data['diaryUrl']
    if diary_url != 'http://cufs.fakelog.cf/':
        link = f'{diary_url}{symbol}/Account/LogOn?ReturnUrl=%2F{symbol}%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f{symbol}%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f{symbol}%252fLoginEndpoint.aspx'
    else:
        link = 'http://cufs.fakelog.cf/powiatwulkanowy/FS/LS?wa=wsignin1.0&wtrealm=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx&wctx=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx'
    s = requests.Session()
    sender_return = sender(link, loginName, Password, ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol, diary_url, s)
    if sender_return == {'success': False}:
        data_response = {
            'success': False
        }
    else:
        request.session['is_logged'] = True
        while True:
            try:
                request.session[request.session.session_key] = Fernet.generate_key().decode('utf-8')
                rkey = Fernet(bytes(request.session[request.session.session_key], 'utf-8'))
                break
            except KeyError:
                continue
            
        sender_return['s'] = json.dumps(sender_return['s'])
        sender_return['s'] = sender_return['s'].encode()
        sender_return['s'] = rkey.encrypt(sender_return['s'])
        sender_return['s'] = sender_return['s'].decode('utf-8')
        data_response = {'success': True, 'data': sender_return}
    return JsonResponse(data_response)

def grades(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        grades = get_grades(register_id, register_r, oun, s)
        return JsonResponse(grades)
    else:
        return redirect('../')

def timetable(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        timetable = get_timetable(register_id, register_r, oun, s, date)
        return JsonResponse(timetable)
    else:
        return redirect('../')

def exams(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        exams = get_exams(register_id, register_r, oun, s, date, school_year)
        return JsonResponse(exams)
    else:
        return redirect('../')

def homeworks(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        homeworks = get_homeworks(register_id, register_r, oun, s, date, school_year)
        return JsonResponse(homeworks)
    else:
        return redirect('../')

def attendance(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        attendance = get_attendance(register_id, register_r, oun, s, date)
        return JsonResponse(attendance, safe=False)
    else:
        return redirect('../')

def notes(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        notes = get_notes(register_id, register_r, oun, s)
        return JsonResponse(notes)
    else:
        return redirect('../')

def registered_devices(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        registered = get_registered_devices(register_id, register_r, oun, s)
        return JsonResponse(registered)
    else:
        return redirect('../')

def register_device_(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        register_data = register_device(register_id, register_r, oun, s)
        return JsonResponse(register_data)
    else:
        return redirect('../')

def received_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        received_messages = get_received_messages(register_id, register_r, oun, s, date, school_year, symbol)
        return JsonResponse(received_messages)
    else:
        return redirect('../')

def sent_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        sent_messages = get_sent_messages(register_id, register_r, oun, s, date, school_year, symbol)
        return JsonResponse(sent_messages)
    else:
        return redirect('../')

def deleted_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        deleted_messages = get_deleted_messages(register_id, register_r, oun, s, date, school_year, symbol)
        return JsonResponse(deleted_messages)
    else:
        return redirect('../')

def recipients(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        recipients = get_recipients(register_id, register_r, oun, s, date, school_year, symbol)
        return JsonResponse(recipients)
    else:
        return redirect('../')

def school_data(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        school_data = get_school_data(register_id, register_r, oun, s)
        return JsonResponse(school_data)
    else:
        return redirect('../')

def dashboard(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        diary_url = data['data']['diary_url']
        symbol = data['data']['symbol']
        dashboard = get_dashboard(register_id, register_r, s, diary_url, symbol)
        return JsonResponse(dashboard)
    else:
        return redirect('../')

def send(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        cookies_data = json.loads(data['cookies_data'])
        register_id = cookies_data['data']['register_id']
        register_r = cookies_data['data']['register_r']
        oun = cookies_data['data']['oun']
        s = cookies_data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = cookies_data['data']['date']
        school_year = cookies_data['data']['school_year']
        symbol = cookies_data['data']['symbol']
        send_data = {'data': data['data'], 'subject': data['subject'], 'content': data['content']}
        send = send_message(register_id, register_r, oun, s, date, school_year, symbol, send_data)
        return JsonResponse(send, safe=False)
    else:
        return redirect('../')

def message_content(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        cookies_data = json.loads(data['cookies_data'])
        register_id = cookies_data['data']['register_id']
        register_r = cookies_data['data']['register_r']
        oun = cookies_data['data']['oun']
        s = cookies_data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = cookies_data['data']['date']
        school_year = cookies_data['data']['school_year']
        symbol = cookies_data['data']['symbol']
        message_id = data['message_id']
        content = get_message_content(register_id, register_r, oun, s, date, school_year, symbol, message_id)
        return JsonResponse(content, safe=False)
    else:
        return redirect('../')