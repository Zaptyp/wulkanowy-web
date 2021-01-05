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
    sent_messages = []
    deleted_messages = []

    messages = s.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers)
    for j in messages.json()['data']:
        received_messages.append({
            'Subject': j['Temat'],
            'Sender': j['Nadawca']['Name'],
            'Date': j['Data'],
            'Read': j['Nieprzeczytana'] == False,
            'Id': j['Id']
        })

    messages = s.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetOutboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25')
    for j in messages.json()['data']:
        sent_messages.append({
            'Subject': j['Temat'],
            'Recipients': get_recipients(j),
            'Date': j['Data'],
            'Read': j['Przeczytane'],
            'Unread': j['Nieprzeczytane'],
            'Id': j['Id']
        })

    messages = s.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetTrashboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25')
    for j in messages.json()['data']:
        deleted_messages.append({
            'Subject': j['Temat'],
            'Sender': j['Nadawca']['Name'],
            'Date': j['Data'],
            'Read': j['Nieprzeczytana'] == False,
            'Id': j['Id']
        })

    return received_messages, sent_messages, deleted_messages

def get_recipients(j):
    Recipients = []
    for x in j['Adresaci']:
        Recipients.append({
            'Name': x['Name'],
            'Read': x['Unreaded'] == False
        })
    return Recipients