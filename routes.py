from app import app
from flask import render_template, request, redirect
from db import db
from sqlalchemy import text
import users
import tilat
import haltijat

@app.route("/")
def index():
    try:
        if users.onko:
            lista = tilat.hae_tilat()
            haltijal = haltijat.hae_haltijat() 
            
            return render_template("index.html", tilat= lista, haltijat=haltijal)
    except:
        return render_template("index.html") 

@app.route("/register",methods = ["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        user = request.form["username"]
        sana = request.form["password"]
        if users.register(user,sana):
            return redirect("/")
        else: 
            return render_template("register.html")

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        user = request.form["username"]
        sana = request.form["password"]
        if users.login(user,sana):
            return redirect("/")
        else:
            return redirect("/")
        
@app.route("/logout")
def logout():
    if users.logout():
        return redirect("/")
    return redirect("/")

@app.route("/tilat/new", methods = ["POST"])
def new():
    name = request.form["tilan nimi"]
    halt = request.form["halt"]
    print(name,halt)
    if tilat.lisää_tila(name,halt):
        return redirect("/")
    return redirect("/")

@app.route("/tilat/<int:id>")
def tila(id):
     
    vastaus = tilat.hae_tila(id)
    kommentit = tilat.hae_kommentit(id)
    
    return render_template("tilat.html", data=vastaus, tid=f"{id}", kommentit=kommentit)

@app.route("/tilat/<int:id>/new", methods = ["POST"])
def kom(id):
    kommentti = request.form["kommentti"]
    tilat.lisaa_kommentti(kommentti,id)
    return redirect(f"/tilat/{id}")

@app.route("/tilat/<int:id>/del")
def ptila(id):
    tilat.poista_tila(id)
    return redirect("/")
@app.route("/tilat/<ind:id>/res")
def rtila(id):
    tilat.palauta_tila(id)
    return redirect("/")