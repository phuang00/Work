#Peihua Huang
#SoftDev1 pd2
#K10 -- Occupations Flask app
#2019-09-19

import csv, random
from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    print(__name__) #where will this go?
    return "No hablo queso!"

@app.route("/occupyflaskst")
def template():
    dict = {}
    with open('data/occupations.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        next(csv_reader, None)
        for row in csv_reader:
            dict[row[0]] = float(row[1])
    del(dict["Total"])
    job = random.choices(list(dict.keys()), list(dict.values()))
    return render_template('template.html', title = "Occupation Data", heading = "Occupations and their Statistics", jobs = "Job Class", percent = "Percentage", team = " Team Cereal Before Milk: Peihua Huang, David Lupea", dict = dict.items(), rand_job = job[0])


if __name__ == "__main__":
    app.debug = True
    app.run()
