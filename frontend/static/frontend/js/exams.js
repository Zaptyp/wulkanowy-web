const exams_ = document.querySelector('#exams_');

myStorage = window.sessionStorage;
weekExams = 0

const getExams = (event) => {
    if (event.target.id == 'previous-exams' || event.target.id == 'previous-exams_i') {
        weekExams -= 1 
    }
    else if (event.target.id == 'next-exams' || event.target.id == 'next-exams_i') {
        weekExams += 1 
    }
    document.querySelector('#content').innerHTML = 'Here is exams (in my imagination)';
    document.querySelector('#content').innerHTML += '<button id="previous-exams" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="previous-exams_i">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button id="next-exams" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="next-exams_i">keyboard_arrow_right</i></button>';
    const left_exams_ = document.querySelector('#previous-exams');
    const right_exams_ = document.querySelector('#next-exams');
    left_exams_.addEventListener('click', getExams);
    right_exams_.addEventListener('click', getExams);
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/exams', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: JSON.stringify({"cookies": cookies_data, "week": weekExams})
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

exams_.addEventListener('click', getExams);