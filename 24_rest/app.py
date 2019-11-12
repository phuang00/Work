#Benjamin Peihua Huang
#SoftDev1 pd2
#K24 -- A RESTful Journey Skyward
#2019-11-12

from flask import Flask
from flask import render_template
import urllib3, json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib3.PoolManager()
    response = u.request('GET', "https://api.nasa.gov/planetary/apod?api_key=KaSPKF6wwTVHdhAzFcp9iivZUrgmlz1TtxRHge2U")
    data = json.loads(response)
    return render_template("index.html", pic=data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
