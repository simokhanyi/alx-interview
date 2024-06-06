#!/usr/bin/env node

const request = require('request');
const process = require('process');

if (process.argv.length !== 3) {
    console.log("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = "https://swapi-api.alx-tools.com/api/films/";

function getMovieCharacters(movieId) {
    const url = `${baseUrl}${movieId}/`;

    request(url, (error, response, body) => {
        if (error) {
            console.error(`Failed to fetch data for movie ID ${movieId}:`, error);
            return;
        }

        if (response.statusCode !== 200) {
            console.error(`Failed to fetch data for movie ID ${movieId}: Status Code ${response.statusCode}`);
            return;
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

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

getMovieCharacters(movieId);
