#!/usr/bin/env node

/**
 * Script to print all characters of a specified Star Wars movie.
 * 
 * The first positional argument passed is the Movie ID - example: 3 = "Return of the Jedi"
 * This script displays one character name per line in the same order as the "characters" list
 * in the /films/ endpoint of the Star Wars API.
 * 
 * Usage: ./0-starwars_characters.js <movie_id>
 */

const request = require('request');
const process = require('process');

/**
 * Wrapper function for request object that allows it
 * to work with async and await.
 * 
 * @param   {String} url - The URL to request.
 * @returns {Promise}    - A promise that resolves with parsed JSON response,
 *                         and rejects with the request error.
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * Entry point - makes requests to Star Wars API
 * for movie info based on the movie ID passed as a CLI parameter.
 * Retrieves movie character info then prints their names
 * in order of appearance in the initial response.
 */
async function main() {
  const args = process.argv;

  if (args.length !== 3) {
    console.log("Usage: ./0-starwars_characters.js <movie_id>");
    return;
  }

  const movieId = args[2];
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  try {
    const movie = await makeRequest(movieUrl);

    if (!movie.characters) {
      console.error('No characters found for this movie.');
      return;
    }

    for (const characterUrl of movie.characters) {
      try {
        const character = await makeRequest(characterUrl);
        console.log(character.name);
      } catch (error) {
        console.error(`Failed to fetch character data from ${characterUrl}:`, error);
      }
    }
  } catch (error) {
    console.error(`Failed to fetch data for movie ID ${movieId}:`, error);
  }
}

main();
