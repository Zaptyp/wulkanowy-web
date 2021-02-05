import React, { Component } from "react";
import { render } from 'react-dom'
import Dashboard from "./Dashboard";

class Content extends Component {
    render() {
        return (
            <Dashboard/>
        )
    }
}

export default Content

const content = document.getElementById("content")
render(<Content />, content)