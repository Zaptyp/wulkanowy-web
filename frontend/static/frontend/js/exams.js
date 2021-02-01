const exams_ = document.querySelector('#exams_');

myStorage = window.sessionStorage;

const getExams = () => {
    document.querySelector('#content').innerHTML = 'Here is exams (in my imagination)';
    document.querySelector('#content').innerHTML += '<button><i class="material-icons">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button><i class="material-icons">keyboard_arrow_right</i></button>';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/exams', {
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

exams_.addEventListener('click', getExams);