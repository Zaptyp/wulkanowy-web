const messages_ = document.querySelector('#messages_');

const getMessages = () => {
    document.querySelector('#content').innerHTML = 'Here is messages (in my imagination)';
}

messages_.addEventListener('click', getMessages);