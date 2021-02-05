import requests
import json
from .generate_cookies import autogenerate_cookies

def get_attendance(register_id, students, oun, s, date):
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    attendance_lessons = requests.post(oun+'/FrekwencjaStatystykiPrzedmioty.mvc/Get', headers=headers, cookies=cookies)
    attendance_json_id = attendance_lessons.json()['data'][0]['Id']
    attendance = requests.post(oun+'/Frekwencja.mvc/Get', headers=headers, cookies=cookies, json={'idTypWpisuFrekwencji': attendance_json_id, 'data': date})

    return [attendance.json(), attendance_lessons.json()]