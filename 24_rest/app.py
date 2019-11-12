#Benjamin Peihua Huang
#SoftDev1 pd2
#K?? -- ?????
#????-??-??

from flask import Flask
from flask import render_template
import urllib3, json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib3.urlopen("https://api.nasa.gov/planetary/apod?api_key=KaSPKF6wwTVHdhAzFcp9iivZUrgmlz1TtxRHge2U")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic=data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
