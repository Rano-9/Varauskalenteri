from db import db
from sqlalchemy import text
from flask import session

def lisää_tila(name,halt=None):
    
    
        sql = f"SELECT * FROM Tilat WHERE nimi = '{name}'"
        query =db.session.execute(text(sql))
        tila = query.fetchone()
        if tila:
            return False


        db.session.commit()
        sql = f"INSERT INTO Tilat (nimi, näkyvä) VALUES ('{name}', true)"
        db.session.execute(text(sql))
        if halt:
            sql = f"INSERT INTO Haltijat (name) VALUES ('{halt}') "
            db.session.execute(text(sql))
        db.session.commit()
        return True

def hae_tilat():
    sql = sql = f"SELECT * FROM Tilat"
    query = db.session.execute(text(sql))
    tilat = query.fetchall()
    return tilat

def lisaa_kommentti(kommentti,id):
    toija = session["user_id"]
    sql = f"INSERT INTO kommentit (tila, kommentti, luoja, näkyvä) VALUES ({id},'{kommentti}', {toija}, True)"
    db.session.execute(text(sql))
    db.session.commit()
    return True