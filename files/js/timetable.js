const timetable_ = document.querySelector('#timetable_');

const getTimetable = () => {
    document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)';
}

timetable_.addEventListener('click', getTimetable);