import json
import requests
from .generate_cookies import autogenerate_cookies

def get_student_data(register_id, students, oun, s):
    
    cookies = autogenerate_cookies(students, s)

    with open('app/API/headers.json') as f:
        headers = json.load(f)

    student_data = requests.post(f'{oun}/Uczen.mvc/Get', headers=headers, cookies=cookies)

    return student_data.json()