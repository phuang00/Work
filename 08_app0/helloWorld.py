from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print("__name__") #where will this go?
    return "No hablo queso!"

@app.route("/hello")
def hi():
    print("__hi__")
    return "Hola! Como estas?"

@app.route("/world")
def earth():
    print("__world__")
    return "Welcome to this wonderful world!!!"

if __name__ == "__main__":
    app.debug = True
    app.run()
