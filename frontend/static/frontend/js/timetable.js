const timetable_ = document.querySelector('#timetable_');

myStorage = window.sessionStorage;
week = 0

const getTimetable = (event) => {
    if (event.target.id == 'previous') {
        week -= 1 
    }
    else if (event.target.id == 'next') {
        week += 1 
    }
    else {
        week = week
    }
    document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)<button id="previous" class="waves-light waves-effect btn red darken-1"><i class="material-icons">keyboard_arrow_left</i></button><button id="next" class="waves-light waves-effect btn red darken-1"><i class="material-icons">keyboard_arrow_right</i></button>';
    const left_ = document.querySelector('#previous');
    const right_ = document.querySelector('#next');
    left_.addEventListener('click', getTimetable);
    right_.addEventListener('click', getTimetable);
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/timetable', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: JSON.stringify({"cookies": cookies_data, "week": week})
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

timetable_.addEventListener('click', getTimetable);