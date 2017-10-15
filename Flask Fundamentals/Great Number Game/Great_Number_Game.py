from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'Key'

@app.route('/')
def index():
    if 'random' not in session:#this line keeps from reset between guesses
        session['random'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods = ["post"])
def guess():
    if int(request.form['guess']) == session['random']:
        session['result'] = 'correct'

    elif int(request.form['guess']) > session['random']:
        session['result'] = 'high'

    else:
        session['result'] = 'low'

    return redirect ('/')

@app.route('/reset')
def reset():
    session.pop('random')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
