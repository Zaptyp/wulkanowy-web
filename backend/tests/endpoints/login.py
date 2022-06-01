from fastapi.testclient import TestClient
from tests.checks.status_code import status_check
from main import app

client = TestClient(app)


def login_test(nick, password, host, symbol, ssl, fg):
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
    cookies = login.json()[0]["session_data"]
    headers = login.json()[0]["schools"][0]["headers"]
    student = login.json()[0]["schools"][0]["students"][0]["cookies"]
    school_id = login.json()[0]["schools"][0]["id"]
    status_check(login.status_code, login.json(), fg)
    assert login.json()[0]["name"] == "powiatwulkanowy"
    assert login.json()[0]["session_data"]
    return cookies, headers, student, school_id
