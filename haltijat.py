from db import db
from sqlalchemy import text
from flask import session
import tilat


def hae_haltijat():
    sql = "SELECT id, nimi, tila FROM Haltijat"
    query = db.session.execute(text(sql))
    haltijat = query.fetchall()
    
    return haltijat

def hae_haltija(name):
    sql = "SELECT id, nimi FROM Haltijat WHERE nimi = :name"
    query = db.session.execute(text(sql),{"name":name})
    haltijat = query.fetchone()
    
    return haltijat

def lisää_haltija(nimi,puh=None,email=None):
    if session["admin"]:
        sql = "INSERT INTO Haltijat (nimi,tila) VALUES (:nimi,False)"
        db.session.execute(text(sql),{"nimi":nimi})
        db.session.commit()
        print(email,puh)
        if email and puh:
            sql = "SELECT id FROM Haltijat WHERE nimi =:nimi"
            query = db.session.execute(text(sql),{"nimi":nimi})
            hal_id = query.fetchone()

            lisää_haltija_tiedot(hal_id.id,puh,email)

def lisää_haltija_tiedot(id,puh,email):
    if session["admin"]:
        sql = "INSERT INTO Haltija_tiedot (id,puh,email) VALUES (:id,:puh,:email)"
        db.session.execute(text(sql),{"id":id,"puh":puh,"email":email})
        db.session.commit()
        print(f"X"*10)