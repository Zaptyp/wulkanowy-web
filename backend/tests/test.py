from fastapi.testclient import TestClient
from main import app
import requests
from tests.endpoints import login, login_incorrect, login_with_incorrect_symbol, notes, grades, school_info, conferences, mobile_access_register, mobile_access_delete_registed, mobile_access_registed, github
from tests.checks import status_code
client = TestClient(app)
class fg:
    lightgreen = "\x1B[38;5;46m"
    orange = "\x1B[38;5;208m"
    red = "\x1B[38;5;160m"
    rs = "\033[0m"

# Settings for all tests
nick = "jan@fakelog.cf"
password = "jan123"
host = "fakelog.cf"
backuphost = "fakelog.tk"
symbol = "powiatwulkanowy"
ssl = "false"
# Weekly settings for tests
week_grades = "16"
# ID settings for tests
id_mobile_deleted = 1234
# Settings for test_login_incorrect and test_symbol_incorrect
nick_invalid = "jan@fakelog.cf"
password_invalid = "Jan321"
symbol_invalid = "warszawa"

def test_check_connection():
    if ssl == "true":
        check = requests.get(
            "https://fakelog.cf",
        )
    elif ssl == "false":
        check = requests.get(
            "http://fakelog.cf",
        )
    status_code.status_check(check.status_code, check.json, fg)
    if check.status_code == 503 or check.status_code == 521 or check.status_code == 522 or check.status_code == 525 or check.status_code == 526 or check.status_code == 429 or check.status_code == 408 or check.status_code == 500 or check.status_code == 502 or check.status_code == 504 or check.status_code == 111:
        global host
        host = backuphost
        print(fg.orange + "Main host unavailable. Changed to backup host" + fg.rs)


def test_login_correct():
    global cookies, headers, student, school_id
    cookies, headers, student, school_id = login.login_test(nick, password, host, symbol, ssl, fg)

def test_login_incorrect():
    login_incorrect.login_incorrect_test(nick_invalid, password_invalid, host, symbol, ssl, headers, fg)

def test_symbol_incorrect():
    login_with_incorrect_symbol.symbol_incorrect_test(nick_invalid, password_invalid, host, symbol, ssl, headers, fg)

def test_notes():
    notes.notes_test(cookies, headers, student, school_id, host, symbol, ssl, fg)

def test_grades():
    grades.grades_test(cookies, headers, student, school_id, host, symbol, ssl, week_grades, fg)

def test_school_info():
    school_info.school_info_test(cookies, headers, student, school_id, host, symbol, ssl, fg)

def test_conference():
    conferences.conference_test(cookies, headers, student, school_id, host, symbol, ssl, fg)

def test_mobile_access_registed():
    mobile_access_registed.mobile_access_registed_test(cookies, headers, student, school_id, host, symbol, ssl, fg)

def test_mobile_access_register():
    mobile_access_register.mobile_access_register_test(cookies, headers, student, school_id, host, symbol, ssl, fg)
    
def test_mobile_access_delete_registed():
    mobile_access_delete_registed.mobile_access_delete_registed_test(cookies, headers, student, school_id, host, symbol, ssl, id_mobile_deleted, fg)

def test_github_info():
    github.github_info_test(fg)
