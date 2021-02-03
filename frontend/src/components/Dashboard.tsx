import React, { Component } from "react";
import Drawer from "@material-ui/core/Drawer"
import List from "@material-ui/core/List"
import ListItem from "@material-ui/core/ListItem"
import ListItemIcon from "@material-ui/core/ListItemIcon"
import ListItemText from "@material-ui/core/ListItemText"
import Filter6Icon from '@material-ui/icons/Filter6';

class Dashboard extends Component {
    state = {
        cookies_data: sessionStorage.getItem('cookies_data'),
        csrfcookie: sessionStorage.getItem('csrfcookie'),
        data: {}
    }

    componentDidMount() {
        fetch("/api/dashboard", {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': this.state.csrfcookie
            },
            body: this.state.cookies_data
        }).then(response => response.json()).then(data => {
            console.log(data)
            this.state.data = data
        })
    }

    render() {
        return (
        <div>
            <Drawer variant="permanent" anchor="left" >
                <List>
                    <ListItem>
                        <ListItemIcon><Filter6Icon  /></ListItemIcon>
                        <ListItemText>Oceny</ListItemText>
                    </ListItem>
                </List>
            </Drawer>
        </div>
        )
    }
}

export default Dashboard