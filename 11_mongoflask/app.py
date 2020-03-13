#Peihua Huang, Jackie Lin (Team Concrastinators)
#SoftDev1 pd1
#K11 -- Import/Export Bank
#2020-03-04

from flask import Flask, render_template, request, redirect, url_for, session
import events

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/history")
def history():
    if "place" in request.args:
        return render_template("history.html", event=events.get_by_place(request.args["place"]))
    return render_template("history.html")

@app.route("/senators")
def senators():
    return render_template("senators.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
