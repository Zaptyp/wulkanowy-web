/******/ (function() { // webpackBootstrap
/*!******************************************!*\
  !*** ./static/frontend/js/attendance.js ***!
  \******************************************/
var attendance_ = document.querySelector('#attendance_');
myStorage = window.sessionStorage;

var getAttendance = function getAttendance() {
  document.querySelector('#content').innerHTML = 'Here is attendance (in my imagination)';
  cookies_data = sessionStorage.getItem('cookies_data');
  csrfcookie_ = sessionStorage.getItem('csrfcookie');
  fetch(url = '../api/attendance', {
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
  });
};

attendance_.addEventListener('click', getAttendance);
/******/ })()
;
//# sourceMappingURL=out-attedance.js.map