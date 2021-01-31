const name_ = document.querySelector('#name');
const email_ = document.querySelector('#email');

myStorage = window.sessionStorage;

const studentName = () => {
    const cookies_data = JSON.parse(sessionStorage.getItem('cookies_data'))
    name_.innerHTML = cookies_data['data']['students']['data'][0]['UczenImie']+' '+cookies_data['data']['students']['data'][0]['UczenImie2']+' '+cookies_data['data']['students']['data'][0]['UczenNazwisko']
};

const studentEmail = () => {
    email_.innerHTML = sessionStorage.getItem('email') 
};

window.addEventListener('load', studentName);
window.addEventListener('load', studentEmail);