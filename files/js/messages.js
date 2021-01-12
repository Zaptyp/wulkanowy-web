const received_ = document.querySelector('#received_');
const sent_ = document.querySelector('#sent_');
const deleted_ = document.querySelector('#deleted_');
const content = document.getElementById("content")

const getReceivedMessages = () => {
    content.innerHTML = ""
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/messages/received', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        const wiadomosci = data.data

        table = document.createElement("table")
        table.className = "striped"
        table.innerHTML = "<thead>\n" +
            "          <tr>\n" +
            "              <th>Temat</th>\n" +
            "              <th>Nadawca</th>\n" +
            "              <th>Data</th>\n" +
            "          </tr>\n" +
            "        </thead>" +
            "        <tbody>" +
            "                " +
            "        </tbody>"

        content.append(table)

        wiadomosci.forEach((wiadomosc) => {
            const tbody = document.getElementsByTagName("tbody")[0]

            wiadomoscRow = tbody.insertRow()

            temat = wiadomoscRow.insertCell()
            temat.innerHTML = `<span id="${wiadomosc.Id}">${wiadomosc.Temat}</span>`
            wiadomoscRow.appendChild(temat)

            nadawca = wiadomoscRow.insertCell()
            nadawca.innerHTML = `<span>${wiadomosc.Nadawca.Name}</span>`
            wiadomoscRow.appendChild(nadawca)


            dataWyslania = wiadomoscRow.insertCell()
            dataWyslania.innerHTML = `<span>${wiadomosc.Data}</span>`
            wiadomoscRow.appendChild(dataWyslania)
        })
    })
}

const getSentMessages = () => {
    content.innerHTML = ""
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/messages/sent', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        const wiadomosci = data.data // haha spaghetti code goes brrr

        table = document.createElement("table")
        table.className = "striped"
        table.innerHTML = "<thead>\n" +
            "          <tr>\n" +
            "              <th>Temat</th>\n" +
            "              <th>Nadawca</th>\n" +
            "              <th>Data</th>\n" +
            "          </tr>\n" +
            "        </thead>" +
            "        <tbody>" +
            "                " +
            "        </tbody>"

        content.append(table)

        wiadomosci.forEach((wiadomosc) => {
            const tbody = document.getElementsByTagName("tbody")[0]

            wiadomoscRow = tbody.insertRow()

            temat = wiadomoscRow.insertCell()
            temat.innerHTML = `<span id="${wiadomosc.Id}">${wiadomosc.Temat}</span>`
            wiadomoscRow.appendChild(temat)

            nadawca = wiadomoscRow.insertCell()
            nadawca.innerHTML = `<span>${wiadomosc.Nadawca.Name}</span>`
            wiadomoscRow.appendChild(nadawca)


            dataWyslania = wiadomoscRow.insertCell()
            dataWyslania.innerHTML = `<span>${wiadomosc.Data}</span>`
            wiadomoscRow.appendChild(dataWyslania)
        })
    })
}

const getDeletedMessages = () => {
    content.innerHTML = ""
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/messages/deleted', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        const wiadomosci = data.data

        table = document.createElement("table")
        table.className = "striped"
        table.innerHTML = "<thead>\n" +
            "          <tr>\n" +
            "              <th>Temat</th>\n" +
            "              <th>Nadawca</th>\n" +
            "              <th>Data</th>\n" +
            "          </tr>\n" +
            "        </thead>" +
            "        <tbody>" +
            "                " +
            "        </tbody>"

        content.append(table)

        wiadomosci.forEach((wiadomosc) => {
            const tbody = document.getElementsByTagName("tbody")[0]

            wiadomoscRow = tbody.insertRow()

            temat = wiadomoscRow.insertCell()
            temat.innerHTML = `<span id="${wiadomosc.Id}">${wiadomosc.Temat}</span>`
            wiadomoscRow.appendChild(temat)

            nadawca = wiadomoscRow.insertCell()
            nadawca.innerHTML = `<span>${wiadomosc.Nadawca.Name}</span>`
            wiadomoscRow.appendChild(nadawca)


            dataWyslania = wiadomoscRow.insertCell()
            dataWyslania.innerHTML = `<span>${wiadomosc.Data}</span>`
            wiadomoscRow.appendChild(dataWyslania)
        })
    })
}


received_.addEventListener('click', getReceivedMessages);
sent_.addEventListener('click', getSentMessages);
deleted_.addEventListener('click', getDeletedMessages);