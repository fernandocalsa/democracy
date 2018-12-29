# Abstract
This app is able to store data about mayors, politicians and political parties, so we can analyze this data and find how in different regions one political party is more common than others, or which political party has the most highest salaries.

The app is developed in Python, and the data is stored in Neo4j database.

This project is just an example and is not production ready. If you have any question or idea please open an issue, a PR or fork the repository.

# Start app

To start the app you just have to run 
```
docker-compose up
```
in a console. This will create two new Docker images and run the containers:
- `democracy_neo4j`: This is a docker instance for Neo4j database. You can access to the database in your browser in http://localhost:7474/browser/
- `democracy_web`: This is the API. You can access to it through http://localhost:5000

# API endpoints

There are four different endpoints in the API:
- GET `/`: This endpoint returns 50 politicians. You can send a `limit` argument to set the number of results you want to receive. ie. `http://localhost:5000?limit=20` this url will return 20 results.
- POST `create`: This url will create a new politician. We can send these parameters:
  - `name`: politician name.
  - `political_party`: political party name.
  - `gender`: it accepts a `male` or `female`.
  - `charge`: charge that the politician has.
  - `institution`: institution name where the politician has the charge.
  - `region`: Name of the region where the institution is.
  - `salary`: Annual salary
  
  This will return the new politician object.
- PUT `/update`: This url will update a politician. We can send these parameters:
  - `id`: politician id in the database.
  - `political_party`: the name of the political party we want to assign to the politician.
- POST `/import`: This url is able to import a bunch of politicians from a CSV file. The CSV file needs these columns:
  - `0`: politician name
  - `1`: political party name
  - `2`: not used
  - `3`: genre. Right now it has to be `Hombre` for male or `Mujer` for female.
  - `4`: Charge.
  - `5`: not used
  - `6`: institution name
  - `7`: region name
  - `8`: salary

  The first row of the file is for the column titles. The file has to be sent in a `file` parameter.

# Postman collection
In order to be easy to test this app, you can use the postman collection provided in `postman_collection.json`. You can import it in Postman and try the API easier.
