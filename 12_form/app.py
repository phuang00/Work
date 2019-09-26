#Peihua Huang
#SoftDev1 pd2
#K12 -- Forms and Requests
#2019-09-25

from flask import Flask
from flask import render_template
from flask import request
# imported Flask, render_template, and request
app = Flask(__name__)
#create instance of class Flask

@app.route("/")
def root():
    print(app)
    # print class name and variable name
    return render_template("foo.html")
    # renders template foo.html

@app.route("/auth")
def authenticate():
    print("\n\n\n")
    print("*** DIAG: this Flask obj ***")
    print(app)
    # prints name of Flask object
    print("*** DIAG: request obj ***")
    print(request)
    # prints where the request comes from and request method
    print("*** DIAG: request.args ***")
    print(request.args)
    # prints the immutable dictionary that stores args from GET request
    #print("*** DIAG: request.args['username'] ***")
    #print(request.args['username'])
    # prints the value stored in key 'username' in request.args dictionary
    #print("*** DIAG: request.headers ***")
    #print(request.headers)
    return render_template(
        "response.html",
        user = request.args['username'],
        method = request.method
        )
    # render template and insert username and method in accordingly

if __name__ == "__main__":
    app.debug = True
    app.run()
