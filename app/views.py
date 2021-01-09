from requests import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import requests
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from .login import sender
from .API.grades import get_grades
from .API.exams import prepare_exams_for_display
from .API.timetable import prepare_timetable_for_display
from .API.notes import prepare_notes_for_display
from .API.attendance import prepare_attendance_for_display
from .API.messages import get_messages

#views
def default_view(request, *args, **kwargs):
    return render(request, 'index.html')

def content_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        return render(request, 'content.html')
    else:
        return render(request, 'index.html')

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
        data_response = {'success': True, 'data': sender_return}
    return JsonResponse(data_response)

def grades(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        data = json.loads(request.body)
        register_id = data['data']['register_id']
        register_r = data['data']['register_r']
        oun = data['data']['oun']
        s = data['data']['s']
        grades = get_grades(register_id, register_r, oun, s)
        return JsonResponse(grades, safe=False)