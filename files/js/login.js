const button = document.querySelector('#button');

const login = () => {
    const loginName = document.querySelector('#id_loginName').value;
    const Password = document.querySelector('#id_Password').value;
    const symbol = document.querySelector('#id_Symbol').value;
    const diary = document.querySelector('#id_diary').value;
    if(loginName != '' && Password != '' && symbol != ''){
        switch(diary){
            case 'Fakelog':
                var diaryUrl = 'http://cufs.fakelog.cf/';
                break;

            case 'Vulcan UONET+':
                var diaryUrl = 'https://cufs.vulcan.net.pl/';
                break;
        }
        data = {
                'loginName': loginName,
                'Password': Password,
                'Symbol': symbol,
                'diaryUrl': diaryUrl
            }
        fetch(url = 'api/login', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfcookie()
              },
            body: JSON.stringify(data)
        }).then(response => response.json()).then(data => {
            if(data['success']){
                myStorage = window.sessionStorage;
                sessionStorage.setItem('cookies_data', JSON.stringify(data));
                sessionStorage.setItem('csrfcookie', csrfcookie());
                sessionStorage.setItem('email', document.querySelector('#id_loginName').value);
                window.location.href = "/content/";
            }
            else{
                document.querySelector('#error').innerHTML = 'Nieprawidłowy login, hasło lub symbol';
            }
        });
    }
};

var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

button.addEventListener('click', login);