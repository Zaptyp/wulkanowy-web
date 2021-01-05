from requests import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from .login import sender, get_cookies
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from .API.grades import prepare_grades_for_display
from .API.exams import prepare_exams_for_display
from .API.timetable import prepare_timetable_for_display
from .API.notes import prepare_notes_for_display
from .API.attendance import prepare_attendance_for_display
from .API.messages import get_messages

def default_view(request, *args, **kwargs):
    return render(request, 'index.html')


def grades_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        grades = prepare_grades_for_display(cookies[0], cookies[1], cookies[2], cookies[3])
    
        grade = {}
        description = {}

        for i in grades[1]:
            grade.update({i: []})
            description.update({i: []})
            for items in grades[0][i]:
                grade[i].append(items['Ocena'])
                description[i].append(items['Opis'])

        content = {'gc': grade, 'dc': description, 'lesson': grades[1]}
        return render(request, 'oceny.html', content)
    else:
        return redirect(default_view)

def homework_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        return render(request, 'zadania.html')
    else:
        return redirect(default_view)

def timetable_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        timetable = prepare_timetable_for_display(cookies[0], cookies[1], cookies[2], cookies[3], cookies[4])

        hour = {}

        for i in timetable['hour']:
            hour.update({i[0]: []})
            hour[i[0]].append(i[1])
            hour[i[0]].append(i[2])

        content = {
            'hour': hour,
            'monday': timetable['monday'],
            'tuesday': timetable['tuesday'],
            'wednesday': timetable['wednesday'],
            'thrusday': timetable['thrusday'],
            'friday': timetable['friday']
            }

        return render(request, 'plan.html', content)
    else:
        return redirect(default_view)

def attendance_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        attendance = prepare_attendance_for_display(cookies[0], cookies[1], cookies[2], cookies[3], cookies[4])
        content = {'attendance': attendance}        

        return render(request, 'frekwencja.html', content)
    else:
        return redirect(default_view)

def notes_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        notes = prepare_notes_for_display(cookies[0], cookies[1], cookies[2], cookies[3])

        content = {
            'notes': notes[0],
            'achievements': notes[1]
            }

        return render(request, 'uwagi.html', content)
    else:
        return redirect(default_view)

def exams_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        print(cookies)
        exams = prepare_exams_for_display(cookies[0], cookies[1], cookies[2], cookies[3], cookies[4], cookies[5])

        positions = []

        for x in range(4):
            positions.append(exams[x])

        content = {'content': positions}

        return render(request, 'sprawdziany.html', content)
    else:
        return redirect(default_view)

def messages_view(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        messages = get_messages(cookies[0], cookies[1], cookies[2], cookies[3], cookies[4], cookies[5], cookies[6])
        content = {'messages': messages[0]}
        return render(request, 'wiadomosci.html', content)
    else:
        return redirect(default_view)

def change_messages_content(request, *args, **kwargs):
    if request.session.has_key('is_logged'):
        cookies = get_cookies()
        messages = get_messages(cookies[0], cookies[1], cookies[2], cookies[3], cookies[4], cookies[5], cookies[6])
        id = request.GET.get('id')
        
        if id == 'received':
            content = {'messages': messages[0]}
        elif id == 'sent':
            content = {'messages': messages[1]}
        elif id == 'deleted':
            content = {'messages': messages[2]}
        return render(request, 'messages_content.html', content)
    else:
        return redirect(default_view)

#API
def login(request, *args, **kwargs):
    sender_return = None
    data = json.loads(request.body)
    loginName = data['loginName']
    Password = data['Password']
    symbol = data['Symbol']
    diary_url = data['diaryUrl']
    if diary_url != 'http://cufs.fakelog.cf/':
        link = f'{diary_url}{symbol}/Account/LogOn?ReturnUrl=%2F{symbol}%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f{symbol}%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f{symbol}%252fLoginEndpoint.aspx'
    else:
        link = 'http://cufs.fakelog.cf/powiatwulkanowy/FS/LS?wa=wsignin1.0&wtrealm=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx&wctx=http://uonetplus.fakelog.localhost:300/powiatwulkanowy/LoginEndpoint.aspx'
    sender_return = sender(link, loginName, Password, ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol, diary_url)
    print(sender_return)
    if sender_return == False:
        data = {
            'success': False
        }
    elif sender_return == True:
        request.session['is_logged'] = True
        data = {
            'success': True
        }
    return JsonResponse(data)
