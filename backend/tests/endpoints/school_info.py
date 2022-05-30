from tests.checks.status_code import status_check
from tests.endpoints.login import client
def school_info_test(cookies, headers, student, school_id, host, symbol, ssl, fg):
    response = client.post(
        "/uonetplus-uczen/school-info",
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
        response.json()["school"]["name"]
        == "Publiczna szkoła Wulkanowego nr 1 w fakelog.cf"
    )
    assert response.json()["teachers"][0]["name"] == "Karolina Kowalska [AN]"