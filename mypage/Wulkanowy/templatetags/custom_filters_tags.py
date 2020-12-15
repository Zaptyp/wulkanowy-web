from django import template
from django.utils.safestring import mark_safe

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
def set_color(grade, value):
    if value == '6' or value == '6-':
        return mark_safe(f"<div class='grade' style='background-color: #3dbbf5;'>{grade}</div>")
    elif value == '5' or value == '5-' or value == '5+':
        return mark_safe(f"<div class='grade' style='background-color: #4caf50;'>{grade}</div>")
    elif value == '4' or value == '4-' or value == '4+':
        return mark_safe(f"<div class='grade' style='background-color: #a0c431;'>{grade}</div>")
    elif value == '3' or value == '3-' or value == '3+':
        return mark_safe(f"<div class='grade' style='background-color: #ffb940;'>{grade}</div>")
    elif value == '2' or value == '2-' or value == '2+':
        return mark_safe(f"<div class='grade' style='background-color: #ff774d;'>{grade}</div>")
    elif value == '1' or value == '1+':
        return mark_safe(f"<div class='grade' style='background-color: #d43f3f;'>{grade}</div>")
    else:
        return mark_safe(f"<div class='grade-else' style='background-color: #607d8b;'>{grade}</div>")

@register.filter
def simple_data(exam):

    return_html = ''

    if exam != {}:
        for exams in exam:
            lesson = exam[exams]['Przedmiot']
            if exam[exams]['Opis'] == '':
                description = '<span style="color: #d11204;"><i>Brak Opisu</i></span>'
            else:
                description = exam[exams]['Opis']
            date = exam[exams]['Data']
            if return_html == '':
                return_html += f'{lesson}<br /><span style="color: green;"><i>{description}</i></span><br />{date}<br />'
            else:
                return_html += f'<div class="line"></div>{lesson}<br /><span style="color: green;"><i>{description}</i></span><br />{date}<br />'

        return mark_safe(return_html)
    else:
        print('Brak sprawdzianów')
        return mark_safe('Brak Sprawdzianów')