import requests
import json
import calendar
import time

def get_messages(register_id, register_r, oun, s, date, school_year, symbol):
    headers = {
        'User-Agent': 'Wulkanowy-web :)'
    }

    now = calendar.timegm(time.gmtime())
    received_messages = []

    messages = s.get('https://uonetplus-uzytkownik.vulcan.net.pl/nowysacz/Wiadomosc.mvc/GetInboxMessages?_dc='+str(now)+'&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers)

    for j in messages.json()['data']:
        received_messages.append({
            'Subject': j['Temat'],
            'Sender': j['Nadawca']['Name'],
            'Date': j['Data'],
            'Read': j['Nieprzeczytana'],
            'Id': j['Id']
        })

    print(received_messages)

    return 'Bla'