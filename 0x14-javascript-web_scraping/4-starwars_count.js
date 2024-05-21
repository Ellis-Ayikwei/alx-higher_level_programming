#!/usr/bin/node
//  script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const filteredFilms = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));

    const wedgeCount = filteredFilms.length;
    console.log(wedgeCount);
  }
});
