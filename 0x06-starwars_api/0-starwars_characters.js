#!/usr/bin/node
// https://swapi-api.alx-tools.com/
// Write a script that prints all characters of a Star Wars movie:

// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api';

if (movieId) {
  request(`${url}/films/${movieId}`, async (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        await new Promise((resolve, reject) => {
          request(character, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              console.log(JSON.parse(body).name);
              resolve();
            }
          });
        });
      }
    }
  });
}
