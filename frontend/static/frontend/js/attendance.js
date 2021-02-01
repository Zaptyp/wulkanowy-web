const attendance_ = document.querySelector('#attendance_');

myStorage = window.sessionStorage;

const getAttendance = () => {
    document.querySelector('#content').innerHTML = 'Here is attendance (in my imagination)';
    document.querySelector('#content').innerHTML += '<button><i class="material-icons">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button><i class="material-icons">keyboard_arrow_right</i></button>';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/attendance', {
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

attendance_.addEventListener('click', getAttendance);