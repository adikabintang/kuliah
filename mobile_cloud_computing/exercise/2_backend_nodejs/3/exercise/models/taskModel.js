const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const tasks = new Schema({
        name: {
            type: String,
            required: true // ga jelas beneran required apa ngga jing
        },
        created_date: {
            type: Date,
            default: Date.now()
        },
        status: {
            type: [{type: String, enum: ['pending', 'ongoing', 'completed']}], 
            default: ['pending']
        }
    }
);

module.exports = mongoose.model('tasks', tasks);