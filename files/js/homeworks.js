const homeworks_ = document.querySelector('#homeworks_');

const getHomeworks = () => {
    document.querySelector('#content').innerHTML = 'Here is homeworks (in my imagination)';
}

homeworks_.addEventListener('click', getHomeworks);