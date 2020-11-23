from flask import render_template,redirect,url_for, request, Response
from application.models import  animalsdict
from application.forms import AnimalForms
import random
import requests

@app.route('/')
def index():
    return render_template('index.html', animalsdict=animalsditct)

@app.route('/submit', methods=['GET'])
def submit(key):
    random = random.randint(1,6)
    animalsdict[key] = animalsdict[key]
    if random == "1":
        return list(animalsdict.keys())[0]
    elif random == "2":
        return list(animalsdict.keys())[1]
    elif random == "3":
        return list(animalsdict.keys())[2]
    elif random =="4":
        return list(animalsdict.keys())[3]
    elif random == "5":
        return list(animalsdict.keys())[4]
    elif random == "6":
        return list(animalsdict.keys())[5]
    return redirect(url_for('index'))
    return render_template('index.html')
