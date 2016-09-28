from random import random
from flask import Flask, render_template
from utils import occupations, occupations

app = Flask(__name__)

@app.route('/')
def display():
    occupationDictionary = occupations.readFile()
    return render_template("template.html", data=occupationDictionary, chosen=occupations.getOccupation())

app.run()
app.debug
