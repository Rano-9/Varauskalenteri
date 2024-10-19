from app import app
from flask import render_template, request, redirect, session
from db import db
from sqlalchemy import text
import datetime
import users
import tilat
import haltijat
import varaus

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
            return redirect("/register/error")
            

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
            return redirect("/login/error")
        
@app.route("/logout")
def logout():
    if users.logout():
        return redirect("/")
    return redirect("/logout/error")

@app.route("/tilat/new", methods = ["POST"])
def new():
    name = request.form["tilan nimi"]
    halt = request.form["halt"]
    print(name,halt)
    if tilat.lisää_tila(name,halt):
        return redirect("/")
    return redirect("/tilat/error")

@app.route("/tilat/<int:id>")
def tila(id):
     
    vastaus = tilat.hae_tila(id)
    kommentit = tilat.hae_kommentit(id)
    varaukset = varaus.hae_varaukset(id)
    tänään = []
    tulevat = []
    for i in varaukset:
        päivä = str.split(i.päivä, " ")
        print(päivä,datetime.date.today())
        if päivä[0] == str(datetime.date.today()):
            tänään.append(i)
            print(i.päivä)
        else:
            tulevat.append(i)
    return render_template("tilat.html", data=vastaus, tid=f"{id}", kommentit=kommentit,varaukset=varaukset,tänään=tänään,tulevat=tulevat)

@app.route("/tilat/<int:id>/new", methods = ["POST"])
def kom(id):
    kommentti = request.form["kommentti"]
    tilat.lisaa_kommentti(kommentti,id)
    return redirect(f"/tilat/{id}")

@app.route("/tilat/<int:id>/del")
def ptila(id):
    tilat.poista_tila(id)
    return redirect("/")
@app.route("/tilat/<int:id>/res")
def rtila(id):
    tilat.palauta_tila(id)
    return redirect("/")

@app.route("/tilat/<int:id>/varaa", methods = ["POST","GET"])
def vtila(id):

        user_id = session["user_id"]
        if request.method == "POST":
            nimi = request.form["nimi"]
            kuvaus = request.form["kuvaus"]
            päivä = request.form["päivä"]
            aika = request.form["aika"]
            dt = päivä + " "+ aika
            varaus.lisää_varaus(nimi,kuvaus,dt,id,user_id)

            return redirect(f"/tilat/{id}")

        if request.method == "GET":
            tila = tilat.hae_tila(id)
            return render_template("varaus.html", id=id,tila=tila)

        return redirect("tilat/error")

@app.route("/haltijat")
def H_index():
    lista = haltijat.hae_haltijat()

    return render_template("haltijat.html", data=lista )

@app.route("/haltijat/new", methods = ["POST"])
def H_new():
    nimi = request.form["nimi"]
    puh = request.form["puh"]
    email = request.form["email"]
    haltijat.lisää_haltija(nimi,puh,email)
    return redirect("/haltijat")

@app.route("/<path:path>/error")
def error_catch(path):
    return render_template("error.html",path=path)

@app.route("/error")
def bad_error():
    return redirect("/")