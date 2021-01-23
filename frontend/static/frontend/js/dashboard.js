const start_ = document.querySelector('#dashboard_');

const getDashboard = () => {
    document.querySelector('#content').innerHTML = 'Dashboard';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/dashboard', {
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

window.addEventListener('load', getDashboard);
start_.addEventListener('click', getDashboard);