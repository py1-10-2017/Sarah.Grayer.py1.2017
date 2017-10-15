from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'Key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = ""
    return render_template("index.html", gold=['gold'], activities=session['activities'])


@app.route('/process_money', methods=["POST"])
def process():
    building = request.form['building']
    if building == 'farm':
        newgold = random.randint(10,21)
        #session['activities'].append({'activity':"You entered a {} and earned {} gold".format(building, newgold), 'class':'win'})
        session['activity'] = "\n" " You entered a {} and earned {} gold".format(building, newgold)

    elif building == 'cave':
        newgold = random.randint(5,11)
        #session['activities'].append({'activity':"You entered a {} and earned {} gold".format(building, newgold), 'class':'win'})
        session['activity'] = " You entered a {} and earned {} gold".format(building, newgold)
    elif building == 'house':
        newgold = random.randint(2,6)
        #session['activities'].append({'activity':"You entered a {} and earned {} gold".format(building, newgold), 'class':'win'})
        session['activity'] = " You entered a {} and earned {} gold".format(building, newgold)
    else:
        newgold = random.randint(-50,51)
        if newgold < 0:
            session['activity'] = " You entered a {} and lost {} gold".format(building, newgold)
        else:
            session['activity'] = " You entered a {} and won {} gold".format(building, newgold)

    session['gold'] += newgold
    session['activities'] += session['activity']
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)
