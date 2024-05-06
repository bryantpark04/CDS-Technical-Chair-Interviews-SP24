import os
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
  return render_template("logo.html")

@app.route('/subteams/<subteam>')
def subteams(subteam):
  return f"{subteam} subteam"