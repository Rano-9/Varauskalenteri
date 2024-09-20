# Varauskalenteri

Sovelluksella näkee kalenteri, kalenterissa olevat varaukset / tapahtumat, ylläpitäjä voi luoda ja poistaa tiloja, käyttäjä voi tehdä varauksen, sekä kommentoida.

Sovelluksessa on 5 kpl tietokantoja:
    users
    tilat
    varaukset
    tilastot
    kommentit

Tietokannat voi luoda seuraavilla komennoilla

CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, PASSWORD TEXT, admin INT);

CREATE TABLE tilat (id SERIAL PRIMARY KEY, nimi TEXT, näkyvä BOOLEAN)

CREATE TABLE kommentit (id SERIAL PRIMARY KEY, tila INT, luonti TIMESTAMP, kommentti TEXT, näkyvä BOOLEAN);

CREATE TABLE varaukset (id SERIAL PRIMARY KEY, käyttäjä TEXT, aika TIMESTAMP, luotu TIMESTAMP, näkyvä BOOLEAN);

CREATE TABLE tilastot (id SERIAL PRIMARY KEY, kävijät INT, luotu TIMESTAMP);

