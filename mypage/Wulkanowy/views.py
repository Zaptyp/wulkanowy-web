from bs4 import BeautifulSoup
from requests import get
from django.shortcuts import render
from .classes import Sender
from .forms import loginForm
import os
import json
from django.shortcuts import redirect
from .API.grades import prepare_grades_for_display
from .API.homework import prepare_homework_for_display
from .API.exams import prepare_exams_for_display
from .API.timetable import prepare_timetable_for_display
from .API.notes import prepare_notes_for_display
from .API.attendance import prepare_attendance_for_display

def default_view(request, *args, **kwargs):
    new_form = loginForm()
    if request.method == "POST":
        new_form = loginForm(request.POST)
        if new_form.is_valid():
            symbol = new_form.cleaned_data['Symbol']
            link = 'https://cufs.vulcan.net.pl/'+symbol+'/Account/LogOn?ReturnUrl=%2F'+symbol+'%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx'
            Sender(link, new_form.cleaned_data['loginName'], new_form.cleaned_data['Password'], ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol)
    context = {'form' : new_form}
    f = open("data.txt", "r")
    status = f.read()
    f.close()
    open("data.txt", "w").close()
    if status == "Denied":
        status = ''
        return redirect('/error/')
    elif status == "Accepted":
        status = ''
        f = open("data.txt", "r")
        status = f.read()
        print(status)
        f.close()

        return redirect('/oceny/')
    else:
        status = ''
        return render(request, 'index.html', context)

def error_view(request, *args, **kwargs):
    new_form = loginForm()
    if request.method == "POST":
        new_form = loginForm(request.POST)
        if new_form.is_valid():
            symbol = new_form.cleaned_data['Symbol']
            link = 'https://cufs.vulcan.net.pl/'+symbol+'/Account/LogOn?ReturnUrl=%2F'+symbol+'%2FFS%2FLS%3Fwa%3Dwsignin1.0%26wtrealm%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx%26wctx%3Dhttps%253a%252f%252fuonetplus.vulcan.net.pl%252f'+symbol+'%252fLoginEndpoint.aspx'
            Sender(link, new_form.cleaned_data['loginName'], new_form.cleaned_data['Password'], ('loginName', 'Password'), 'Zła nazwa użytkownika lub hasło', symbol)
    error_mess = 'Niepoprawny e-mail lub hasło'
    context = {'form' : new_form, 'error' : error_mess}
    f = open("data.txt", "r")
    status = f.read()
    print(status)
    f.close()
    open("data.txt", "w").close()
    if status == "Denied":
        status = None
        return redirect('/error/')
    elif status == "Accepted":
        status = None
        return redirect('/oceny/')
    else:
        status = None
        return render(request, 'form_error.html', context)

def grades_view(request, *args, **kwargs):
    grades = prepare_grades_for_display()
    
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

def homework_view(request, *args, **kwargs):
    prepare_homework_for_display()
    content = {'json_data': None}
    return render(request, 'zadania.html', content)

def timetable_view(request, *args, **kwargs):
    prepare_timetable_for_display()
    content = {'json_data': None}
    return render(request, 'plan.html', content)

def attendance_view(request, *args, **kwargs):
    prepare_attendance_for_display()
    content = {'json_data': None}
    return render(request, 'frekwencja.html', content)

def notes_view(request, *args, **kwargs):
    prepare_notes_for_display()
    content = {'json_data': None}
    return render(request, 'uwagi.html', content)

def exams_view(request, *args, **kwargs):
    prepare_exams_for_display()
    content = {'json_data': None}
    return render(request, 'sprawdziany.html', content)

def messeges_view(request, *args, **kwargs):
    return render(request, 'wiadomosci.html')