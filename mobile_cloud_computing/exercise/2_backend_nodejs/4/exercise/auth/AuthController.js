var express = require('express');
var router = express.Router();

var User = require('../models/user');
var jwt = require('jsonwebtoken');
var bcrypt = require('bcryptjs');
var config = require('../config');
var verifyToken = require('./verifyToken');

router.get('/register', function (req, res, next) {
    res.status(200).json({ message: "Register User Page" });
});

router.post('/register', function (req, res, next) {
    var inputEmail = req.body.email;
    var inputUsername = req.body.username;
    var inputPassword = req.body.password;
    var inputPasswordConf = req.body.passwordConf;
    var salt = 10;

    if (inputPassword !== inputPasswordConf) {
        console.error("post /register: password do not match");
        res.status(400).json({ message: "Passwords do not match." });
    } else {
        var hashedPassword = bcrypt.hashSync(inputPassword, salt);

        User.create({
            email: inputEmail,
            username: inputUsername,
            password: hashedPassword
        }, function (err, user) {
            if (err) {
                console.error("/register error while registering: " + err.message);
                res.status(500).json({message: "Error while registering user."});
            } else {
                var token = jwt.sign({ id: user._id }, config.secret, {
                    expiresIn: 86400 // expires in 24 hours
                });

                res.status(200).send({ message: "User has been successfully registered", 
                    auth: true, token: token });
            }
        });
    }

});

router.get('/login', function(req, res, next) {
    console.error("get /login, nothing");
    res.status(200).json({message: "Login Page"});
});

router.post('/login', function(req, res, next) {
    var inputEmail = req.body.logemail;
    var inputPassword = req.body.logpassword;

    console.error("post /login; email: " + inputEmail + ", password: " + inputPassword);

    if (inputEmail === undefined || inputPassword === undefined) {
        console.error("post /login: undefined");
        return res.status(400).json({message: "All fields required."});
    }

    User.findOne({ email: inputEmail }, function (err, user) {
        if (err) {
            console.error("ouch I don't know what happens");
            return res.status(500).json({message: "AAAAAAAAA"});
        }

        if (!user) {
            console.error("/post login: wrong email or password")
            return res.status(401).json({message: "Wrong email or password."});
        } else {
            var passwordIsValid = bcrypt.compareSync(inputPassword, user.password);
            
            if (!passwordIsValid) {
                console.error("/post login: wrong password");
                return res.status(401).json({message: "Wrong email or password."});
            }

            var token = jwt.sign({ id: user._id }, config.secret, {
                expiresIn: 86400 // expires in 24 hours
            });

            //res.status(200).send({ auth: true, token: token });
            // redirect to profile
            console.error("post /login: redirecting to profile");
            //res.headers['x-access-token'] = token;
            //res.header('x-access-token', token);
            req.session.token = token;
            res.redirect('/profile');
        }
    });
});

router.get('/profile', verifyToken, function(req, res, next) {
    console.error("get /profile req.userId: " + req.userId);
    //message: ‘User logged in!’, username, email, auth (true / false), token (JWT / null) userId (extracted by verifyToken.js)
    User.findById(req.userId, function (err, user) {
        res.status(200).json({message: "User logged in!", username: user.username, email: user.email,
            auth: true, token: req.session.token, userId: req.userId});
    });
});

router.get('/logout', function(req, res, next) {
    req.session.token = null;
    res.redirect('/login');
});

module.exports = router;