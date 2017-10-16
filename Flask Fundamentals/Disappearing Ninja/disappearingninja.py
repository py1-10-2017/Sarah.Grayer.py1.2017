from flask import Flask, render_template, request, redirect, flash, session
import re

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja', methods=['POST'])
def process():
    if (request.form['color']) == 'blue':
        session['turtle'] = 'leonardo'
    elif (request.form['color']) == 'orange':
        session['turtle'] = 'michelangelo'
    elif (request.form['color']) == 'red':
        session['turtle'] = 'raphael'
    elif (request.form['color']) == 'purple':
        session['turtle'] = 'donatello'
    else:
        session['turtle'] = 'none'

    return render_template('ninja.html')
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('turtle')
    #session.pop('color')
    return redirect('/')

app.run(debug=True)
