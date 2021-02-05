import React, { Component } from 'react';
import { render } from 'react-dom';

class AccountManager extends Component {
    constructor (props) {
        super(props)
        this.handleChangeStudent = this.handleChangeStudent.bind(this)
        var cookies_data = JSON.parse(sessionStorage.getItem('cookies_data'));
        var students = cookies_data.data.register_r.data
        students.forEach((student) => {
            console.log(student);
        });
    }

    state = {
        student: {}
    };

    handleChangeStudent = (event) => {
        this.setState({student: event.target.value})
    }

    render() {
        return (
            <div id="box">
                <h1>Dupa</h1>
            </div>
        );
    }
}

export default AccountManager;

const container = document.getElementById("AccountManager");
render(<AccountManager />, container);