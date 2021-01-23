/******/ (function() { // webpackBootstrap
/*!*************************************!*\
  !*** ./static/frontend/js/exams.js ***!
  \*************************************/
var exams_ = document.querySelector('#exams_');
myStorage = window.sessionStorage;

var getExams = function getExams() {
  document.querySelector('#content').innerHTML = 'Here is exams (in my imagination)';
  cookies_data = sessionStorage.getItem('cookies_data');
  csrfcookie_ = sessionStorage.getItem('csrfcookie');
  fetch(url = '../api/exams', {
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

exams_.addEventListener('click', getExams);
/******/ })()
;
//# sourceMappingURL=out-exams.js.map