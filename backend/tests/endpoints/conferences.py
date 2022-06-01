from tests.checks.status_code import status_check
from tests.endpoints.login import client


def conference_test(cookies, headers, student, school_id, host, symbol, ssl, fg):
    response = client.post(
        "/uonetplus-uczen/conferences",
        headers={"Content-Type": "application/json"},
        json={
            "session_data": cookies,
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
        response.json()[0]["subject"]
        == "Podsumowanie I semestru - średnia klasy, oceny, frekwencja, zachowanie."
    )
    assert response.json()[1]["date"] == "06.09.2019 16:30"
