from flask import Flask             #facilitate flask webserving
from flask import render_template, request   #facilitate jinja templating
from flask import session, redirect, url_for, make_response        #facilitate form submission
import os
from emotion import *
import openai
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
    model_engine = "text-davinci-002"
    temperature = 0.8
    max_tokens = 40
    # send API request to OpenAI and receive response
    response = openai.Completion.create(
    engine=model_engine,
    prompt=f"Do not give extra output. Give me detailed advice for what to do when I am feeling {z}",
    temperature=temperature,
    max_tokens=max_tokens
    )
    generated_text = response.choices[0].text.strip()
    return render_template("direct.html",response = z,res=generated_text)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
