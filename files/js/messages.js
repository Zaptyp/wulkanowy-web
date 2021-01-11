const received_ = document.querySelector('#received_');
const sent_ = document.querySelector('#sent_');
const deleted_ = document.querySelector('#deleted_');

const getReceivedMessages = () => {
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
        content = document.getElementById("content")
        console.log(data)
        wiadomosci = data.data

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

            console.log(tbody)

            wiadomoscRow = tbody.insertRow()

            temat = wiadomoscRow.insertCell()
            temat.innerText = wiadomosc.Temat
            wiadomoscRow.appendChild(temat)

            nadawca = wiadomoscRow.insertCell()
            nadawca.innerText = wiadomosc.Nadawca.Name
            wiadomoscRow.appendChild(nadawca)


            dataWyslania = wiadomoscRow.insertCell()
            dataWyslania.innerText = wiadomosc.Data
            wiadomoscRow.appendChild(dataWyslania)
        })
    })
}

const getSentMessages = () => {
    document.querySelector('#content').innerHTML = 'Here is sent messages (in my imagination)';
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
        console.log(data);
    })
}

const getDeletedMessages = () => {
    document.querySelector('#content').innerHTML = 'Here is deleted messages (in my imagination)';
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
        console.log(data);
    })
}


received_.addEventListener('click', getReceivedMessages);
sent_.addEventListener('click', getSentMessages);
deleted_.addEventListener('click', getDeletedMessages);