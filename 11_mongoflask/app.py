#Peihua Huang, Jackie Lin (Team Concrastinators)
#SoftDev1 pd1
#K11 -- Import/Export Bank
#2020-03-04

from flask import Flask, render_template, request, redirect, url_for, session
# import events
import senator
import events

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/history")
def history():
    if "place" in request.args:
        # print("hi")
        # data = events.get_by_place("Egypt")
        # for item in data:
            # print(item['description'])
        return render_template("history.html", event=events.get_by_place(request.args["place"]))
    return render_template("history.html")

@app.route("/senators")
def senators():
    state = ""
    party = ""
    gender = ""
    first = ""
    last = ""
    num_gen = ""
    if "state" in request.args:
        state = senator.find_state(request.args["state"])
    if "party" in request.args:
        party = senator.find_party(request.args["party"])
    if "gender" in request.args:
        gender = senator.find_gender(request.args["gender"])
    if "first" in request.args:
        first = senator.find_website(request.args["first"])
    if "last" in request.args:
        last = senator.find_description(request.args["last"])
    if "num_gen" in request.args:
        num_gen = senator.find_num_gender(request.args["num_gen"], int(request.args["num"]))
    return render_template("senators.html", state=state, party=party,
                                            gender=gender, first=first,
                                            last=last, num_gen=num_gen)

if __name__ == "__main__":
    app.debug = True
    senator.create_senators()
    events.create_events()
    # senators.create_senators()
    app.run(host='0.0.0.0')
