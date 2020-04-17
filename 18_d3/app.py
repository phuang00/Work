# Peihua Huang, Jackie Lin (Team Har Gow Siu Mai)
# SoftDev2 pd1
# K18 -- Come Up For Air
# 2020-04-20

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import json, os
from utl import parse
# imported Flask, render_template, request, redirect, url_for, and session
app = Flask(__name__)
#create instance of class Flask

@app.route("/")
def root():
    return render_template('index.html', datas=parse.parse_json())

if __name__ == "__main__":
    app.debug = True
    app.run()
