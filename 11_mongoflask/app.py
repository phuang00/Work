#Peihua Huang, Jackie Lin (Team Concrastinators)
#SoftDev1 pd1
#K11 -- Import/Export Bank
#2020-03-04

from flask import Flask, render_template, request, redirect, url_for, session
import events
import senators

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/history")
def history():
    if "place" in request.args:
        print("hi")
        data = events.get_by_place("Egypt")
        for item in data:
            print(item['description'])
        return render_template("history.html", event=events.get_by_place(request.args["place"]))
    return render_template("history.html")

@app.route("/senators")
def senators():
    return render_template("senators.html")

if __name__ == "__main__":
    app.debug = True
    senators.create_senators()
    events.create_events()
    # senators.create_senators()
    app.run(host='0.0.0.0')
