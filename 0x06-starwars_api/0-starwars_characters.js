#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

async function getMovieData () {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

  try {
    const response = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) reject(error);
        else resolve(response);
      });
    });

    if (response.statusCode !== 200) {
      throw new Error(`Error fetching movie data, status code ${response.statusCode}`);
    }

    const res = JSON.parse(response.body);
    const characters = res.characters;

    const characterNames = await Promise.all(characters.map(async (characterUrl) => {
      const charResponse = await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) reject(error);
          else resolve(response);
        });
      });

      if (charResponse.statusCode !== 200) {
        throw new Error(`Failed to fetch character data. Status code: ${charResponse.statusCode}`);
      }

      const characterData = JSON.parse(charResponse.body);
      return characterData.name;
    }));

    characterNames.forEach((name) => {
      console.log(name);
    });
  } catch (err) {
    console.log(`Error parsing movie data : ${err}`);
  }
}

if (!movieID) {
  console.log('USAGE: ./0-starwars_characters.js <movie id>');
} else {
  getMovieData();
}
