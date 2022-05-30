from tests.checks.status_code import status_check
from tests.endpoints.login import client
def mobile_access_delete_registed_test(cookies, headars, student, school_id, host, symbol, ssl, id_mobile_deleted, fg):
    response = client.post(
        "/uonetplus-uczen/mobile-access/delete-registered-device",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {"id": id_mobile_deleted},
            "headers": headars,
        },
    )
    status_check(response.status_code, response.json(), fg)
    # Nowa metoda testowania
    # if response.status_code == 404:
    #    print(response.json())
    # else:
    #    print("Test")
    assert response.json()["success"] == True
    # print(response.json())