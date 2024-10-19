from db import db
from sqlalchemy import text
from flask import session
import datetime
import haltijat
import tilat

def hae_varaukset(id):
    date = datetime.date.today()
    date0=date
    date += datetime.timedelta(days=14)
    sql = "SELECT TO_CHAR(V.päivä,'YYYY-MM-DD HH24:MI') AS päivä, V.id, Ut.username, Vt.nimi, Vt.kuvaus FROM Varaukset AS V, Varaus_tiedot AS Vt, Users AS Ut WHERE ut.id = vt.luoja AND v.id = vt.id AND V.tila = :tila AND v.päivä BETWEEN :date0 AND :date"
    t = text(sql)
    query = db.session.execute(t,{"tila":id,"date0":date0,"date":date})
    varaukset = query.fetchall()
    return varaukset

def lisää_varaus(nimi,kuvaus,päivä,tila_id,luoja_id):
    sql = "INSERT INTO Varaukset (tila,päivä) VALUES (:tila,:päivä) RETURNING id"
    t = text(sql)
    query = db.session.execute(t,{"tila":tila_id,"päivä":päivä})
    id = query.fetchone()
    id = id[0]
    sql = "INSERT INTO Varaus_tiedot (id, nimi, kuvaus, luoja) VALUES (:id,:nimi,:kuvaus,:luoja)"
    t = text(sql)
    db.session.execute(t,{"id":id,"nimi":nimi,"kuvaus":kuvaus,"luoja":luoja_id})
    db.session.commit()
    return True
    