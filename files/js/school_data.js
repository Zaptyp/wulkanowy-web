const school_data = document.querySelector('#school_data_');

myStorage = window.sessionStorage;

const getSchoolData = () => {
    document.querySelector('#content').innerHTML = 'Here is school data (in my imagination)';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/school_data', {
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

school_data_.addEventListener('click', getSchoolData);