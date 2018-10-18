var express = require('express');
var path = require('path');

var calcRouter = require('./routes/calc');
var vappuRotuer = require('./routes/vappu');
var imagesRouter = require('./routes/images')

var app = express();

app.use('/calc', calcRouter);
app.use('/vappu', vappuRotuer);
app.use('/images', imagesRouter)

app.listen(3000)
module.exports = app;
