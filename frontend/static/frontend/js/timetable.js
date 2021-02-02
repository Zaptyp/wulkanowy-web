const timetable_ = document.querySelector('#timetable_');

myStorage = window.sessionStorage;
week = 0

const getTimetable = (event) => {
    if (event.target.id == 'previous' || event.target.id == 'previous_i') {
        week -= 1 
    }
    else if (event.target.id == 'next' || event.target.id == 'next_i') {
        week += 1 
    }
    document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)<button id="previous" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="previous_i" >keyboard_arrow_left</i></button><button id="next" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="next_i" >keyboard_arrow_right</i></button>';
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