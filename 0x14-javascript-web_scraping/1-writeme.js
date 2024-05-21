#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');

const filepath = process.argv[2];
const StringToWrite = process.argv[3];

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

writeToFile(filepath, StringToWrite);
