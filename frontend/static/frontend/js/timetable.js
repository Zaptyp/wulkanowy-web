const timetable_ = document.querySelector('#timetable_');

myStorage = window.sessionStorage;
weekTimetable = 0

const getTimetable = (event) => {
    if (event.target.id == 'previous-timetable' || event.target.id == 'previous-timetable_i') {
        weekTimetable -= 1 
    }
    else if (event.target.id == 'next-timetable' || event.target.id == 'next-timetable_i') {
        weekTimetable += 1 
    }
    document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)';
    document.querySelector('#content').innerHTML += '<button id="previous-timetable" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="previous-timetable_i">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button id="next-timetable" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="next-timetable_i">keyboard_arrow_right</i></button>';
    const left_timetable_ = document.querySelector('#previous-timetable');
    const right_timetable_ = document.querySelector('#next-timetable');
    left_timetable_.addEventListener('click', getTimetable);
    right_timetable_.addEventListener('click', getTimetable);
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/timetable', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: JSON.stringify({"cookies": cookies_data, "week": weekTimetable})
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

timetable_.addEventListener('click', getTimetable);