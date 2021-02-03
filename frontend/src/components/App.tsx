import React, { Component } from "react";
import { render } from "react-dom";
import LoginForm from "./LoginForm";

class App extends Component {
    /*constructor(props) {
        super(props)
    }*/

    render() {
        return (
            <LoginForm />
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);