
CREATE TABLE Users (id SERIAL PRIMARY KEY, username TEXT, PASSWORD TEXT, admin boolean);
CREATE TABLE Tilat (id SERIAL PRIMARY KEY, nimi TEXT, näkyvä BOOLEAN, haltija INT);
CREATE TABLE Haltija_tiedot (id INT, puh TEXT, email TEXT);
CREATE TABLE Haltijat (id SERIAL PRIMARY KEY, nimi TEXT, tila BOOLEAN);
CREATE TABLE Kommentit (id SERIAL PRIMARY KEY, tila INT, luonti TIMESTAMP, kommentti TEXT);