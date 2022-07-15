DROP TABLE visits;
DROP TABLE attractions;
DROP TABLE cities;
DROP TABLE countries;
DROP TABLE users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE attractions (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE visits (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  attraction_id INT NOT NULL REFERENCES attractions(id) ON DELETE CASCADE,
  review TEXT
);

