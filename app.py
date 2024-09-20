from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():

    return render_template("index.html") 

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = f"INSERT INTO messages (content) VALUES ('{content}')"
    db.session.execute(text(sql))
    db.session.commit()

    return redirect("/")

@app.route("/register")

def register():
    if session:
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/register/new", methods=["POST"])

def regi():
    username = request.form["username"]
    sql = f"SELECT id, password FROM users WHERE username='{username}'"
    result = db.session.execute(text(sql))
    user = result.fetchone()
    if user:
        return("OLET KÄYTTÄJÄ")
    else:
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        print(hash_value)
        sql = f"INSERT INTO users (username, password) VALUES ('{username}', '{hash_value}')"
        db.session.execute(text(sql))
        db.session.commit()
        return(username)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
