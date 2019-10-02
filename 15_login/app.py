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
# imported Flask, render_template, and request
app = Flask(__name__)
#create instance of class Flask

usr = "apples"
pwd = "bananas"
#session["loggedIn"] = False

@app.route("/")
def root():
    #if (session["loggedIn"]):
        #return redirect(url_for("welcome"))
    return render_template("template.html")

@app.route("/auth")
def authenticate():
    if (usr == request.args['username']):
        if (pwd == request.args['password']):
            #session["loggedIn"] = True
            return redirect(url_for("welcome"))
        else:
            return render_template("error.html", rsn = "incorrect password")
    else:
        return render_template("error.html", rsn = "incorrect username")
    return render_template("error.html", rsn = "bad juju")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
