import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import clsx from 'clsx';
import { createStyles, makeStyles, useTheme, Theme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
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
    drawerWidth = 240;
    iconsList = [<Dashboard />, <Filter6Icon />, <EventNote />, <Event />, <Class />, <DateRange />, <InsertChart />, <EmojiEvents />, <Devices />, <Business />, <AssignmentInd />];
    iconsListMessages = [<InboxIcon />, <Forward />, <Send />, <Delete />]

    useStyles = makeStyles((theme: Theme) =>
        createStyles({
            root: {
                display: 'flex',
            },
            appBar: {
                zIndex: theme.zIndex.drawer + 1,
                transition: theme.transitions.create(['width', 'margin'], {
                    easing: theme.transitions.easing.sharp,
                    duration: theme.transitions.duration.leavingScreen,
                }),
            },
            appBarShift: {
                marginLeft: this.drawerWidth,
                width: `calc(100% - ${this.drawerWidth}px)`,
                transition: theme.transitions.create(['width', 'margin'], {
                    easing: theme.transitions.easing.sharp,
                    duration: theme.transitions.duration.enteringScreen,
                }),
            },
            menuButton: {
                marginRight: 36,
            },
            hide: {
                display: 'none',
            },
            drawer: {
                width: this.drawerWidth,
                flexShrink: 0,
                whiteSpace: 'nowrap',
            },
            drawerOpen: {
                width: this.drawerWidth,
                transition: theme.transitions.create('width', {
                    easing: theme.transitions.easing.sharp,
                    duration: theme.transitions.duration.enteringScreen,
                }),
            },
            drawerClose: {
                transition: theme.transitions.create('width', {
                    easing: theme.transitions.easing.sharp,
                    duration: theme.transitions.duration.leavingScreen,
                }),
                overflowX: 'hidden',
                width: theme.spacing(7) + 1,
                [theme.breakpoints.up('sm')]: {
                    width: theme.spacing(9) + 1,
                },
            },
            toolbar: {
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'flex-end',
                padding: theme.spacing(0, 1),
                // necessary for content to be below app bar
                ...theme.mixins.toolbar,
            },
            content: {
                flexGrow: 1,
                padding: theme.spacing(3),
            },
        }),
    );

        classes = this.useStyles();
        theme = useTheme();

        state = {
            open: false,
            setOpen: false
        }

        handleDrawerOpen = () => {
            this.setState({setOpen: true});
        };

        handleDrawerClose = () => {
            this.setState({setOpen: false});
        };

    constructor(props) {
        super(props)
    };

    render() {
        return (
            <div className={this.classes.root}>
            <CssBaseline />
            <AppBar
                position="fixed"
                className={clsx(this.classes.appBar, {
                    [this.classes.appBarShift]: open,
                })}
            >
                <Toolbar>
                    <IconButton
                        color="inherit"
                        aria-label="open drawer"
                        onClick={this.handleDrawerOpen}
                        edge="start"
                        className={clsx(this.classes.menuButton, {
                            [this.classes.hide]: open,
                        })}
                    >
                        <MenuIcon />
                    </IconButton>
                </Toolbar>
            </AppBar>
            <Drawer anchor="left" variant="permanent" className={clsx(this.classes.drawer, {
                [this.classes.drawerOpen]: open,
                [this.classes.drawerClose]: !open,
            })}
                classes={{
                    paper: clsx({
                        [this.classes.drawerOpen]: open,
                        [this.classes.drawerClose]: !open,
                    }),
                }}
            >
                <div className={this.classes.toolbar}>
                    <IconButton onClick={this.handleDrawerClose}>
                        {this.theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
                    </IconButton>
                </div>
                <Divider />
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
ReactDOM.render(<Content />, content);