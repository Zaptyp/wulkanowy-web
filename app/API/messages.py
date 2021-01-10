import requests
import json
import calendar
import time

def get_received_messages(register_id, register_r, oun, s, date, school_year, symbol):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    now = calendar.timegm(time.gmtime())

    if oun == 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        received_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.cf/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        received_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return received_messages.json()

def get_sent_messages(register_id, register_r, oun, s, date, school_year, symbol):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    now = calendar.timegm(time.gmtime())

    if oun == 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        sent_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.cf/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        sent_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return sent_messages.json()

def get_deleted_messages(register_id, register_r, oun, s, date, school_year, symbol):
    headers = {
        'Accept-Encoding': 'gzip, deflate, br7',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        "User-Agent": "Wulkanowy-web :)"
    }

    now = calendar.timegm(time.gmtime())
   
    if oun == 'http://uonetplus-uczen.fakelog.cf/powiatwulkanowy/123458':
        deleted_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.cf/{symbol}/Wiadomosc.mvc/GetOutboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        deleted_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetOutboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return deleted_messages.json()
