from tests.checks.status_code import status_check
from tests.endpoints.login import client
def mobile_access_registed_test(cookies, headers, student, school_id, host, symbol, ssl, fg):
    response = client.post(
        "/uonetplus-uczen/mobile-access/get-registered-devices",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headers,
        },
    )
    status_check(response.status_code, response.json(), fg)
    assert (
        response.json()[0]["name"]
        == "To Be Filled By O.E.M.#To Be Filled By O.E.M. (Windows 8.1)"
    )
    assert response.json()[1]["id"] == 1234
