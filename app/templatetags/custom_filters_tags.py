from django import template
from django.utils.safestring import mark_safe
from app.login import get_cookies
from app.API.homework import prepare_homework_for_display

register = template.Library()

@register.filter
def return_item(l, i):
    try:
        if l[i] == []:
            return ['Brak Ocen']
        else:
            return l[i]
    except:
        return None

@register.filter
def set_color(grade):
    if grade == '6' or grade == '6-':
        return '#3dbbf5'
    elif grade == '5' or grade == '5-' or grade == '5+':
        return '#4caf50'
    elif grade == '4' or grade == '4-' or grade == '4+':
        return '#a0c431'
    elif grade == '3' or grade == '3-' or grade == '3+':
        return '#ffb940'
    elif grade == '2' or grade == '2-' or grade == '2+':
        return '#ff774d'
    elif grade == '1' or grade == '1+':
        return '#d43f3f'
    else:
        return '#607d8b'

@register.filter
def simple_data(exam):
    return_html = []
    if exam != {}:
        for exams in exam:
            lesson = exam[exams]['Przedmiot']
            if exam[exams]['Opis'] == '':
                description = 'Brak Opisu'
            else:
                description = exam[exams]['Opis']
            date = exam[exams]['Data']
            if return_html == []:
                return_html.append([lesson, description, date])
            else:
                return_html.append([lesson, description, date])
        return return_html
    else:
        return mark_safe('Brak Sprawdzianów')

homework_all = None

@register.filter
def week_homework(no):
    global homework_all
    cookie = get_cookies()
    if homework_all == None:
        homework_all = prepare_homework_for_display(cookie[0], cookie[1], cookie[2], cookie[3], cookie[5])
    homework = []

    for i in range(4):
        homework.append(homework_all[i][no])
        
    return homework

@register.filter
def points_color(points):
    if int(points) < 0:
        return 'red;'
    elif int(points) > 0:
        return 'green;'
    else:
        return 'black;'

@register.filter
def suffix(points):
    if int(points) == 0 or int(points) >= 5 or int(points) <= -5:
        return points+' punktów'
    elif int(points) == -1 or int(points) == 1:
        return points+' punkt'
    elif int(points) > -5 and int(points) <= -2:
        return points+' punkty'