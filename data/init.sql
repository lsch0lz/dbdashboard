CREATE DATABASE dbdashboard;
\c dbdashboard;
CREATE TABLE users ( id serial PRIMARY KEY, name VARCHAR ( 50 ) UNIQUE NOT NULL, lastname VARCHAR ( 50 ) NOT NULL, email VARCHAR ( 255 ) UNIQUE NOT NULL, password VARCHAR ( 255 ) NOT NULL);