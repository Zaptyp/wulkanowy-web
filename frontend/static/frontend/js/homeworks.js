const homeworks_ = document.querySelector('#homeworks_');

myStorage = window.sessionStorage;

const getHomeworks = () => {
    document.querySelector('#content').innerHTML = 'Here is homeworks (in my imagination)';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/homeworks', {
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

homeworks_.addEventListener('click', getHomeworks);