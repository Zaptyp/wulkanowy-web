const registered_ = document.querySelector('#mobile_access_');

myStorage = window.sessionStorage;

const getRegisteredDevices = () => {
    document.querySelector('#content').innerHTML = '<button id="register_device_">ZAJERESTRUJ URZĄDZENIE</button><div id="register_device_data"></div><br />Here is registered mobile devices (in my imagination)';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/mobile/registered', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data);
        const register_device_ = document.querySelector('#register_device_');
        register_device_.addEventListener('click', registerDevice);
    })
}

const registerDevice = () => {
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/mobile/register', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data);
        document.querySelector('#register_device_data').innerHTML = data.data.QrCodeImage+'<br /> TOKEN:'+data.data.TokenKey+'<br /> PIN:'+data.data.PIN+'<br /> SYMBOL:'+data.data.CustomerGroup;
    })
}

registered_.addEventListener('click', getRegisteredDevices);