#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);

    // Create an object to keep track of the completed tasks count for each user id
    const completedTasksCountByUserId = {};

    // Iterate through all the todos
    todos.forEach(function (todo) {
      if (todo.completed) {
        // If task is completed, increment the count for the corresponding user id
        if (!completedTasksCountByUserId[todo.userId]) {
          completedTasksCountByUserId[todo.userId] = 1;
        } else {
          completedTasksCountByUserId[todo.userId]++;
        }
      }
    });

    // Print the users with completed tasks
    console.log(completedTasksCountByUserId);
  }
});
