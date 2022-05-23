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
    session = requests.Session()
    cers = send_credentials(data.username, data.password, data.symbol, data.host, data.ssl, session)
    students = get_students(data.symbol, data.host, data.ssl, cers, session)
    cookies = get_cookies(data.ssl, data.host, data.symbol, session, students, response)

    return cookies


def send_credentials(username: str, password: str, symbol: str, host: str, ssl: bool, session):
    realm = build_url(subd="uonetplus", host=host, ssl=ssl)
    url = build_url(
        subd="cufs",
        host=host,
        path=paths.CUFS.START,
        realm=quote(quote(realm, safe=""), safe=""),
        symbol=symbol,
        ssl=ssl,
    )
    payload = {"LoginName": username, "Password": password}
    try:
        page = session.post(url, payload)
        if page.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="invalid_host_or_ssl"
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid_host_or_ssl"
        )
    soup = BeautifulSoup(page.text, "lxml")
    error_tags = soup.select(".ErrorMessage, #ErrorTextLabel, #loginArea #errorText")
    for error_tag in error_tags:
        msg = re.sub(r"\s+", " ", error_tag.text).strip()
        if msg:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="incorrect_username_or_password"
            )
    wa: str = soup.select_one('input[name="wa"]')["value"]
    wresult: str = soup.select_one('input[name="wresult"]')["value"]
    wctx_tag = soup.select_one('input[name="wctx"]')
    wctx: str = wctx_tag["value"] if wctx_tag else None
    cers = {"wa": wa, "wresult": wresult, "wctx": wctx}

    return cers


def build_url(subd: str = None, host: str = None, path: str = None, ssl: bool = True, **kwargs):
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


def get_cookies(ssl: bool, host: str, symbol: str, session, students, response):
    key = Fernet.generate_key().decode("utf-8")
    fernet = Fernet(bytes(key, "utf-8"))
    vulcan_cookies = session.cookies.get_dict()
    cookies = fernet.encrypt(str(vulcan_cookies).encode("utf-8"))
    response.set_cookie(key="key", value=key, max_age=1200)
    data = {
        "students": students,
        "vulcan_cookies": cookies,
        "symbol": symbol,
        "host": host,
        "ssl": ssl,
    }

    return data


def get_students(symbol: str, host: str, ssl: bool, cers, session):
    students = []
    url = build_url(subd="uonetplus", path=paths.UONETPLUS.START, symbol=symbol, host=host, ssl=ssl)
    crtr = session.post(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
        },
        data=cers,
    )
    if not "nie został zarejestrowany" in crtr.text:
        soup = BeautifulSoup(crtr.text, "lxml")
        schools = soup.select('.panel.linkownia.pracownik.klient a[href*="uonetplus-uczen"]')
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
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="incorrect_symbol")
    return students


def get_script_param(text: str, param: str, default: str = None) -> str:
    m = re.search(f"{param}: '(.+?)'", text)
    return m.group(1) if m else default
