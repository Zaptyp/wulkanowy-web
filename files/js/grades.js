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
        allGrades = data.data.Oceny

        allGrades.forEach((grade) => {
            content = document.getElementById("content")
            czastkowe = grade.OcenyCzastkowe
            //console.log(grade)
            czastkowe.forEach((czastkowa) => {
                const gradeDiv = document.createElement("div")
                gradeDiv.className = "grade"
                gradeDiv.innerHTML = `${czastkowa.Wpis}`
                if (czastkowa.Wpis == "6" || czastkowa.Wpis == "6-") gradeDiv.style.background = "#3dbbf5"
                else if (czastkowa.Wpis == "5" || czastkowa.Wpis == "5-" || czastkowa.Wpis == "5+") gradeDiv.style.background = "#4caf50"
                else if (czastkowa.Wpis == "4" || czastkowa.Wpis == "4-" || czastkowa.Wpis == "4+") gradeDiv.style.background = "#a0c431"
                else if (czastkowa.Wpis == "3" || czastkowa.Wpis == "3-" || czastkowa.Wpis == "3+") gradeDiv.style.background = "#ffb940"
                else if (czastkowa.Wpis == "2" || czastkowa.Wpis == "2-" || czastkowa.Wpis == "2+") gradeDiv.style.background = "#ff774d"
                else if (czastkowa.Wpis == "1" || czastkowa.Wpis == "1-") gradeDiv.style.background = "#d43f3f"
                else gradeDiv.style.background = "#607d8b"
                console.log(czastkowa)
                content.appendChild(gradeDiv)
            })
        })
    })
}

grades_.addEventListener('click', getGrades);