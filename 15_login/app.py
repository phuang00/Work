#Peihua Huang
#SoftDev1 pd2
#K15 -- Login
#2019-10-02

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import os
# imported Flask, render_template, and request
app = Flask(__name__)
#create instance of class Flask

usr = "apples"
pwd = "bananas"
app.secret_key = os.urandom(32)

@app.route("/")
def root():
    #print(url_for("login"))
    if ("loggedIn" in session):
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("login"))

@app.route("/auth")
def authenticate():
    if (usr == request.args['username']):
        if (pwd == request.args['password']):
            session["loggedIn"] = True
            return redirect(url_for("welcome"))
        else:
            return render_template("error.html", rsn = "incorrect password")
    else:
        return render_template("error.html", rsn = "incorrect username")
    return render_template("error.html", rsn = "bad juju")

@app.route("/welcome")
def welcome():
    if ("loggedIn" in session):
        return render_template("welcome.html")
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return render_template("template.html")

@app.route("/logout")
def logout():
    if ("loggedIn" in session):
        session.pop("loggedIn")
    return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run()
