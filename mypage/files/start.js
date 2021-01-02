function grade_action(id) {
    var x = document.getElementById(id);
    var element = x.getElementsByTagName('li')[0];
    if(element.style.display == 'none'){
        element.style.display = 'block';
    }
    else if(element.style.display == 'block'){
        element.style.display = 'none';
    }
}

function change_message_content(id) {
    $.ajax({
        url: '/change_messages_content/',
        data: {
          'id': id
        },
        success: function(data) {
            document.querySelector('#messages_content').innerHTML = data;
        }
    });
}