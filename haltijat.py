from db import db
from sqlalchemy import text
from flask import session
import tilat


def hae_haltijat():
    sql = f"SELECT id, nimi FROM Haltijat"
    query = db.session.execute(text(sql))
    haltijat = query.fetchall()
    
    return haltijat

def hae_haltija(name):
    sql = f"SELECT id, nimi FROM Haltijat WHERE nimi = '{name}'"
    query = db.session.execute(text(sql))
    haltijat = query.fetchone()
    
    return haltijat