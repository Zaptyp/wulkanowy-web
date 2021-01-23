/******/ (function() { // webpackBootstrap
/*!*************************************!*\
  !*** ./static/frontend/js/start.js ***!
  \*************************************/
var name_ = document.querySelector('#name');
var email_ = document.querySelector('#email');
myStorage = window.sessionStorage;

var studentName = function studentName() {
  var cookies_data = JSON.parse(sessionStorage.getItem('cookies_data'));
  name_.innerHTML = cookies_data['data']['register_r']['data'][0]['UczenImie'] + ' ' + cookies_data['data']['register_r']['data'][0]['UczenImie2'] + ' ' + cookies_data['data']['register_r']['data'][0]['UczenNazwisko'];
};

var studentEmail = function studentEmail() {
  email_.innerHTML = sessionStorage.getItem('email');
};

window.addEventListener('load', studentName);
window.addEventListener('load', studentEmail);
/******/ })()
;
//# sourceMappingURL=out-start.js.map