const student_data_ = document.querySelector('#student_data_');

myStorage = window.sessionStorage;

const getStudentData = () => {
    document.querySelector('#content').innerHTML = 'Here is student data (in my imagination)';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/student_data', {
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

student_data_.addEventListener('click', getStudentData)