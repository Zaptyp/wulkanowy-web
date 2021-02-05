const attendance_ = document.querySelector('#attendance_');

myStorage = window.sessionStorage;
weekAttendance = 0

const getAttendance = (event) => {
    if (event.target.id == 'previous-attendance' || event.target.id == 'previous-attendance_i') {
        weekAttendance -= 1 
    }
    else if (event.target.id == 'next-attendance' || event.target.id == 'next-attendance_i') {
        weekAttendance += 1 
    }
    document.querySelector('#content').innerHTML = 'Here is attendance (in my imagination)';
    document.querySelector('#content').innerHTML += '<button id="previous-attendance" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="previous-attendance_i">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button id="next-attendance" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="next-attendance_i">keyboard_arrow_right</i></button>';
    const left_attendance_ = document.querySelector('#previous-attendance');
    const right_attendance_ = document.querySelector('#next-attendance');
    left_attendance_.addEventListener('click', getAttendance);
    right_attendance_.addEventListener('click', getAttendance);
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/attendance', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: JSON.stringify({"cookies": cookies_data, "week": weekAttendance})
    }).then(response => response.json()).then(data => {
        console.log(data);
    })
}

attendance_.addEventListener('click', getAttendance);