from django import template

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