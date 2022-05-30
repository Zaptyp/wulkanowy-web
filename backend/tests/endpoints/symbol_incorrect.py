from tests.checks.status_code import status_check
from tests.endpoints.login import client
def symbol_incorrect_test(nick, password, host, symbol_invalid, ssl, headars, fg):
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
    status_check(response.status_code, response.json(), fg)
    #assert response.json() == {"detail": "Symbol is incorrect"}