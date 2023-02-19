from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
from emotion import *
#from management import User


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('home_page.html')

@app.route('/get_emotion', methods=['GET', 'POST'])
def get_emotion():
    emot = request.form.get('newText')
    arr = []
    arr.append(emot)
    response = co.classify(
    model='large',
    inputs=arr,
    examples=examples,
    )
    response = str(response).strip("[").strip("]")
    x = response.find("\"")
    y = response.find(",")
    z = response[x:y]
    return render_template("direct.html",response = z)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
