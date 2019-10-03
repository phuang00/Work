#Peihua Huang
#SoftDev1 pd2
#K16 -- Flashing
#2019-10-03

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
# hardcode username and password
app.secret_key = os.urandom(32)
# set secret key to randomly generated string

@app.route("/")
def root():
    #print(url_for("login"))
    if ("loggedIn" in session):
        # if user is logged in
        return redirect(url_for("welcome"))
        # redirect to welcome page
    else:
        # else
        return redirect(url_for("login"))
        # redirect to login page

@app.route("/auth")
def authenticate():
    if (usr == request.args['username']):
        if (pwd == request.args['password']):
            # if both the username and password are correct
            session["loggedIn"] = True
            # start a session
            return redirect(url_for("welcome"))
            # redirect to welcome page
        else:
            # if password is incorrect
            return render_template("error.html", rsn = "incorrect password")
            # render error template 
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
