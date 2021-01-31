const log_out_ = document.querySelector('#log_out_');

myStorage = window.sessionStorage;

const logOut = () => {
    fetch(url = '../api/log_out', {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        }
    }).then(response => response.json()).then(data => {
        sessionStorage.clear();
        console.log(data)
        window.location.href = '../'
    })
}

log_out_.addEventListener('click', logOut)