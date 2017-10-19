from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[0-9])')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    errors = False

    if len(request.form['firstname']) <1:
        flash('First name cannot be empty')
        errors = True

    elif not request.form['firstname'].isalpha():
        flash('First name cannot contain numbers or special characters')
        errors = True

    if len(request.form['lastname']) < 1:
        flash('Last name cannot be empty')
        errors = True
    elif not request.form['lastname'].isalpha():
        flash('Last name cannot contain numbers or special characters')
        errors = True

    if len(request.form['email']) < 1:
        flash('Email cannot be empty')
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        errors = True

    if len(request.form['pass']) < 8:
        flash('Password must be 8 or more characters')
        errors = True
    elif not PASSWORD_REGEX.match(request.form['pass']):
        flash('Password must contain at least one uppercase letter and at least one number')
        errors = True
    elif request.form['pass'] != request.form['passconfirm']:
        flash('Passwords must match')
        errors = True

    if errors == False:
        flash('Thank you for submitting your information!')

    return redirect('/')


app.run(debug=True)
