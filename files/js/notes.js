const notes_ = document.querySelector('#notes_');

const getNotes = () => {
    document.querySelector('#content').innerHTML = 'Here is notes (in my imagination)';
}

notes_.addEventListener('click', getNotes);