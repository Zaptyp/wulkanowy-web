import React, { Component } from 'react';

class AttendanceCom extends Component {
    constructor(props) {
        super(props);
        var cookies_data = sessionStorage.getItem('cookies_data');
        var csrfcookie_ = sessionStorage.getItem('csrfcookie');
        fetch('../api/attendance', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfcookie_
            },
            body: JSON.stringify({"cookies": cookies_data, "week": 0})
        }).then(response => response.json()).then(data => {
            console.log(data);
        })
    }

    render() {
        return (
            <p>Attendance</p>
        )
    }
}

export default AttendanceCom