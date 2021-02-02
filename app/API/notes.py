import json
import requests

def get_notes(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    notes = requests.post(oun+'/UwagiIOsiagniecia.mvc/Get', headers=headers, cookies=cookies)

    return notes.json()