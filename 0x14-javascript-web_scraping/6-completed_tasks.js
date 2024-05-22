#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = todos.reduce((acc, todo) => {
      if (todo.completed) {
        if (!acc[todo.userId]) {
          acc[todo.userId] = 0;
        }
        acc[todo.userId]++;
      }
      return acc;
    }, {});
    console.log(completedTasks);
  }
});
