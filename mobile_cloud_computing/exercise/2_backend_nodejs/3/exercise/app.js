const express = require('express');
const mongoose = require('mongoose');
const path = require('path');

var tasksRouter = require('./routes/tasks');

var app = express();

// 
//

const config = require('./db');

mongoose.connect(config.DB, { useNewUrlParser: true }).then(
    () => {
        console.log('Database is connected');
    },
    err => { console.log('Can not connect to the database' + err) }
);

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

app.use('/', tasksRouter);

app.listen(3000)
module.exports = app;
