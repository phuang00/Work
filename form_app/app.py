from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def root():
    print(app)
    return ""

@app.route("/foo.html")
def hello_world():
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
