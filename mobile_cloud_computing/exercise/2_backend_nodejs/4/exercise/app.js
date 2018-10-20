const express = require('express');
const mongoose = require('mongoose');
const path = require('path');
var cookieParser = require('cookie-parser');
var session = require('express-session');

var authRouter = require('./auth/AuthController');

var app = express();
const config = require('./db');

var configSecret = require('./config');
app.use(cookieParser());
app.use(session({
    secret: configSecret.secret,
    resave: false,
    saveUninitialized: false
}));

mongoose.connect(config.DB, { useNewUrlParser: true }).then(
    () => {
        console.log('Database is connected');
    },
    err => { console.log('Can not connect to the database' + err) }
);

//app.use('/', tasksRouter);
var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/', authRouter);

app.listen(3000)
module.exports = app;
