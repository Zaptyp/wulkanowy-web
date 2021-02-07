import React, { Component } from 'react';

class NotesCom extends Component {
    constructor(props) {
        super(props);
        var cookies_data = sessionStorage.getItem('cookies_data');
        var csrfcookie_ = sessionStorage.getItem('csrfcookie');
        fetch('../api/notes', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfcookie_
            },
            body: cookies_data
        }).then(response => response.json()).then(data => {
            console.log(data);
        })
    }

    render() {
        return (
            <p>Notes</p>
        )
    }
}

export default NotesCom