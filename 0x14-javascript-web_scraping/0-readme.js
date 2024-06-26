#!/usr/bin/node
// script that reads and prints the content of a file

const fs = require('fs');

const filePath = process.argv[2];

function readFileAndPrint (filePath) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

readFileAndPrint(filePath);
