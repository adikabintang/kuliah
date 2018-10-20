var express = require('express');
var path = require('path');

var indexRouter = require('./routes/index');

var app = express();

app.use('/', indexRouter);

// app.listen(3000)
module.exports = app;
