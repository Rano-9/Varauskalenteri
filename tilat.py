from db import db
from sqlalchemy import text
from flask import session
import haltijat

def lisää_tila(name,halt=None):
    if session["admin"]:
        sql = f"SELECT * FROM Tilat WHERE nimi = '{name}'"
        query =db.session.execute(text(sql))
        tila = query.fetchone()
        if tila:
            return False
        db.session.commit()

        if halt:
            haltija = haltijat.hae_haltija(halt)         
            sql = f"INSERT INTO Tilat (nimi, näkyvä, haltija) VALUES ('{name}', true, {haltija[0]})"
        else:
            sql = f"INSERT INTO Tilat (nimi, näkyvä) VALUES ('{name}', true)"
        db.session.execute(text(sql))
        db.session.commit()
        
            
        return True

def poista_tila(id):
    if session["admin"]:
        sql = f"UPDATE tilat SET näkyvä=FALSE WHERE id={id}"
        db.session.execute(text(sql))
        db.session.commit()
    

def palauta_tila(id):
    if session["admin"]:
        sql = f"UPDATE tilat SET näkyvä=TRUE WHERE id={id}"
        db.session.execute(text(sql))
        db.session.commit()

def hae_tilat():
    sql = f"SELECT * FROM Tilat"
    query = db.session.execute(text(sql))
    tilat = query.fetchall()
    return tilat

def hae_tila(id):
    sql = f"SELECT nimi FROM Tilat WHERE id ={id}"
    query = db.session.execute(text(sql))
    vastaus = query.fetchone()
    return vastaus

def hae_kommentit(id):
    sql = f"SELECT kommentti, id FROM Kommentit WHERE tila = {id} AND näkyvä = true"
    query = db.session.execute(text(sql))
    kommentit = query.fetchall()
    return kommentit

def lisaa_kommentti(kommentti,id):
    toija = session["user_id"]
    sql = f"INSERT INTO kommentit (tila, kommentti, luoja, näkyvä) VALUES ({id},'{kommentti}', {toija}, True)"
    db.session.execute(text(sql))
    db.session.commit()
    return True


#sql = f"INSERT INTO Haltijat (nimi, tila) VALUES ('{halt}',False)"
#            db.session.execute(text(sql))