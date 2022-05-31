from fastapi import APIRouter, HTTPException, Response
from starlette import status
from bs4 import BeautifulSoup
from urllib.parse import quote
from datetime import datetime
from cryptography.fernet import Fernet
import requests
import re
from app import models, paths

router = APIRouter()


@router.post("/login")
def login(data: models.Login, response: Response):
    session: requests.sessions.session = requests.Session()
    cert: dict = send_credentials(
        data.username, data.password, data.host, data.symbol, data.ssl, session)
    students: list[models.Student] = get_students(
        data.host, data.symbol, data.ssl, cert, session)
    session_cookies: str = encrypt_session_cookies(session, response)
    data = {
        "students": students,
        "session_cookies": session_cookies,
        "host": data.host,
        "ssl": data.ssl
    }

    return data

def send_credentials(username: str, password: str, host: str, symbol: str, ssl: bool, session: requests.sessions.Session) -> dict:
    realm = build_url(subd="uonetplus", host=host, ssl=ssl)
    url = build_url(
        subd="cufs",
        host=host,
        path=paths.CUFS.START,
        realm=quote(quote(realm, safe=""), safe=""),
        symbol=symbol,
        ssl=ssl,
    )
    credentials = {"LoginName": username, "Password": password}
    credentials_response = session.post(url=url, data=credentials)
    check_errors(credentials_response.text)
    cert = create_cert(credentials_response.text)
    return cert

def check_errors(credentials_response: str):
    soup = BeautifulSoup(credentials_response, "lxml")
    error_tag = soup.select_one(
        ".ErrorMessage, #ErrorTextLabel, #loginArea #errorText")
    if error_tag:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="incorrect_username_or_password"
        )

def create_cert(credentials_response: str) -> dict:
    soup = BeautifulSoup(credentials_response, "lxml")
    wa: str = soup.select_one('input[name="wa"]')["value"]
    wresult: str = soup.select_one('input[name="wresult"]')["value"]
    wctx_tag = soup.select_one('input[name="wctx"]')
    wctx: str = wctx_tag["value"] if wctx_tag else None
    cert = {"wa": wa, "wresult": wresult, "wctx": wctx}
    return cert

def build_url(subd: str = None, host: str = None, path: str = None, ssl: bool = True, **kwargs) -> str:
    if ssl:
        url = "https://"
    else:
        url = "http://"
    if subd:
        url += subd + "."
    url += str(host)
    if path:
        url += path
    if not kwargs.get("symbol"):
        kwargs["symbol"] = "Deflaut"

    for k in kwargs:
        url = url.replace(f"{{{k.upper()}}}", str(kwargs[k]))
    return url

def encrypt_session_cookies(session: requests.sessions.Session, response) -> str:
    key = Fernet.generate_key().decode("utf8")
    fernet = Fernet(bytes(key, "utf-8"))
    session_cookies = session.cookies.get_dict()
    session_cookies = fernet.encrypt(str(session_cookies).encode("utf-8"))
    response.set_cookie(key="key", value=key, max_age=1200)
    return session_cookies

def send_cert(host: str, symbol: str, ssl: bool, cert: dict, session: requests.sessions.Session) -> requests.models.Response:
    url = build_url(subd="uonetplus", path=paths.UONETPLUS.START,
                    symbol=symbol, host=host, ssl=ssl)
    cert_response = session.post(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
        },
        data=cert,
    )
    if "nie został zarejestrowany" in cert_response.text:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="incorrect_symbol"
        )
    return cert_response

def get_students(host: str, symbol: str, ssl: bool, cert: dict, session: requests.sessions.Session) -> list[models.Student]:
    students = []
    cert_response = send_cert(host, symbol, ssl, cert, session)
    soup = BeautifulSoup(cert_response.text, "lxml")
    schools = soup.select(
        '.panel.linkownia.pracownik.klient a[href*="uonetplus-uczen"]')
    for school in schools:
        school_id = school["href"].split("/")[4]
        url = build_url(
            subd="uonetplus-uczen",
            path=paths.UCZEN.START,
            symbol=symbol,
            host=host,
            schoolid=school_id,
            ssl=ssl,
        )
        page = session.get(url)
        school_name = get_script_param(page.text, "organizationName")
        anti_forgery_token = get_script_param(page.text, "antiForgeryToken")
        app_guid = get_script_param(page.text, "appGuid")
        version = get_script_param(page.text, "version")
        url = build_url(
            subd="uonetplus-uczen",
            path=paths.UCZEN.UCZENDZIENNIK_GET,
            symbol=symbol,
            host=host,
            schoolid=school_id,
            ssl=ssl,
        )
        students_response = session.post(url)
        for student in students_response.json()["data"]:
            semesters = []
            headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "X-V-AppVersion": version,
                "X-V-AppGuid": app_guid,
                "X-V-RequestVerificationToken": anti_forgery_token,
            }
            for semester in student["Okresy"]:
                semester = models.Semester(
                    number=semester["NumerOkresu"],
                    level=semester["Poziom"],
                    start=datetime.fromisoformat(semester["DataOd"]),
                    end=datetime.fromisoformat(semester["DataDo"]),
                    class_id=semester["IdOddzial"],
                    unit_id=semester["IdJednostkaSprawozdawcza"],
                    current=semester["IsLastOkres"],
                    id=semester["Id"],
                )
                semesters.append(semester)
            student = models.Student(
                id=student["Id"],
                student_id=student["IdUczen"],
                student_name=student["UczenImie"],
                student_second_name=student["UczenImie2"],
                student_surname=student["UczenNazwisko"],
                is_register=student["IsDziennik"],
                register_id=student["IdDziennik"],
                kindergarten_register_id=student["IdPrzedszkoleDziennik"],
                level=student["Poziom"],
                symbol=student["Symbol"],
                name=student["Nazwa"],
                year=student["DziennikRokSzkolny"],
                start=datetime.fromisoformat(student["DziennikDataOd"]),
                end=datetime.fromisoformat(student["DziennikDataDo"]),
                full_name=student["UczenPelnaNazwa"],
                school_id=school_id,
                school_symbol=symbol,
                school_name=school_name,
                cookies={
                    "idBiezacyDziennik": str(student["IdDziennik"]),
                    "idBiezacyUczen": str(student["IdUczen"]),
                    "idBiezacyDziennikPrzedszkole": str(student["IdPrzedszkoleDziennik"]),
                    "biezacyRokSzkolny": str(student["DziennikRokSzkolny"]),
                },
                headers=headers,
                semesters=semesters,
            )
            students.append(student)
    return students

def get_script_param(text: str, param: str, default: str = None) -> str:
    m = re.search(f"{param}: '(.+?)'", text)
    return m.group(1) if m else default