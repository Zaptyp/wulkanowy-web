import React, { Component } from 'react';
import clsx from 'clsx';
import ReactDOM from 'react-dom';
import { createStyles, makeStyles, useTheme, Theme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
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
import Forward from '@material-ui/icons/Forward';
import Send from '@material-ui/icons/Send';
import Delete from '@material-ui/icons/Delete';


const drawerWidth = 240;

const useStyles = makeStyles((theme: Theme) =>
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
            marginLeft: drawerWidth,
            width: `calc(100% - ${drawerWidth}px)`,
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
            width: drawerWidth,
            flexShrink: 0,
            whiteSpace: 'nowrap',
        },
        drawerOpen: {
            width: drawerWidth,
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

function MiniDrawer() {
    const classes = useStyles();
    const theme = useTheme();
    const [open, setOpen] = React.useState(false);

    const handleDrawerOpen = () => {
        setOpen(true);
    };

    const handleDrawerClose = () => {
        setOpen(false);
    };

    const iconsList = [<Dashboard />, <Filter6Icon />, <EventNote />, <Event />, <Class />, <DateRange />, <InsertChart />, <EmojiEvents />, <Devices />, <Business />, <AssignmentInd />];
    const iconsListMessages = [<InboxIcon />, <Forward />, <Send />, <Delete />]

    return (
        <div className={classes.root}>
            <CssBaseline />
            <AppBar id="bar"
                position="fixed"
                className={clsx(classes.appBar, {
                    [classes.appBarShift]: open,
                })}
            >
                <Toolbar>
                    <IconButton
                        color="inherit"
                        aria-label="open drawer"
                        onClick={handleDrawerOpen}
                        edge="start"
                        className={clsx(classes.menuButton, {
                            [classes.hide]: open,
                        })}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" noWrap>
                        Wulkanowy web early access insider preview pre-alpha pre-beta alpha beta release canditate v. 0.0.1
          </Typography>
                </Toolbar>
            </AppBar>
            <Drawer anchor="left"
                variant="permanent"
                className={clsx(classes.drawer, {
                    [classes.drawerOpen]: open,
                    [classes.drawerClose]: !open,
                })}
                classes={{
                    paper: clsx({
                        [classes.drawerOpen]: open,
                        [classes.drawerClose]: !open,
                    }),
                }}>
                <div className={classes.toolbar}>
                    <IconButton onClick={handleDrawerClose}>
                        {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
                    </IconButton>
                </div>
                <Divider />
                <List>
                    {['Start', 'Oceny', 'Plan Lekcji', 'Sprawdziany', 'Zadania Domowe', 'Frekwencja', 'Uczeń na Tle Klasy', 'Uwagi i Osiągnięcia', 'Dostęp Mobilny', 'Szkoła i Nauczyciele', 'Dane Ucznia'].map((text, index) => (
                        <ListItem button key={text}>
                            <ListItemIcon>{iconsList[index]}</ListItemIcon>
                            <ListItemText primary={text} />
                        </ListItem>
                    ))}
                </List>
                <Divider />
                <List>
                    {['Odebrane', 'Wysłane', 'Wyślij Wiadomość', 'Usunięte'].map((text, index) => (
                        <ListItem button key={text}>
                            <ListItemIcon>{iconsListMessages[index]}</ListItemIcon>
                            <ListItemText primary={text} />
                        </ListItem>
                    ))}
                </List>
            </Drawer>
            <main className={classes.content}>
                <div className={classes.toolbar} />
                <Typography paragraph>
                    Here is content (in my imagination)
                </Typography>
            </main>
        </div>
    );
}

class Content extends Component {
    render() {
        return (
            <MiniDrawer />
        )
    }
}

export default Content

const content = document.getElementById("content");
ReactDOM.render(<Content />, content);