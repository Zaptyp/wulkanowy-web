/******/ (function() { // webpackBootstrap
/*!*****************************************!*\
  !*** ./static/frontend/js/timetable.js ***!
  \*****************************************/
var timetable_ = document.querySelector('#timetable_');
myStorage = window.sessionStorage;

var getTimetable = function getTimetable() {
  document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)';
  cookies_data = sessionStorage.getItem('cookies_data');
  csrfcookie_ = sessionStorage.getItem('csrfcookie');
  fetch(url = '../api/timetable', {
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

timetable_.addEventListener('click', getTimetable);
/******/ })()
;
//# sourceMappingURL=out-timetable.js.map