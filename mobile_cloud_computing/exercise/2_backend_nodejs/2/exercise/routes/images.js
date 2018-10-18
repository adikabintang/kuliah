var express = require('express');
var router = express.Router();

router.get('/', function (req, res, next) {
    var fs = require('fs');
    const request = require('request');
    var resultArray = []
    var anjing = "";
    var counterArray = 0;

    var obj = JSON.parse(fs.readFileSync('exercise/images.json', 'utf8'));
    console.log(obj);
    for (var i = 0; i < obj.length; i++) {
        console.log("url: " + obj[i].url);
        var requestedUrl = 'http://localhost:80' + obj[i].url; 
        request
            .get(requestedUrl)
            .on('complete', function(response) {
                var filename = response.headers['content-disposition'].split('=')[1].split(';')[0];
                var fileSize = (parseFloat(response.headers['content-length']) / 1000).toString() + " Kb";
                var fileType = response.headers['content-type'].split('/')[1].toUpperCase();
                resultArray.push({name: filename, type: fileType, size: fileSize});
                console.log(filename)
                console.log(fileSize)
                console.log(fileType)
                console.error(filename)
                console.error(fileSize)
                console.error(fileType)
                counterArray++;
                if (counterArray == obj.length) {
                    res.send(resultArray);
                }
            });            
    }
});

module.exports = router;
