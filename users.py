from db import db
from sqlalchemy import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(user, sana):
    user = str.lower(user)
    sql = "SELECT id, password, admin FROM users WHERE username = :user"
    result = db.session.execute(text(sql),{"user":user})
    user = result.fetchone()

    if not user:
        return False
    else:
        if check_password_hash(user.password,sana):
            session["user_id"] = user.id
            if user.admin == True:
                session["admin"] = True
            else:
                session["admin"] = False
            return True
        else:
            return False
        
def logout():

    try:
        del session["user_id"]
        del session["admin"]
        return True
    except:
        return False
    
def register(user,sana):
    user = str.lower(user)
    sql = "SELECT id FROM Users WHERE username = :user"
    result = db.session.execute(text(sql),{"user":user})
    if result.fetchone():
        return False
    salattu = generate_password_hash(sana)
    try:
        sql = "INSERT INTO users (username,password,admin) VALUES (:user,:salattu,False)"
        db.session.execute(text(sql),{"user":user,"salattu":salattu})
        db.session.commit()
        return True
    except:
        return False
    
def onko():
    try:
        return session["user_id"]
    except:
        return False

def hae_käyttäjät():
    sql = "SELECT * FROM Users"
    result = db.session.execute(text(sql))
    return result.fetchall()