DROP TABLE visits_attraction;
DROP TABLE visits_city;
DROP TABLE visits_country;
DROP TABLE attractions;
DROP TABLE cities;
DROP TABLE countries;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id)
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id),
    city_id INT REFERENCES cities(id),
    attraction_cat VARCHAR(255)
);

CREATE TABLE visits_country(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    review TEXT
);

CREATE TABLE visits_city (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    review TEXT
);

CREATE TABLE visits_attraction (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    attraction_id INT NOT NULL REFERENCES attractions(id) ON DELETE CASCADE,
    review TEXT
);