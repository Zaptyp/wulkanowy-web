/******/ (function() { // webpackBootstrap
/*!*********************************************!*\
  !*** ./static/frontend/js/mobile_access.js ***!
  \*********************************************/
var registered_ = document.querySelector('#mobile_access_');
myStorage = window.sessionStorage;

var getRegisteredDevices = function getRegisteredDevices() {
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
  }).then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    var register_device_ = document.querySelector('#register_device_');
    register_device_.addEventListener('click', registerDevice);
  });
};

var registerDevice = function registerDevice() {
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
  }).then(function (response) {
    return response.json();
  }).then(function (data) {
    console.log(data);
    document.querySelector('#register_device_data').innerHTML = data.data.QrCodeImage + '<br /> TOKEN:' + data.data.TokenKey + '<br /> PIN:' + data.data.PIN + '<br /> SYMBOL:' + data.data.CustomerGroup;
  });
};

registered_.addEventListener('click', getRegisteredDevices);
/******/ })()
;
//# sourceMappingURL=out-mobile_access.js.map