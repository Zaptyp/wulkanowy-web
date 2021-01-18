const received_ = document.querySelector('#received_');
const sent_ = document.querySelector('#sent_');
const deleted_ = document.querySelector('#deleted_');
const content = document.getElementById("content");
const send_ = document.querySelector('#send_')
var hash = require('object-hash');

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
            "              <th>Adresat</th>\n" +
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
            nadawca.innerHTML = `<span>${wiadomosc.Adresaci[0]}</span>`
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

const getAddressee = () => {
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/messages/recipients', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data);
        document.querySelector('#content').innerHTML = `
        <form action="javascript:void(0);">
        <div class="input-field">
        <select id='recipients' style='display: inline !important;'>
        </select>
        </div>
        <div class="input-field">
          <input required="" placeholder="Temat" id="subject" class="input-field">
        </div>
        <div class="input-field">
          <input required="" placeholder="Treść" id="message-content" class="input-field">
        </div>
        <button id="button" class="waves-light waves-effect btn red darken-1">WYŚLIJ</button>
        </form>`
        data.addressee.data.forEach((recipient) => {
            const recipient_hash = `${hash.MD5(recipient)}`
            document.querySelector('#recipients').insertAdjacentHTML('beforeend', '<option value="'+recipient_hash+'">'+recipient.Name+'</option>');
            sessionStorage.setItem(recipient_hash, JSON.stringify(recipient));
            const button_ = document.querySelector('#button');
            button_.addEventListener('click', sendMessage);
        })
    })
}

const sendMessage = () => {
    const recipient_hash_ = document.querySelector('#recipients').value;
    const subject_ = document.querySelector('#subject').value;
    const content_ = document.querySelector('#message-content').value;
    const recipient_ = JSON.parse(sessionStorage.getItem(recipient_hash_));
    if(subject_ != '' && content_ != ''){
        cookies_data = sessionStorage.getItem('cookies_data');
        csrfcookie_ = sessionStorage.getItem('csrfcookie');
        send_data = {
            'cookies_data': cookies_data,
            'data': recipient_,
            'subject': subject_,
            'content': content_
        }
        fetch(url = '../api/messages/send', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfcookie_
              },
            body: JSON.stringify(send_data)
        }).then(response => response.json()).then(data => {
            console.log(data)
        })
    }
    
}


received_.addEventListener('click', getReceivedMessages);
sent_.addEventListener('click', getSentMessages);
deleted_.addEventListener('click', getDeletedMessages);
send_.addEventListener('click', getAddressee);