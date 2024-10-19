from db import db
from sqlalchemy import text
from flask import session
import tilat


def hae_haltijat():
    sql = "SELECT h.id, ht.nimi, h.näkyvä FROM Haltijat AS H, Haltija_tiedot AS Ht WHERE H.id = Ht.id"
    query = db.session.execute(text(sql))
    haltijat = query.fetchall()
    
    return haltijat

def hae_haltija(name):
    sql = "SELECT H.id, ht.nimi FROM Haltijat AS H, Haltija_tiedot AS Ht WHERE Ht.id = H.id AND ht.nimi = :name"
    query = db.session.execute(text(sql),{"name":name})
    haltijat = query.fetchone()
    
    return haltijat

def lisää_haltija(nimi,puh=None,email=None):
    if session["admin"]:
        sql = "INSERT INTO Haltijat (näkyvä) VALUES (False) RETURNING id"
        t = text(sql)
        query = db.session.execute(t)
        id = query.fetchone()
        sql = "INSERT INTO Haltija_tiedot (id,nimi,puh,email) VALUES (:id,:nimi,:puh,:email)"
        db.session.execute(text(sql),{"id":id[0],"nimi":nimi,"puh":puh,"email":email})
        db.session.commit()