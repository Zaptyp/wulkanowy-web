from requests import get
from django.shortcuts import render
from .login import sender, get_cookies
from .forms import loginForm
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from .API.grades import prepare_grades_for_display
from .API.exams import prepare_exams_for_display
from .API.timetable import prepare_timetable_for_display
from .API.notes import prepare_notes_for_display
from .API.attendance import prepare_attendance_for_display
from .API.messages import get_messages

def default_view(request, *args, **kwargs):
    sender_return = None
    new_form = loginForm()
    if request.method == "POST":
        new_form = loginForm(request.POST)
        if new_form.is_valid():
            symbol = new_form.cleaned_data['Symbol']
            link = 'https://cufs.vulcan.net.pl/'+symbol+'/Account/LogOn?ReturnUrl=%2F'+symbol+'%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx'
            sender_return = sender(link, new_form.cleaned_data['loginName'], new_form.cleaned_data['Password'], ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol)
    context = {'form' : new_form}
    if sender_return == False:
        return redirect('/error/')
    elif sender_return == True:
        request.session['is_logged'] = True    
        return redirect('/oceny/')
    else:
        return render(request, 'index.html', context)

def error_view(request, *args, **kwargs):
    sender_return = None
    new_form = loginForm()
    if request.method == "POST":
        new_form = loginForm(request.POST)
        if new_form.is_valid():
            symbol = new_form.cleaned_data['Symbol']
            link = 'https://cufs.vulcan.net.pl/'+symbol+'/Account/LogOn?ReturnUrl=%2F'+symbol+'%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx'
            sender_return = sender(link, new_form.cleaned_data['loginName'], new_form.cleaned_data['Password'], ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol) 
    context = {'form' : new_form, 'error' : 'Niepoprawny e-mail lub hasło'}
    if sender_return == False:
        return redirect('/error/')
    elif sender_return == True:
        request.session['is_logged'] = True
        return redirect('/oceny/')
    else:
        return render(request, 'form_error.html', context)

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
        content = {'json_data': messages}
        return render(request, 'wiadomosci.html', content)
    else:
        return redirect(default_view)