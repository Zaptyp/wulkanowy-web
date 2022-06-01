from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.requests import Request
from app import models, paths
import requests
from datetime import datetime
from cryptography.fernet import Fernet
import ast

router = APIRouter()


@router.post("/uonetplus-uczen/notes")
def get_notes(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.UWAGIIOSIAGNIECIA_GET
    response = get_response(data, path, session_cookies)
    notes = []
    for note in response.json()["data"]["Uwagi"]:
        note = models.Note(
            date=datetime.fromisoformat(note["DataWpisu"]).strftime("%d.%m.%Y %H:%M"),
            teacher=note["Nauczyciel"],
            category=note["Kategoria"],
            content=note["TrescUwagi"],
            points=note["Punkty"],
            show_points=int(note["PokazPunkty"]),
            category_type=bool(note["KategoriaTyp"]),
        )
        notes.append(note)
    notes_and_achievements = models.NotesAndAchievements(
        notes=notes, achievements=response.json()["data"]["Osiagniecia"]
    )
    return notes_and_achievements

@router.post("/uonetplus-uczen/school-info")
def get_school_info(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.SZKOLAINAUCZYCIELE_GET
    response = get_response(data, path, session_cookies)
    teachers = []
    school = models.School(
        name=response.json()["data"]["Szkola"]["Nazwa"],
        address=response.json()["data"]["Szkola"]["Adres"],
        contact=response.json()["data"]["Szkola"]["Kontakt"],
        headmaster=response.json()["data"]["Szkola"]["Dyrektor"],
        pedagogue=response.json()["data"]["Szkola"]["Pedagog"],
    )
    for teacher in response.json()["data"]["Nauczyciele"]:
        teacher = models.Teacher(name=teacher["Nauczyciel"], subject=teacher["Nazwa"])
        teachers.append(teacher)
    school_info = models.SchoolInfo(school=school, teachers=teachers)
    return school_info

@router.post("/uonetplus-uczen/conferences")
def get_conferences(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.ZEBRANIA_GET
    response = get_response(data, path, session_cookies)
    conferences = []
    for conference in response.json()["data"]:
        split = conference["Tytul"].split(", ")
        title = ", ".join(split[2:])
        date = datetime.strptime(split[1].replace(" godzina", ""), "%d.%m.%Y %H:%M")
        conference = models.Conference(
            title=title,
            subject=conference["TematZebrania"],
            agenda=conference["Agenda"],
            present_on_conference=conference["ObecniNaZebraniu"],
            online=conference["ZebranieOnline"],
            id=conference["Id"],
            date=date.strftime("%d.%m.%Y %H:%M"),
        )
        conferences.append(conference)
    return conferences

@router.post("/uonetplus-uczen/grades")
def get_grades(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.OCENY_GET
    response = get_response(data, path, session_cookies)
    subjects = []
    descriptive_grades = []
    for subject in response.json()["data"]["Oceny"]:
        subject_grades = []
        for grade in subject["OcenyCzastkowe"]:
            grade = models.Grade(
                entry=grade["Wpis"],
                color=grade["KolorOceny"],
                symbol=grade["KodKolumny"],
                description=grade["NazwaKolumny"],
                weight_value=grade["Waga"],
                date=grade["DataOceny"],
                teacher=grade["Nauczyciel"],
            )
            subject_grades.append(grade)
        subject = models.Subject(
            name=subject["Przedmiot"],
            visible_subject=subject["WidocznyPrzedmiot"],
            position=subject["Pozycja"],
            average=subject["Srednia"],
            proposed_grade=subject["ProponowanaOcenaRoczna"],
            final_grade=subject["OcenaRoczna"],
            proposed_points=subject["ProponowanaOcenaRocznaPunkty"],
            final_points=subject["OcenaRocznaPunkty"],
            grades=subject_grades,
        )
        subjects.append(subject)
    for descriptive_grade in response.json()["data"]["OcenyOpisowe"]:
        descriptive_grade = models.DescriptiveGrade(
            subject=descriptive_grade["NazwaPrzedmiotu"],
            description=descriptive_grade["Opis"],
            is_religion_or_ethics=descriptive_grade["IsReligiaEtyka"],
        )
        descriptive_grades.append(descriptive_grade)
    grades = models.Grades(
        is_average=response.json()["data"]["IsSrednia"],
        is_points=response.json()["data"]["IsPunkty"],
        subjects=subjects,
        descriptive_grades=descriptive_grades,
    )
    return grades

@router.post("/uonetplus-uczen/mobile-access/get-registered-devices")
def get_registered_devices(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.ZAREJESTROWANEURZADZENIA_GET
    response = get_response(data, path, session_cookies)
    registered_devices = []
    for device in response.json()["data"]:
        device = models.Device(
            id=device["Id"],
            name=device["NazwaUrzadzenia"],
            create_date=datetime.fromisoformat(device["DataUtworzenia"]).strftime("%d.%m.%Y %H:%M"),
        )
        registered_devices.append(device)
    return registered_devices

@router.post("/uonetplus-uczen/mobile-access/register-device")
def get_register_device_token(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.REJESTRACJAURZADZENIATOKEN_GET
    response = get_response(data, path, session_cookies)
    token_response = models.TokenResponse(
        token=response.json()["data"]["TokenKey"],
        symbol=response.json()["data"]["CustomerGroup"],
        pin=response.json()["data"]["PIN"],
        qr_code_image=response.json()["data"]["QrCodeImage"],
    )
    return token_response

@router.post("/uonetplus-uczen/mobile-access/delete-registered-device")
def get_register_device_token(data: models.UonetPlusUczen, request: Request):
    session_cookies = decrypt_session_data(request, data.session_data)
    path = paths.UCZEN.ZAREJESTROWANEURZADZENIA_DELETE
    response = get_response(data, path, session_cookies)
    return response.json()

def build_url(subd: str = None, host: str = None, path: str = None, ssl: bool = True, **kwargs) -> str:
    if ssl:
        url = "https://"
    else:
        url = "http://"
    if subd:
        url += subd + "."
    url += host
    if path:
        url += path
    if not kwargs.get("symbol"):
        kwargs["symbol"] = "Default"

    for k in kwargs:
        url = url.replace(f"{{{k.upper()}}}", str(kwargs[k]))
    return url

def get_response(data, path, session_cookies) -> requests.models.Response:
    session = requests.Session()
    session_cookies.update(data.student)
    url = build_url(
        subd="uonetplus-uczen",
        path=path,
        symbol=data.symbol,
        host=data.host,
        schoolid=data.school_id,
        ssl=data.ssl,
    )
    response = session.post(
        url=url,
        headers=data.headers,
        json=data.payload,
        cookies=session_cookies,
    )
    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="uonet_error")
    if (
        "uonet_error"
        in response.text
    ):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="uonet_error"
        )
    return response

def decrypt_session_data(request, session_data: str) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        if request.session.get('session_key'):
            session_key = request.session.get('session_key')
        else:
            raise credentials_exception
        fernet = Fernet(bytes(session_key, "utf-8"))
        session_data = ast.literal_eval(fernet.decrypt(session_data.encode("utf-8")).decode("utf-8"))
        if session_data['expire'] != None and session_data['session_cookies'] != None:
            if datetime.timestamp(datetime.utcnow())*1000 > float(session_data['expire']):
                raise credentials_exception
        else:
            raise credentials_exception
        return dict(session_data['session_cookies'])
    except:
        raise credentials_exception
