const stats_ = document.querySelector('#stats_');

myStorage = window.sessionStorage;

const showMenu = () => {
    document.querySelector('#content').innerHTML = '<button id="partial" class="waves-light waves-effect btn red darken-1">OCENY CZĄSTKOWE</button>';
    document.querySelector('#content').innerHTML += '<button id="year" class="waves-light waves-effect btn red darken-1">OCENY ROCZNE</button>';
    const partial_ = document.querySelector('#partial');
    const year_ = document.querySelector('#year');
    partial_.addEventListener('click', getPartial);
    year_.addEventListener('click', getYear);
}

const getPartial = () => {
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/stats/partial', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

const getYear = () => {
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/stats/year', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

stats_.addEventListener('click', showMenu);