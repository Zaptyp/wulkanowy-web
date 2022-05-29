from fastapi.testclient import TestClient
from main import app
import pytest
import json
import requests
client = TestClient(app)

host = "fakelog.cf"
backuphost = "fakelog.tk"
symbol = "powiatwulkanowy"
ssl = False
# Login
nick = "jan@fakelog.cf"
password = "jan123"
# Grades
week_grades = "16"
# Mobile access
id_mobile_deleted = 1234
# Invalid data
nick_invalid = "jan@fakelog.cf"
password_invalid = "Jan321"
symbol_invalid = "warszawa"

def test_check_connection():
    if ssl:
        check = requests.get(
            "https://fakelog.cf",
        )
    else:
        check = requests.get(
            "http://fakelog.cf",
        )
    if check.status_code == 503 or check.status_code == 521 or check.status_code == 522 or check.status_code == 525 or check.status_code == 526 or check.status_code == 429 or check.status_code == 408 or check.status_code == 500 or check.status_code == 502 or check.status_code == 504 or check.status_code == 111:
        global host
        host = backuphost
        print("Main host unavailable. Changed to backup host")

def test_login_correct():
    global login_data
    login = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": nick,
            "password": password,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
        },
    )
    login_data = login.json()
    assert login.status_code == 200
    assert login.json()["symbol"] == symbol
    assert login.json()["host"] == host

def test_login_incorrect():
    response = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": nick_invalid,
            "password": password_invalid,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
        },
    )
    assert response.status_code == 403
    assert response.json() == {'detail': 'Username or password is incorrect'}

def test_symbol_incorrect():
    response = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": nick,
            "password": password,
            "host": host,
            "symbol": symbol_invalid,
            "ssl": ssl,
        },
    )
    assert response.status_code == 403
    assert response.json() == {"detail": "Symbol is incorrect"}

def test_notes():
    response = get_uonetplus_uczen_response(
        "/uonetplus-uczen/notes", {}
    )
    assert response.status_code == 200
    assert response.json()["notes"][0]["teacher"] == "Karolina Kowalska [AN]"
    assert response.json()["notes"][1]["content"] == "+ 20p za udział w Konkursie Języka Angielskiego"

def test_grades():
    response = get_uonetplus_uczen_response("/uonetplus-uczen/grades", {"okres": week_grades})
    assert response.status_code == 200
    assert response.json()["subjects"][0]["grades"][0]["teacher"] == "Karolina Kowalska"
    assert response.json()["subjects"][0]["grades"][0]["symbol"] == "Akt"

def test_school_info():
    response = get_uonetplus_uczen_response("/uonetplus-uczen/school-info", {})
    assert response.status_code == 200
    assert (
        response.json()["school"]["name"]
        == "Publiczna szkoła Wulkanowego nr 1 w fakelog.cf"
    )
    assert response.json()["teachers"][0]["name"] == "Karolina Kowalska [AN]"

def test_conferences():
    response = get_uonetplus_uczen_response("/uonetplus-uczen/conferences", {})
    assert response.status_code == 200
    assert (
        response.json()[0]["subject"]
        == "Podsumowanie I semestru - średnia klasy, oceny, frekwencja, zachowanie."
    )
    assert response.json()[1]["date"] == "06.09.2019 16:30"

def test_mobile_access_registed():
    response = get_uonetplus_uczen_response("/uonetplus-uczen/mobile-access/get-registered-devices", {})
    assert response.status_code == 200
    assert (
        response.json()[0]["name"]
        == "To Be Filled By O.E.M.#To Be Filled By O.E.M. (Windows 8.1)"
    )
    assert response.json()[1]["id"] == 1234

def test_mobile_access_register():
    response = get_uonetplus_uczen_response("/uonetplus-uczen/mobile-access/register-device", {})
    assert response.status_code == 200
    assert response.json()["pin"] == "999999"
    assert response.json()["qr_code_image"]

def test_mobile_access_delete_registed():
    response = get_uonetplus_uczen_response(
        "/uonetplus-uczen/mobile-access/delete-registered-device",
        {"id": id_mobile_deleted}
    )
    assert response.status_code == 200
    assert response.json()["success"] == True

def get_uonetplus_uczen_response(url: str, json: dict):
    response = client.post(
        url,
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": login_data["vulcan_cookies"],
            "student": login_data["students"][0]["cookies"],
            "school_id": login_data["students"][0]["school_id"],
            "host": login_data["host"],
            "symbol": login_data["students"][0]["school_symbol"],
            "ssl": login_data["ssl"],
            "json": json,
            "headers": login_data["students"][0]["headers"],
        },
    )
    return response
