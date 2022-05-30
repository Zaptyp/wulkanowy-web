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
    cookies = login.json()["vulcan_cookies"]
    headers = login.json()["students"][0]["headers"]
    student = login.json()["students"][0]["cookies"]
    school_id = login.json()["students"][0]["school_id"]
    status_check(login.status_code, login.json(), fg)
    assert login.json()["symbol"] == "powiatwulkanowy"
    assert login.json()["vulcan_cookies"]
    try:
        assert login.json()["host"] == "fakelog.cf"
    except:
        assert login.json()["host"] == "fakelog.tk"
    return cookies, headers, student, school_id