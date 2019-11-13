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
    u = urllib.request.urlopen("https://ghibliapi.herokuapp.com/locations")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", locations=data)

@app.route("/ddclasses")
def cards():
    u = urllib.request.urlopen("http://www.dnd5eapi.co/api/classes")
    response = u.read()
    data = json.loads(response)
    return render_template("results.html", classes=data["results"])

if __name__ == "__main__":
    app.debug = True
    app.run()
