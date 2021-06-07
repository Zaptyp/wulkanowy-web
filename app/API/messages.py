import requests
import json
import calendar
import time
import re
from .generate_cookies import autogenerate_cookies

def get_received_messages(register_id, students, oun, s, date, school_year, symbol):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    now = calendar.timegm(time.gmtime())

    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        received_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.tk/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        received_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return received_messages.json()

def get_sent_messages(register_id, students, oun, s, date, school_year, symbol):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    now = calendar.timegm(time.gmtime())

    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        sent_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.tk/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        sent_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetInboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return sent_messages.json()

def get_deleted_messages(register_id, students, oun, s, date, school_year, symbol):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    now = calendar.timegm(time.gmtime())
   
    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        deleted_messages = requests.get(f'http://uonetplus-uzytkownik.fakelog.tk/{symbol}/Wiadomosc.mvc/GetOutboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)
    else:
        deleted_messages = requests.get(f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}/Wiadomosc.mvc/GetOutboxMessages?_dc={now}&dataOd=&dataDo=&page=1&start=0&limit=25', headers=headers, cookies=s)

    return deleted_messages.json()

def get_recipients(register_id, students, oun, s, date, school_year, symbol):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        link = f'http://uonetplus-uzytkownik.fakelog.tk/{symbol}'
    else:
        link = f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}'

    get_jednostki = requests.get(f'{link}/NowaWiadomosc.mvc/GetJednostkiUzytkownika', headers=headers, cookies=s)
    id_jednostka = get_jednostki.json()['data'][0]['IdJednostkaSprawozdawcza']
    data = {
        "paramsVo":{"IdJednostkaSprawozdawcza":id_jednostka, 'Rola': 2}
    }
    get_addressee = requests.post(f'{link}/Adresaci.mvc/GetAddressee', headers=headers, cookies=s, json=data)

    return {'addressee': get_addressee.json(), 'unitId': id_jednostka}

def send_message(register_id, students, oun, s, date, school_year, symbol, send_data):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        link = f'http://uonetplus-uzytkownik.fakelog.tk/{symbol}'
    else:
        link = f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}'

    student_data = students['data'][0]['UczenNazwisko']+' '+students['data'][0]['UczenImie']

    sess = requests.Session()

    sess.cookies.update(s)
    sess.headers.update(headers)

    index = sess.get(link)

    antiForgeryToken = re.search("antiForgeryToken: '(.)*'", index.text)
    antiForgeryToken = antiForgeryToken.group()
    antiForgeryToken = antiForgeryToken.replace('antiForgeryToken: ', '').replace("'", "")

    appGuid = re.search("appGuid: '(.)*'", index.text)
    appGuid = appGuid.group()
    appGuid = appGuid.replace('appGuid: ', '').replace("'", "")

    sess.headers.update({
        'X-V-RequestVerificationToken': antiForgeryToken,
        'X-V-AppGuid': appGuid,
        'Content-Type': 'application/json',
        'TE': "Trailers"
    })

    payload = {
        "incomming": {
            "Id": 0,
            "Nieprzeczytane": 0,
            "Przeczytane": 0,
            "Nieprzeczytana": False,
            "FolderWiadomosci": 0,
            "WiadomoscPowitalna": False,
            "Data": None,
            "Tresc": send_data['content'],
            "Temat": send_data['subject'],
            "IdWiadomosci": 0,
            "HasZalaczniki": False,
            "Zalaczniki": "",
            "Adresaci": [
                {
                    "Id": send_data['data']['Id'],
                    "IdReceiver": "",
                    "Name": send_data['data']['Name'],
                    "Role": send_data['data']['Role'],
                    "UnitId": send_data['data']['UnitId'],
                    "IdLogin": send_data['data']['IdLogin'],
                    "PushWiadomosc": False,
                    "Hash": send_data['data']['Hash'],
                    "Date": None,
                    "IsMarked": False
                }
            ],
            "WyslijJako": student_data,
            "WiadomoscAdresatLogin": "",
            "IdWiadomoscAdresatLogin": None,
            "RolaNadawcy": 0,
            "NieprzeczytanePrzeczytane": "0/0",
            "NadawcaNazwa": "Brak nadawcy",
            "IdNadawca": 0,
            "AdresaciNazwa": "Brak adresata"
        }
    }

    send = sess.post(f'{link}/NowaWiadomosc.mvc/InsertWiadomosc', data=json.dumps(payload))

    return send.json()

def get_message_content(register_id, students, oun, s, date, school_year, symbol, message_id):
    with open('app/API/headers.json') as f:
        headers = json.load(f)

    if oun == 'http://uonetplus-uczen.fakelog.tk/powiatwulkanowy/123458':
        link = f'http://uonetplus-uzytkownik.fakelog.cf/{symbol}'
    else:
        link = f'https://uonetplus-uzytkownik.vulcan.net.pl/{symbol}'

    sess = requests.Session()

    sess.cookies.update(s)
    sess.headers.update(headers)

    index = sess.get(link)

    antiForgeryToken = re.search("antiForgeryToken: '(.)*'", index.text)
    antiForgeryToken = antiForgeryToken.group()
    antiForgeryToken = antiForgeryToken.replace('antiForgeryToken: ', '').replace("'", "")

    appGuid = re.search("appGuid: '(.)*'", index.text)
    appGuid = appGuid.group()
    appGuid = appGuid.replace('appGuid: ', '').replace("'", "")

    sess.headers.update({
        'X-V-RequestVerificationToken': antiForgeryToken,
        'X-V-AppGuid': appGuid
    })

    payload = {
        'messageId': message_id
    }

    content = sess.post(f'{link}/Wiadomosc.mvc/GetInboxMessageDetails', data=json.dumps(payload))

    if content.status_code != 200:
        while True:
            content = sess.post(f'{link}/Wiadomosc.mvc/GetInboxMessageDetails', data=json.dumps(payload))
            if content.status_code == 200:
                break

    return content.json()