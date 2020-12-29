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

    messages_tree = s.get('https://uonetplus-uzytkownik.vulcan.net.pl/'+symbol+'/Wiadomosc.mvc/GetMessagesTree?_dc='+str(now)+'&node=root', headers=headers)
    for i in range(5):
        date_to = messages_tree.json()['children'][0]['children'][i]['ObjectData']['DataDo']
        if i != 4:
            date_from = messages_tree.json()['children'][0]['children'][i]['ObjectData']['DataOd']
            messages = s.get('https://uonetplus-uzytkownik.vulcan.net.pl/'+symbol+'/Wiadomosc.mvc/GetInboxMessages?_dc='+str(now)+'&dataOd='+date_from+'&dataDo='+date_to+'&page=1&start=0&limit=25', headers=headers)
        else:
            messages = s.get('https://uonetplus-uzytkownik.vulcan.net.pl/'+symbol+'/Wiadomosc.mvc/GetInboxMessages?_dc='+str(now)+'&dataDo='+date_to+'&page=1&start=0&limit=25', headers=headers)
        if messages.json()['data'] != []:
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