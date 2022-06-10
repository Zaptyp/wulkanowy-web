from tests.checks.status_code import status_check
from tests.routes.login import client

# client = TestClient(app)
def login_incorrect_test(
    nick_invalid, password_invalid, host, symbol, ssl, fg
):
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
    status_check(response.status_code, response.json(), fg)
    assert response.json() == {"detail": "incorrect_username_or_password"}
