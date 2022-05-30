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
    headars = login.json()["students"][0]["headers"]
    student = login.json()["students"][0]["cookies"]
    school_id = login.json()["students"][0]["school_id"]
    #print(login.json())
    status_check(login.status_code, login.json(), fg)
    assert login.json()["symbol"] == "powiatwulkanowy"
    #assert login.json()["school_id"]
    assert login.json()["vulcan_cookies"]
    try:
        assert login.json()["host"] == "fakelog.cf"
    except:
        assert login.json()["host"] == "fakelog.tk"
    """
    if not cookies:
        errorcode = 1
        print("\nCookies output: ")
        print(login.json()["vulcan_cookies"])
        pytest.fail("No VULCAN cookies detected")
    elif not headars:
        errorcode = 2
        print("\nHeaders output: ")
        print(login.json()["students"][0]["headers"])
        pytest.fail("No headers detected")
    elif not student:
        errorcode = 3
        print("\nStudent output: ")
        print(login.json()["students"][0]["cookies"])
        pytest.fail("No student cookies detected")
    elif not school_id:
        errorcode = 4
        print("\nSchool ID output: ")
        print(login.json()["students"][0]["school_id"])
        pytest.fail("No school ID detected")
    """
    return cookies, headars, student, school_id