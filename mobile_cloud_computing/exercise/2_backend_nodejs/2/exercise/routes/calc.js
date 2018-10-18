var express = require('express');
var router = express.Router();

function sanitizeQuery(req, res) {
  var first = req.query.first;
  var second  = req.query.second;

  if (first === undefined && second === undefined) {
    res.status(400);
    res.json({message: "Missing both parameters"});
    return false;
  }

  if (first === undefined) {
    res.status(400);
    res.json({message: "Missing first required parameter"});
    return false;
  }

  if (second === undefined) {
    res.status(400);
    res.json({message: "Missing second required parameter"});
    return false;
  }

  if (isNaN(parseFloat(first)) && isNaN(parseFloat(second))) {
    res.status(400);
    res.json({message: "Both parameters are not numbers"});
    return false;
  }

  if (isNaN(parseFloat(first))) {
    res.status(400);
    res.json({message: "The first parameter is not a number"});
    return false;
  }

  if (isNaN(parseFloat(second))) {
    res.status(400);
    res.json({message: "The second parameter is not a number"});
    return false;
  }

  res.status(200)
  return true;
}

// router.get is for subpath
// app.get is for path
// https://stackoverflow.com/questions/27227650/difference-between-app-use-and-router-use-in-express
router.get('/add', function(req, res, next) {
  var first = req.query.first;
  var second  = req.query.second;
  var isValid = sanitizeQuery(req, res);
  if (isValid) {
    var addResult = parseFloat(first) + parseFloat(second);
    res.json({result: addResult.toFixed(3).toString()});
  }

  res.end();
});

router.get('/sub', function(req, res, next) {
  var first = req.query.first;
  var second  = req.query.second;
  var isValid = sanitizeQuery(req, res);
  if (isValid) {
    var subResult = parseFloat(first) - parseFloat(second);
    res.json({result: subResult.toFixed(3).toString()});
  }

  res.end();
});

router.get('/mul', function(req, res, next) {
  var first = req.query.first;
  var second  = req.query.second;
  var isValid = sanitizeQuery(req, res);
  if (isValid) {
    var mulResult = parseFloat(first) * parseFloat(second);
    res.json({result: mulResult.toFixed(3).toString()});
  }

  res.end();
});

// divide by zero?
router.get('/div', function(req, res, next) {
  var first = req.query.first;
  var second  = req.query.second;

  var isValid = sanitizeQuery(req, res);
  if (isValid) {
    if (parseFloat(second) === 0) { 
      res.status(400);
      res.json({message: "Division by zero is not allowed"})
    }
    else {
      var addResult = parseFloat(first) / parseFloat(second);
      res.json({result: addResult.toFixed(3).toString()});
    }
  }

  res.end();
});

module.exports = router;
