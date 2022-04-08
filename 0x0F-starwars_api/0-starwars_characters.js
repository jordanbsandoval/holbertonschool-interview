#!/usr/bin/node
// Star Wars Characters
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const cId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(cId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
