from db import db
from sqlalchemy import text
from flask import session
import haltijat

def lisää_tila(name,halt=None):
    if session["admin"]:
        sql = "SELECT * FROM Tilat WHERE nimi = :name"
        query =db.session.execute(text(sql),{"name":name})
        tila = query.fetchone()
        if tila:
            return False
        db.session.commit()

        if halt:
            haltija = haltijat.hae_haltija(halt)         
            sql = "INSERT INTO Tilat (nimi, näkyvä, haltija) VALUES (:name, true, :haltija)"
            db.session.execute(text(sql),{"name":name,"haltija":haltija[0]})
        else:
            sql = "INSERT INTO Tilat (nimi, näkyvä) VALUES (:name, true)"
            db.session.execute(text(sql),{"name":name})
        
        db.session.commit()    
        return True

def poista_tila(id):
    if session["admin"]:
        sql = "UPDATE tilat SET näkyvä=FALSE WHERE id=:id"
        db.session.execute(text(sql),{"id":id})
        db.session.commit()
    

def palauta_tila(id):
    if session["admin"]:
        sql = "UPDATE tilat SET näkyvä=TRUE WHERE id=:id"
        db.session.execute(text(sql),{"id":id})
        db.session.commit()

def hae_tilat():
    sql = "SELECT * FROM Tilat WHERE näkyvä=TRUE"
    query = db.session.execute(text(sql))
    tilat = query.fetchall()
    return tilat

def hae_tila(id):
    sql = "SELECT nimi FROM Tilat WHERE id =:id"
    t = text(sql)
    query = db.session.execute(t,{"id":id})
    vastaus = query.fetchone()
    return vastaus

def hae_kommentit(id):
    sql = "SELECT kommentti, id FROM Kommentit WHERE tila = :id AND näkyvä =TRUE"
    query = db.session.execute(text(sql),{"id":id})
    kommentit = query.fetchall()
    return kommentit

def lisaa_kommentti(kommentti,id):
    toija = session["user_id"]
    sql = "INSERT INTO kommentit (tila, kommentti, luoja, näkyvä) VALUES (:id,:kommentti, :toija, True)"
    db.session.execute(text(sql),{"id":id,"kommentti":kommentti,"toija":toija,})
    db.session.commit()
    return True


#sql = f"INSERT INTO Haltijat (nimi, tila) VALUES ('{halt}',False)"
#            db.session.execute(text(sql))