from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Key'

@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/add2', methods=['POST'])
def increment2():
    session['counter'] += 1
    return redirect('/')

@app.route('/add10', methods=['POST'])
def increment10():
    session['counter'] += 9
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
