#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(moviesWithWedgeAntilles.length);
  }
});
