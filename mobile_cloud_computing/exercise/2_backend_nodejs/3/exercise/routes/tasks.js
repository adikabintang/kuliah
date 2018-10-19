var express = require('express');
var router = express.Router();
const Tasks = require('../models/taskModel');

router.post('/task', function (req, res, next) {
    //const tasksDb = new Tasks(req.body);
    // tasksDb.save()
    //     .then(task => {
    //         res.status(201);
    //         res.contentType('application/json');
    //         res.send({ message: "Task successfully created", id: task.id });
    //     })
    //     .catch(err => {
    //         console.error("error in post /task: " + err.message);
    //         res.status(400).json({error: err.message});
    //     });
    var name = req.body.name;
    var created_date = req.body.created_date;
    var status = req.body.status;

    console.error("name: " + name + "; created_date: " + created_date + "; status: " + status);

    var newTask = new Tasks({
        name: name,
        created_date: created_date,
        status: status
    });

    newTask.save(function (err, task) {
        if (err) {
            console.error("error in post /task: " + err.message);
            res.status(400).json({ error: err.message });
        } else {
            res.status(201);
            res.contentType('application/json');
            res.send({ message: "Task successfully created", id: task.id });
        }

    });

    // Tasks.create({
    //     name: name,
    //     created_date: created_date,
    //     status: status
    // }, function (err, task) {
    //     if (err) {
    //         console.error("error in post /task: " + err.message);
    //         res.status(400).json({ error: err.message });
    //     } else {
    //         res.status(201);
    //         res.contentType('application/json');
    //         res.send({ message: "Task successfully created", id: task.id });
    //     }
    // });

});

router.get('/tasks', function (req, res, next) {
    Tasks.find({}, function (err, tasks) {
        if (err) {
            res.status(400);
            console.error("error get /tasks: " + error.message);
            res.json({ error: err.message });
        }

        console.error("get /tasks result: " + tasks);
        res.json(tasks);
    });
});

router.get('/tasks/:task_id', function (req, res, next) {
    Tasks.findById(req.params.task_id, function (err, tasks) {
        if (err) {
            res.status(400);
            console.error("error /tasks/:task_id: " + error.message);
            res.json({ error: err.message });
        }

        console.error("task/task_id result: " + tasks);
        res.contentType('application/json');
        res.send(JSON.stringify(tasks));
    });
});

router.delete('/tasks/:task_id', function (req, res, next) {
    Tasks.findByIdAndRemove(req.params.task_id, function (err) {
        if (err) {
            res.status(400);
            console.error("error delete /tasks: " + error.message);
            res.json({ error: err.message });
        }

        console.error('User deleted!');
        res.contentType('application/json');
        res.send({ message: "Task successfully deleted", id: req.params.task_id });
    });
});

router.put('/tasks/:task_id', function (req, res, next) {
    Tasks.findByIdAndUpdate(req.params.task_id,
        {
            name: req.body.name,
            created_date: req.body.created_date,
            status: req.body.status
        },
        function (err, user) {
            if (err) {
                res.status(400);
                console.error("error put /tasks/:task_id: " + error.message);
                res.json({ error: err.message });
            }

            res.contentType('application/json');
            res.send({
                message: "Task successfully updated",
                id: req.params.task_id,
                name: req.body.name,
                created_date: req.body.created_date,
                status: req.body.status
            });
        });
});

module.exports = router;
