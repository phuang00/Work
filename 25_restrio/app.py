#Peihua Huang, Jacob Olin
#SoftDev1 pd2
#K25 -- Getting More REST
#2019-11-12

import urllib, json
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/ghibli")
def ghibli():
    u = urllib.request.urlopen("https://ghibliapi.herokuapp.com/locations")
    response = u.read()
    data = json.loads(response)
    return render_template("ghibli.html", locations=data)

@app.route("/ddclasses")
def cards():
    u = urllib.request.urlopen("http://www.dnd5eapi.co/api/classes")
    response = u.read()
    data = json.loads(response)
    return render_template("results.html", classes=data["results"])

@app.route("/weather")
def loripsum():
    u = urllib.request.urlopen("https://api.darksky.net/forecast/14bbf557960676ac31fd1ee5266f5da7/40.718100,-74.014760")
    response = u.read()
    data = json.loads(response)
    return render_template("weather.html", info=data["currently"])

if __name__ == "__main__":
    app.debug = True
    app.run()
