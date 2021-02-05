const homeworks_ = document.querySelector('#homeworks_');

myStorage = window.sessionStorage;
weekHomeworks = 0

const getHomeworks = (event) => {
    if (event.target.id == 'previous-homeworks' || event.target.id == 'previous-homeworks_i') {
        weekHomeworks -= 1 
    }
    else if (event.target.id == 'next-homeworks' || event.target.id == 'next-homeworks_i') {
        weekHomeworks += 1 
    }
    document.querySelector('#content').innerHTML = 'Here is homeworks (in my imagination)';
    document.querySelector('#content').innerHTML += '<button id="previous-homeworks" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="previous-homeworks_i">keyboard_arrow_left</i></button>';
    document.querySelector('#content').innerHTML += '<button id="next-homeworks" class="waves-light waves-effect btn red darken-1"><i class="material-icons" id="next-homeworks_i">keyboard_arrow_right</i></button>';
    const left_homeworks_ = document.querySelector('#previous-homeworks');
    const right_homeworks_ = document.querySelector('#next-homeworks');
    left_homeworks_.addEventListener('click', getHomeworks);
    right_homeworks_.addEventListener('click', getHomeworks);
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/homeworks', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: JSON.stringify({"cookies": cookies_data, "week": weekHomeworks})
    }).then(response => response.json()).then(data => {
        console.log(data);
    })
}

homeworks_.addEventListener('click', getHomeworks);