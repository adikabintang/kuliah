var mongoose = require('mongoose');
var UserSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
        trim: true
    },
    username: {
        type: String,
        required: true,
        unique: true,
        trim: true
    },
    password: {
        type: String
    }
});

mongoose.model('user', UserSchema);

module.exports = mongoose.model('user');