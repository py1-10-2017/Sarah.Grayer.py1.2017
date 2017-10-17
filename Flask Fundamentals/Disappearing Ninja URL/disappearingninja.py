from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja/<color>')
def show(color):
    ninjas = {
    'orange'='michelangelo',
    'blue'='leonardo'
    'red'='raphael',
    'purple'='donatello'
    }

    if color in ninjas:
        character = ninjas[color]
    else character = 'notapril'

    return render_template('ninja.html, character = character')
    #return redirect('/')

@app.route('/reset')
def reset():
    session.pop('turtle')
    #session.pop('color')
    return redirect('/')

app.run(debug=True)
