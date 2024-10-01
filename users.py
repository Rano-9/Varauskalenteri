from db import db
from sqlalchemy import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(user, sana):
    sql = f"SELECT id, password FROM users WHERE username = '{user}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()

    if not user:
        return False
    else:
        if check_password_hash(user.password,sana):
            session["user_id"] = user.id
            return True
        else:
            return False
def logout():

    try:
        del session["user_id"]
        return True
    except:
        return False
def register(user,sana):
    salattu = generate_password_hash(sana)
    try:
        sql = f"INSERT INTO users (username,password) VALUES ('{user}','{salattu}')"
        db.session.execute(text(sql))
        db.session.commit()

        return True
    except:
        return False
    
def onko():
    return session["user_id"]