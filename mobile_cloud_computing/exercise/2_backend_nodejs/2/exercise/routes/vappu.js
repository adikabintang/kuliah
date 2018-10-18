var express = require('express');
var router = express.Router();

router.get('/gettime', function(req, res, next) {
  var yearNow = new Date().getFullYear();
  var vappuThisYear = new Date(yearNow, 4, 1); // month starts from 0
  console.log("vappu this year: " + vappuThisYear)
  var remainingSec = 0;
  
  // testing
  var c = new Date(2018, 5, 5, 18, 23)
  var v = new Date(2019, 4, 1)

  var p = v - c
  console.log("---> " + p)

  // testing
  
  var currentEpochSec = new Date().getTime();
  if (vappuThisYear > currentEpochSec) {
    remainingSec = vappuThisYear - currentEpochSec;
    console.log("next vappu is in this year")
  } else {
    var nextVappu = new Date((yearNow + 1), 4, 1);
    remainingSec = nextVappu - currentEpochSec;
    console.log("next vappu is in next year")
  }

  res.send({seconds: parseInt(remainingSec / 1000)});
});

module.exports = router;
