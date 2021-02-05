import React, { Component } from 'react';
import { render } from 'react-dom';
import { Radio } from '@material-ui/core';
import { FormControlLabel } from '@material-ui/core'
import { RadioGroup } from '@material-ui/core';
import { Button } from "@material-ui/core";

class AccountManager extends Component {
    state = {
        cookies_data: null,
        student: {},
        students: [],
        studentsCounter: []
    };

    constructor (props) {
        super(props)
        this.handleChangeStudent = this.handleChangeStudent.bind(this)
        var cookies_data = JSON.parse(sessionStorage.getItem('cookies_data'));
        var students = cookies_data.data.register_r.data;
        this.state.cookies_data = cookies_data;
        this.state.students =  students;
        students.forEach((student) => {
            var studentName = student.UczenPelnaNazwa
            this.state.studentsCounter.push(<FormControlLabel value={studentName} label={studentName} control={<Radio />} />, <br />)})
    };

    handleChangeStudent = (event) => {
        this.setState({student: event.target.value});
    };

    handleSubmit = () => {
        this.state.students.forEach((student) => {
            if (student.UczenPelnaNazwa == this.state.student) {
                console.log(this.state.cookies_data)
                this.state.cookies_data.data.register_r.data = [student];
                sessionStorage.setItem('cookies_data', JSON.stringify(this.state.cookies_data));
                window.location.href = '/content/';
            }
        });
    };

    render() {
        return (
            <div id="box" onChange={this.handleChangeStudent}>
                <h1>Wybierz Ucznia</h1>
                <RadioGroup>
                    <div id="group">
                        {this.state.studentsCounter}
                    </div>
                </RadioGroup>
                <Button type="submit" id="button" variant="contained" size="large" onClick={this.handleSubmit}>Wybierz</Button>
            </div>
        );
    }
}

export default AccountManager;

const container = document.getElementById("AccountManager");
render(<AccountManager />, container);