var jwt = require('jsonwebtoken');
var config = require('../config');

function verifyToken(req, res, next) {
    //var token = req.headers['x-access-token'];
    var token = req.session.token;
    console.error("verifyToken, token: " + token);
    if (!token) {
        //return res.status(403).send({ auth: false, message: 'No token provided.' });
        console.error("verifyToken: no token provided");
        return res.redirect('/login');
        //console.error("verifyToken: after next() in !token");
    }

    jwt.verify(token, config.secret, function (err, decoded) {
        if (err) {
            console.error("verifyToken: failed to authenticate token: " + err.message);
            return res.status(500).send({ auth: false, message: 'Failed to authenticate token.' });
        }

        // if everything good, save to request for use in other routes
        //req.body.userId = decoded.id;
        req.userId = decoded.id;
        next();
    });
}

module.exports = verifyToken;