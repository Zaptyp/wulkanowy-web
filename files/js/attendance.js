const attendance_ = document.querySelector('#attendance_');

const getAttendance = () => {
    document.querySelector('#content').innerHTML = 'Here is attendance (in my imagination)';
}

attendance_.addEventListener('click', getAttendance);