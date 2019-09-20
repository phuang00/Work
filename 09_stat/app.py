#Peihua Huang
#SoftDev1 pd2
#K09 -- Static folder and templates
#2019-09-19

from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

coll = [0, 1, 1, 2, 3, 5, 8]

@app.route("/my_foist_template")
def template():
    return render_template('my_foist_template.html', foo = "fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
