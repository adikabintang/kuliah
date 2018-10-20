var express = require('express');
const request = require('request');
const latex = require('node-latex');
const path = require('path');
const fs = require('fs');
var router = express.Router();

router.get('/', function(req, res, next) {
    var urlDownload = req.query.url;
    var folderPath = path.join(__dirname, '..', 'files');

    request.get(urlDownload).on('complete', function(response) {
        const input = fs.createReadStream(folderPath + '/sample.tex');
        const output = fs.createWriteStream(folderPath + '/final.pdf');
        const pdf = latex(input);

        pdf.pipe(output)
        pdf.on('error', function(err) {
            console.error("error creating pdf: " + err.message);
            res.json({status: "failure"});
        });
        pdf.on('finish', function() {
            res.json({status: "success"});
        });
    }).pipe(fs.createWriteStream(folderPath + '/sample.tex'));

});

module.exports = router;