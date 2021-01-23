/******/ (function() { // webpackBootstrap
/*!*************************************!*\
  !*** ./static/frontend/js/notes.js ***!
  \*************************************/
var notes_ = document.querySelector('#notes_');
content = document.getElementById("content");
myStorage = window.sessionStorage;

var getNotes = function getNotes() {
  content.innerHTML = "";
  cookies_data = sessionStorage.getItem('cookies_data');
  csrfcookie_ = sessionStorage.getItem('csrfcookie');
  fetch(url = '../api/notes', {
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
    var uwagi = data.data.Uwagi;
    var osiagniecia = data.data.Osiagniecia;
    console.log(data);
    var uwagiList = document.createElement("ul");
    uwagiList.id = "notesList";
    content.append(uwagiList);
    uwagi.forEach(function (uwaga) {
      uwagaElement = document.createElement("li");
      uwagaElement.innerHTML = "<div class=\"noteElement\"><h6 style=\"display:block; margin-top: -5px;\">".concat(uwaga.Kategoria, "</h6><span style=\"display:block; float: right; margin-top: -25px; font-size: 13px;\">").concat(uwaga.Nauczyciel, "</span><span style=\"display:block; width: 50%; font-size: 12px;\">").concat(uwaga.TrescUwagi, "</span><span style=\"float:right; font-size: 20px; margin-top: -20px; font-weight: 700;\">").concat(uwaga.Punkty, "</span></div>");
      uwagiList.append(uwagaElement);
    });
    osiagniecia.forEach(function (osiagniecie) {
      osiagniecieElement = document.createElement("li");
      osiagniecieElement.innerHTML = "<div class=\"achievementElement\"><span>".concat(osiagniecie, "</span></div>");
      uwagiList.append(osiagniecieElement);
    });
  });
};

notes_.addEventListener('click', getNotes);
/******/ })()
;
//# sourceMappingURL=out-notes.js.map