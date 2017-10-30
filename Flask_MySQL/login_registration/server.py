from flask import Flask, render_template, redirect, flash, request, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt #bcrypt
import md5
import os, binascii #salt
salt = binascii.b2a_hex(os.urandom(15))#salt
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app=Flask(__name__)
bcrypt = Bcrypt(app)
mysql=MySQLConnector(app, 'login_reg')
app.secret_key = "secret_key"

@app.route('/', methods=['GET'])
def index():#shows index.html
    return render_template('index.html')


@app.route('/create_user', methods=['POST'])
def create():#takes post data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    #salt =  binascii.b2a_hex(os.urandom(15))
    #encrypted_pw = md5.new(password + salt).hexdigest()
    confirm_password = request.form['confirm_password']

    print "*"*100
    print first_name
    print last_name
    print email
    print username
    print password

    #validations here
    valid = True #so that we don't redirect unless there are no errors

    if first_name == "":
        flash ("First name cannot be empty")
        valid = False
    elif not NAME_REGEX.match(first_name):
        flash ("First name can contain only letters")
        valid = False

    if last_name == "":
        flash ("Last name cannot be empty")
        valid = False
    elif not NAME_REGEX.match(last_name):
        flash ("Last name can contain only letters")
        valid = False

    if email == "":
        flash ("Email cannot be empty")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash ("Invalid email")
        valid = False

    if username == "":
        flash ("Username cannot be empty")
        valid = False
    elif len(username) <3:
        flash ("Username cannot be less than three characters")
        valid = False

    if password == "":
        flash ("Password cannot be empty")
        valid = False
    elif len(password) <8:
        flash("Password must be at least eight characters")
        valid = False

    if confirm_password != password:
        flash ("Passwords must match")
        valid = False

    if valid == True: #send to db
        query= "INSERT INTO users (first_name, last_name, email, username, pw_hash) VALUES (:first_name, :last_name, :email, :username, :password);"
        data = {
            "first_name": first_name,#column'email = form value 'email'
            "last_name": last_name,
            "email": email,
            "username": username,
            "password": password,
        }
        mysql.query_db(query, data)#defining
        flash ("Success! Please login")
        print "user added"
        return redirect ('/')
    else:
        print "invalid"
        return redirect('/')

@app.route('/login', methods=['POST','GET'])#takes post data
def login():#below is the data to get
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM users WHERE username=:username"
    data = {'username':username}
    user = mysql.query_db(query, data)#will return an array
    if len(user) == 0:#array does not exist
        flash("That is not a valid username")
        return redirect('/')
    else:
        user = user[0]
        if user["pw_hash"] == password:#grab 1st user, and first user's pw
            flash("Logged in!")
            return redirect ('/success')
        else:
            flash ("Invalid password")
            return redirect('/')

@app.route('/success', methods=['POST', 'GET']) #shows success
def success():
    print "This was a success"
    return render_template('success.html')

app.run(debug=True)

#if Get route, ask
#do I get data? do I render something?

#if Post route, ask
#do I handle data? do I add to db?
#redirect
