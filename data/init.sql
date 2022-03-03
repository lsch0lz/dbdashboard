CREATE DATABASE IF NOT EXISTS dbdashboard;
USE dbdashboard;
CREATE TABLE IF NOT EXISTS user (id int NOT NULL auto_increment, name varchar(255), lastname varchar(255), email varchar(255), password varchar(255), PRIMARY KEY (id));