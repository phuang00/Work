#Peihua Huang
#SoftDev1 pd2
#K -- Forms and Requests
#2019-09-25

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def root():
    print(app)
    return render_template("foo.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    return "Waaaa hooo HAAAH"

if __name__ == "__main__":
    app.debug = True
    app.run()
