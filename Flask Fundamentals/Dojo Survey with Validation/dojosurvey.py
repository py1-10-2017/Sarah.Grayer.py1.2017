from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be empty")
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be longer than 120 characters.")
    else:
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template('results.html', name = name, location = location, language = language, comment = comment)
    return redirect('/')

app.run(debug=True)
