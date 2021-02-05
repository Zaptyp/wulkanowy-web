import React, { Component } from "react";
import { render } from 'react-dom';
import { Button, ListItemText, ListItemIcon, ListItem } from '@material-ui/core';
import { Drawer } from '@material-ui/core';
import Filter6Icon from '@material-ui/icons/Filter6';
import Dashboard from '@material-ui/icons/Dashboard';
import EventNote from '@material-ui/icons/EventNote';
import Event from '@material-ui/icons/Event';
import Class from '@material-ui/icons/Class';
import DateRange from '@material-ui/icons/DateRange';
import InsertChart from '@material-ui/icons/InsertChart';
import EmojiEvents from '@material-ui/icons/EmojiEvents';
import Devices from '@material-ui/icons/Devices';
import Business from '@material-ui/icons/Business'
import AssignmentInd from '@material-ui/icons/AssignmentInd';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import Divider from '@material-ui/core/Divider';
import Forward from '@material-ui/icons/Forward';
import Send from '@material-ui/icons/Send';
import Delete from '@material-ui/icons/Delete';

class Content extends Component {
    iconsList = [<Dashboard />, <Filter6Icon />, <EventNote />, <Event />, <Class />, <DateRange />, <InsertChart />, <EmojiEvents />, <Devices />, <Business />, <AssignmentInd />];
    iconsListMessages = [<InboxIcon />, <Forward />, <Send />, <Delete />]
    render() {
        return (
            <div>
                <Drawer anchor="left" variant="permanent">
                {['Start', 'Oceny', 'Plan Lekcji', 'Sprawdziany', 'Zadania Domowe', 'Frekwencja', 'Uczeń na Tle Klasy', 'Uwagi i Osiągnięcia', 'Dostęp Mobilny', 'Szkoła i Nauczyciele', 'Dane Ucznia'].map((text, index) => (
                    <ListItem button key={text}>
                    <ListItemIcon>{this.iconsList[index]}</ListItemIcon>
                    <ListItemText primary={text} />
                    </ListItem>
                ))}
                <Divider />
                {['Odebrane', 'Wysłane', 'Wyślij Wiadomość', 'Usunięte'].map((text, index) => (
                    <ListItem button key={text}>
                    <ListItemIcon>{this.iconsListMessages[index]}</ListItemIcon>
                    <ListItemText primary={text} />
                    </ListItem>
                ))}
                </Drawer>
            </div>
        )
    }
};

export default Content;

const content = document.getElementById("content");
render(<Content />, content);