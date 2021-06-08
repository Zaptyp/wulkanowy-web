from requests import get
from cryptography.fernet import Fernet
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import requests
from rest_framework.decorators import api_view
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
from .API.student_data import get_student_data
from .API.stats import get_partial, get_year
from .decrypt import decrypt_cookies
import datetime

#API
@api_view(['POST'])
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
        request.session[request.session.session_key] = Fernet.generate_key().decode('utf-8')
        rkey = Fernet(bytes(request.session[request.session.session_key], 'utf-8'))
            
        sender_return['s'] = json.dumps(sender_return['s'])
        sender_return['s'] = sender_return['s'].encode()
        sender_return['s'] = rkey.encrypt(sender_return['s'])
        sender_return['s'] = sender_return['s'].decode('utf-8')
        data_response = {'success': True, 'data': sender_return}
    return JsonResponse(data_response)

@api_view(['POST'])
def grades(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        grades = get_grades(register_id, students, school_url, s)
        return JsonResponse(grades)
    else:
        return redirect('../')

@api_view(['POST'])
def timetable(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        week = data['week']
        data = json.loads(data['cookies'])
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        now = datetime.datetime.now()
        weekday = now.weekday()

        for x in range(7):
            if weekday == x:
                now = now - datetime.timedelta(days=x)

        now = now + datetime.timedelta(days=week*7)

        day = now.day
        month = now.month
        year = now.year

        date = datetime.date(year, month, day).isoformat()

        date = f'{date}T00:00:00'
        timetable = get_timetable(register_id, students, school_url, s, date)
        return JsonResponse(timetable)
    else:
        return redirect('../')

@api_view(['POST'])
def exams(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        week = data['week']
        data = json.loads(data['cookies'])
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        now = datetime.datetime.now()
        weekday = now.weekday()

        for x in range(7):
            if weekday == x:
                now = now - datetime.timedelta(days=x)

        now = now + datetime.timedelta(days=week*7)

        day = now.day
        month = now.month
        year = now.year

        date = datetime.date(year, month, day).isoformat()

        date = f'{date}T00:00:00'
        school_year = data['data']['school_year']
        exams = get_exams(register_id, students, school_url, s, date, school_year)
        return JsonResponse(exams)
    else:
        return redirect('../')

@api_view(['POST'])
def homeworks(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        week = data['week']
        data = json.loads(data['cookies'])
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        now = datetime.datetime.now()
        weekday = now.weekday()

        for x in range(7):
            if weekday == x:
                now = now - datetime.timedelta(days=x)

        now = now + datetime.timedelta(days=week*7)

        day = now.day
        month = now.month
        year = now.year

        date = datetime.date(year, month, day).isoformat()

        date = f'{date}T00:00:00'
        school_year = data['data']['school_year']
        homeworks = get_homeworks(register_id, students, school_url, s, date, school_year)
        return JsonResponse(homeworks)
    else:
        return redirect('../')

@api_view(['POST'])
def attendance(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        week = data['week']
        data = json.loads(data['cookies'])
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        now = datetime.datetime.now()
        weekday = now.weekday()

        for x in range(7):
            if weekday == x:
                now = now - datetime.timedelta(days=x)

        now = now + datetime.timedelta(days=week*7)

        day = now.day
        month = now.month
        year = now.year

        date = datetime.date(year, month, day).isoformat()

        date = f'{date}T00:00:00'
        attendance = get_attendance(register_id, students, school_url, s, date)
        return JsonResponse(attendance, safe=False)
    else:
        return redirect('../')

@api_view(['POST'])
def notes(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        notes = get_notes(register_id, students, school_url, s)
        return JsonResponse(notes)
    else:
        return redirect('../')

@api_view(['POST'])
def registered_devices(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        registered = get_registered_devices(register_id, students, school_url, s)
        return JsonResponse(registered)
    else:
        return redirect('../')

@api_view(['POST'])
def register_device_(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        register_data = register_device(register_id, students, school_url, s)
        return JsonResponse(register_data)
    else:
        return redirect('../')

@api_view(['POST'])
def received_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        received_messages = get_received_messages(register_id, students, school_url, s, date, school_year, symbol)
        return JsonResponse(received_messages)
    else:
        return redirect('../')

@api_view(['POST'])
def sent_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        sent_messages = get_sent_messages(register_id, students, school_url, s, date, school_year, symbol)
        return JsonResponse(sent_messages)
    else:
        return redirect('../')

@api_view(['POST'])
def deleted_messages(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        deleted_messages = get_deleted_messages(register_id, students, school_url, s, date, school_year, symbol)
        return JsonResponse(deleted_messages)
    else:
        return redirect('../')

@api_view(['POST'])
def recipients(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = data['data']['date']
        school_year = data['data']['school_year']
        symbol = data['data']['symbol']
        recipients = get_recipients(register_id, students, school_url, s, date, school_year, symbol)
        return JsonResponse(recipients)
    else:
        return redirect('../')

@api_view(['POST'])
def school_data(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        school_data = get_school_data(register_id, students, school_url, s)
        return JsonResponse(school_data)
    else:
        return redirect('../')

@api_view(['POST'])
def dashboard(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        diary_url = data['data']['diary_url']
        symbol = data['data']['symbol']
        dashboard = get_dashboard(register_id, students, s, diary_url, symbol)
        return JsonResponse(dashboard)
    else:
        return redirect('../')

@api_view(['POST'])
def send(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        cookies_data = json.loads(data['cookies_data'])
        register_id = cookies_data['data']['register_id']
        students = cookies_data['data']['students']
        school_url = cookies_data['data']['school_url']
        s = cookies_data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = cookies_data['data']['date']
        school_year = cookies_data['data']['school_year']
        symbol = cookies_data['data']['symbol']
        send_data = {'data': data['data'], 'subject': data['subject'], 'content': data['content']}
        send = send_message(register_id, students, school_url, s, date, school_year, symbol, send_data)
        return JsonResponse(send, safe=False)
    else:
        return redirect('../')

@api_view(['POST'])
def message_content(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        cookies_data = json.loads(data['cookies_data'])
        register_id = cookies_data['data']['register_id']
        students = cookies_data['data']['students']
        school_url = cookies_data['data']['school_url']
        s = cookies_data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        date = cookies_data['data']['date']
        school_year = cookies_data['data']['school_year']
        symbol = cookies_data['data']['symbol']
        message_id = data['message_id']
        content = get_message_content(register_id, students, school_url, s, date, school_year, symbol, message_id)
        return JsonResponse(content, safe=False)
    else:
        return redirect('../')

@api_view(['POST'])
def student_data(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        data = get_student_data(register_id, students, school_url, s)
        return JsonResponse(data)
    else:
        return redirect('../')

#STATS
@api_view(['POST'])
def partial(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        partial_stats = get_partial(register_id, students, school_url, s)
        return JsonResponse(partial_stats)
    else:
        return redirect('../')

@api_view(['POST'])
def year(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        students = data['data']['students']
        school_url = data['data']['school_url']
        s = data['data']['s']
        key = bytes(request.session[request.session.session_key], 'utf-8')
        s = decrypt_cookies(s, key)
        year_stats = get_year(register_id, students, school_url, s)
        return JsonResponse(year_stats)
    else:
        return redirect('../')

@api_view(['GET'])
def log_out(request, *args, **kwargs):
    del request.session[request.session.session_key]
    del request.session['is_logged']
    return JsonResponse({'logOut': True})