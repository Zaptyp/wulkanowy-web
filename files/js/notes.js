const notes_ = document.querySelector('#notes_');
content = document.getElementById("content")

myStorage = window.sessionStorage;

const getNotes = () => {
    content.innerHTML = ""
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/notes', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        const uwagi = data.data.Uwagi
        const osiagniecia = data.data.Osiagniecia
        console.log(data);

        const uwagiList = document.createElement("ul")
        uwagiList.id = "notesList"
        content.append(uwagiList)

        uwagi.forEach((uwaga) => {
            uwagaElement = document.createElement("li")
            uwagaElement.innerHTML = `<div class="noteElement"><h6 style="display:block; margin-top: -5px;">${uwaga.Kategoria}</h6><span style="display:block; float: right; margin-top: -25px; font-size: 13px;">${uwaga.Nauczyciel}</span><span style="display:block; width: 50%; font-size: 12px;">${uwaga.TrescUwagi}</span><span style="float:right; font-size: 20px; margin-top: -20px; font-weight: 700;">${uwaga.Punkty}</span></div>`
            uwagiList.append(uwagaElement)
        })

        osiagniecia.forEach((osiagniecie) => {
            osiagniecieElement = document.createElement("li")
            osiagniecieElement.innerHTML = `<div class="achievementElement"><span>${osiagniecie}</span></div>`
            uwagiList.append(osiagniecieElement)
        })
    })
}

notes_.addEventListener('click', getNotes);