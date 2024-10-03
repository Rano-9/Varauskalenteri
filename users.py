from db import db
from sqlalchemy import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(user, sana):
    sql = f"SELECT id, password, admin FROM users WHERE username = '{user}'"
    result = db.session.execute(text(sql))
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
    salattu = generate_password_hash(sana)
    if user == "Rano":
        sql = f"SELECT id FROM users WHERE username = 'Rano'"
        result = db.session.execute(text(sql))
        if result.fetchone():
            return False
        else:
            sql = f"INSERT INTO users (username,password,admin) VALUES ('{user}','{salattu}',True)"
            db.session.execute(text(sql))
            db.session.commit()
    try:
        sql = f"INSERT INTO users (username,password,admin) VALUES ('{user}','{salattu}',False)"
        db.session.execute(text(sql))
        db.session.commit()

        return True
    except:
        return False
    
def onko():
    try:
        return session["user_id"]
    except:
        return False