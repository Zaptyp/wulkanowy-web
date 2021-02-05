import json

def autogenerate_cookies(students, s):
    cookies = s
    cookies.update({
        "biezacyRokSzkolny": f"{students['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{students['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{students['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyUczen": f"{students['data'][0]['IdUczen']}"
    })

    return cookies 