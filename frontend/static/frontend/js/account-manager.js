var cookies_data = JSON.parse(sessionStorage.getItem('cookies_data'));
students = cookies_data.data.register_r.data;

const displayData = () => {
    var primary = '';

    students.forEach((student) =>{
        if(student.UczenNazwisko+' '+student.UczenImie2+' '+student.UczenImie+' '+student.UczenSymbol != primary){
            primary = student.UczenNazwisko+' '+student.UczenImie2+' '+student.UczenImie+' '+student.UczenSymbol;
            document.querySelector("#content").innerHTML += `<p>
            <label>
            <input class="with-gap" name="group1" value='`+student.UczenPelnaNazwa+`' type="radio" checked />
            <span>`+student.UczenPelnaNazwa+`</span>
            </label>
           </p>`
        }
    })
    document.querySelector("#content").innerHTML += `<button id="button" class="waves-light waves-effect btn red darken-1">LOGIN</button>`
    const button_ = document.querySelector("#button")
    button_.addEventListener('click', logIn)
}

const logIn = () => {
    var ele = document.getElementsByName('group1'); 
              
    for(i = 0; i < ele.length; i++) { 
        if(ele[i].checked){
            studentName = ele[i].value;
            students.forEach((student) => {
                if(student.UczenPelnaNazwa == studentName){
                    cookies_data.data.register_r.data = [student]
                    sessionStorage.setItem('cookies_data', JSON.stringify(cookies_data));
                    window.location.href = '/content/'
                }
            })
        }
    }
}

window.addEventListener('load', displayData)