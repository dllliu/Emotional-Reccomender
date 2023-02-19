from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
from emotion import *
import openai
#from management import User
import db
from datetime import datetime



#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
openai.api_key = "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"

@app.route('/')
def index():
    if 'username' in session:
        return redirect("/home")
    return render_template('login.html') #edit

@app.route('/login', methods = ['GET','POST'])
def login():
    #Check if it already exists in database and render home page if it does
    #otherwise redirect to error page which will have a button linking to the login page
    username = request.form.get('username')
    password = request.form.get('password')
    if db.verify_account(username,password):
        session['username'] = username
        session['password'] = password
        return redirect("/home")
    if request.form.get('submit_button') is not None:
        return render_template("create_account.html")
    else:
        resp = make_response(render_template('error.html',msg = "username or password is not correct"))
        return resp

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect("/login")
    username = session['username']
    password = session['password']
    if db.verify_account(username, password):
        viewable_pages = db.get_user_stories(username)
        return render_template("home_page.html", username = username,
        viewable_stories = viewable_pages)
    
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    '''
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    '''
    #print("creating account")
    if request.method == 'POST':
        userIn = request.form.get('username')
        passIn = request.form.get('password') 
        if db.add_account(userIn, passIn) == -1:
            return f"account with username {userIn} already exists"
        else:
            return render_template("success_signup.html")
            #return redirect("/login")
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
    
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
    # send API request to OpenAI and receive response
    now = datetime.today().isoformat()
    db.add_entry(now, emot, session['username'])
    return render_template("direct.html",response = z)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
