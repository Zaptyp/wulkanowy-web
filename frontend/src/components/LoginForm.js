import React, { Component } from "react";
import TextField from "@material-ui/core/TextField"
import Button from "@material-ui/core/Button"

class LoginForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loginName: '',
            Password: '',
            Symbol: 'powiatwulkanowy',
            diaryUrl: 'http://cufs.fakelog.cf/'
        };
        this.handleChangeEmail = this.handleChangeEmail.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChangeEmail(event) {    this.setState({loginName: event.target.value});  }
    csrfcookie() {
        var cookieValue = null,
            name = 'csrftoken';
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };
    handleChangePassword(event) {    this.setState({Password: event.target.value});  }
    handleSubmit(event) {
        fetch("http://127.0.0.1:8000/api/login", {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': this.csrfcookie(),
            },
            body: JSON.stringify(this.state)
        }).then(response => response.json()).then(data => {
            if(data['success']){
                var myStorage = window.sessionStorage;
                sessionStorage.setItem('cookies_data', JSON.stringify(data));
                sessionStorage.setItem('csrfcookie', this.csrfcookie());
                sessionStorage.setItem('email', this.state.loginName);
                window.location.href = "/content/";
                console.log("Success!")
            }
            else{
                console.log("dupa")
            }
        });
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <TextField value={this.state.loginName} onChange={this.handleChangeEmail} variant="outlined" label="E-mail"/>
                <TextField value={this.state.Password} onChange={this.handleChangePassword} variant="outlined" label="Password" type="password"/>
                <Button type="submit" variant="contained" color="primary" size="large">Wyślij</Button>
            </form>
        );
    }
}

export default LoginForm;