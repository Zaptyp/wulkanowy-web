// TODO: do Marcina z przyszłości od Marcina z przeszłości: MARCIN SKOŃCZ OCENY!!!
var hash = require('object-hash');

const grades_ = document.querySelector('#grades_');

myStorage = window.sessionStorage;

const getGrades = () => {
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/grades', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
          },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        const allGrades = data.data.Oceny
        const content = document.getElementById("content")
        const container = document.getElementsByClassName("gradeModals")[0]

        allGrades.forEach((grade) => {
            const czastkowe = grade.OcenyCzastkowe

            czastkowe.forEach((czastkowa) => {
                const gradeDiv = document.createElement("div")
                gradeDiv.classList = "grade modal-trigger"
                gradeDiv.dataset.target = `${hash.MD5(czastkowa)}`
                gradeDiv.innerHTML = `${czastkowa.Wpis}`

                switch (czastkowa.Wpis) {
                    case "6" || "6-":
                        gradeDiv.style.background = "#3dbbf5"
                        break;
                    case "5" || "5-" || "5+":
                        gradeDiv.style.background = "#4caf50"
                        break;
                    case "4" || "4-" || "4+":
                        gradeDiv.style.background = "#a0c431"
                        break;
                    case "3" || "3-" || "3+":
                        gradeDiv.style.background = "#ffb940"
                        break;
                    case "2" || "2-" || "2+":
                        gradeDiv.style.background = "#ff774d"
                        break;
                    case "1" || "1+":
                        gradeDiv.style.background = "#d43f3f"
                        break;
                    default:
                        gradeDiv.style.background = "#607d8b"
                }
                const gradeModal = document.createElement("div")
                gradeModal.id = `${hash.MD5(czastkowa)}`
                gradeModal.classList = "modal"
                gradeModal.innerHTML = `<div class="modal-content">
                                            <h4>${grade.Przedmiot}</h4>
                                            <p>A bunch of text</p>
                                        </div>
                                        <div class="modal-footer">
                                            <a href="#!" class="modal-close${hash.MD5(czastkowa)} waves-effect waves-green btn-flat">Agree</a>
                                        </div>`
                gradeDiv.addEventListener('click', () => {
                    console.log(`Nauczyciel: ${czastkowa.Nauczyciel}, Waga: ${czastkowa.Waga}, Data: ${czastkowa.DataOceny}, Przedmiot: ${grade.Przedmiot}`)
                    gradeModal.style.display = 'block'
                })

               container.append(gradeModal)

                document.getElementsByClassName(`modal-close${hash.MD5(czastkowa)}`)[0].addEventListener('click', () => {
                    gradeModal.style.display = 'none'
                })

               content.append(gradeDiv)
            })
        })
    })
}

grades_.addEventListener('click', getGrades);