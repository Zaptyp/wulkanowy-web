import React, { Component } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Select from "@material-ui/core/Select";
import MenuItem from '@material-ui/core/MenuItem';

class LoginForm extends Component {
    urls = {
        Uonet: 'https://cufs.vulcan.net.pl/',
        Fakelog: 'http://cufs.fakelog.cf/',
    };
    state = {
        loginName: '',
        Password: '',
        Symbol: '',
        diaryUrl: ''
    };
    constructor(props) {
        super(props);
        this.handleChangeEmail = this.handleChangeEmail.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
        this.handleChangeSymbol = this.handleChangeSymbol.bind(this)
        this.handleChangeURL = this.handleChangeURL.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChangeEmail = (event) =>{    this.setState({loginName: event.target.value});  }
    handleChangePassword = (event) => {    this.setState({Password: event.target.value});  }
    handleChangeSymbol = (event) => {     this.setState({Symbol: event.target.value});    }
    handleChangeURL = (event) => {    this.setState({diaryUrl: event.target.value});  }
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
    handleSubmit = (event) => {
        fetch("api/login", {
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
                window.location.href = "/account-manager/";
            }
            else{
                document.querySelector('#error').innerHTML = 'Zła nazwa użytkownika, hasło lub symbol';
            }
        });
        event.preventDefault();
    }

    render() {
        return (
            <div id="box">
                <div id="box-content">
                    <form onSubmit={this.handleSubmit}>
                        <TextField value={this.state.loginName} onChange={this.handleChangeEmail} label="E-mail"/><br />
                        <TextField value={this.state.Password} onChange={this.handleChangePassword} label="Password" type="password"/><br />
                        <TextField value={this.state.Symbol} onChange={this.handleChangeSymbol} label="Symbol"/><br />
                        <Select id="url-select" autoWidth={true} onChange={this.handleChangeURL}>
                            <MenuItem value={this.urls.Uonet}>Vulcan UONET+</MenuItem>
                            <MenuItem value={this.urls.Fakelog}>Fakelog</MenuItem>
                        </Select><br />
                        <div id="error"></div>
                        <Button type="submit" id="button" variant="contained" size="large">Zaloguj</Button>
                    </form>
                </div>
            </div>
        );
    }
}

export default LoginForm;