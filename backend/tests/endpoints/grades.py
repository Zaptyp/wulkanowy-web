from tests.checks.status_code import status_check
from tests.endpoints.login import client
#client = TestClient(app)
def grades_test(cookies, headars, student, school_id, host, symbol, ssl, week_grades, fg):
    response = client.post(
        "/uonetplus-uczen/grades",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {"okres": week_grades},
            "headers": headars,
        },
    )
    status_check(response.status_code, response.json(), fg)
    assert response.json()["subjects"][0]["grades"][0]["teacher"] == "Karolina Kowalska"
    assert response.json()["subjects"][0]["grades"][0]["symbol"] == "Akt"
    # assert response.json()['grades'][3]['grade'] == '4'