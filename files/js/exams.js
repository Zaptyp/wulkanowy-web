const exams_ = document.querySelector('#exams_');

const getExams = () => {
    document.querySelector('#content').innerHTML = 'Here is exams (in my imagination)';
}

exams_.addEventListener('click', getExams);