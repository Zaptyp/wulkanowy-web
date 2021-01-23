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
        content.innerHTML = ""
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
                        czastkowa.Kolor = "#3dbbf5"
                        gradeDiv.style.background = "#3dbbf5"
                        break;
                    case "5" || "5-" || "5+":
                        czastkowa.Kolor = "#4caf50"
                        gradeDiv.style.background = "#4caf50"
                        break;
                    case "4" || "4-" || "4+":
                        czastkowa.Kolor = "#a0c431"
                        gradeDiv.style.background = "#a0c431"
                        break;
                    case "3" || "3-" || "3+":
                        czastkowa.Kolor = "#ffb940"
                        gradeDiv.style.background = "#ffb940"
                        break;
                    case "2" || "2-" || "2+":
                        czastkowa.Kolor = "#ff774d"
                        gradeDiv.style.background = "#ff774d"
                        break;
                    case "1" || "1+":
                        czastkowa.Kolor = "#d43f3f"
                        gradeDiv.style.background = "#d43f3f"
                        break;
                    default:
                        czastkowa.Kolor = "#607d8b"
                        gradeDiv.style.background = "#607d8b"
                }
                const gradeModal = document.createElement("div")
                gradeModal.id = `${hash.MD5(czastkowa)}`
                gradeModal.classList = "modal"
                gradeModal.style.marginTop = "15rem"
                gradeModal.innerHTML = `<div class="modal-content">
                                            <h4>${grade.Przedmiot}</h4>
                                            <h5>${czastkowa.KodKolumny} - ${czastkowa.NazwaKolumny}</h5>
                                            
                                            <div style="float: right; background: ${czastkowa.Kolor}; width: 60px;  height: 70px; text-align: center;"><h1>${czastkowa.Wpis}</h1></div>
                                            
                                            <span class="teacher" style="font-size: 16px;">Nauczyciel</span>
                                            <p>${czastkowa.Nauczyciel}</p>
                                            
                                            <span class="weight" style="font-size: 16px;">Waga</span>
                                            <p>${czastkowa.Waga}</p>
                                            
                                            <span class="date" style="font-size: 16px;">Data</span>
                                            <p>${czastkowa.DataOceny}</p>
                                        </div>
                                        <div class="modal-footer">
                                            <a href="#!" class="modal-close${hash.MD5(czastkowa)} waves-effect waves-white btn materialize-red">Zamknij</a>
                                        </div>`
                gradeDiv.addEventListener('click', () => {
                    console.log(czastkowa)
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
