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

// Ensure the correct number of arguments are provided
if (process.argv.length !== 3) {
    console.log("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = "https://swapi-api.alx-tools.com/api/films/";

/**
 * Fetch and print the names of all characters in a specified Star Wars movie.
 * 
 * @param {string} movieId - The ID of the Star Wars movie.
 */
function getMovieCharacters(movieId) {
    const url = `${baseUrl}${movieId}/`;

    // Fetch movie details from the Star Wars API
    request(url, (error, response, body) => {
        if (error) {
            console.error(`Failed to fetch data for movie ID ${movieId}:`, error);
            return;
        }

        if (response.statusCode !== 200) {
            console.error(`Failed to fetch data for movie ID ${movieId}: Status Code ${response.statusCode}`);
            return;
        }

        // Parse the JSON response
        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        // Fetch and print each character name
        characterUrls.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error(`Failed to fetch character data from ${characterUrl}:`, error);
                    return;
                }

                if (response.statusCode === 200) {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                } else {
                    console.error(`Failed to fetch character data from ${characterUrl}: Status Code ${response.statusCode}`);
                }
            });
        });
    });
}

// Call the function with the provided movie ID
getMovieCharacters(movieId);
