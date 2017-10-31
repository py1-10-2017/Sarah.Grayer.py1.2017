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
mysql=MySQLConnector(app, 'the_wall')
app.secret_key = "secret_key"

@app.route('/', methods=['GET'])
def index():#shows index.html (login and registration page)
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create():#takes post data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    print "*"*100
    print first_name
    print last_name
    print email
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
        query= "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password);"
        data = {
            "first_name": first_name,#column'email = form value 'email'
            "last_name": last_name,
            "email": email,
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
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email=:email"
    data = {'email':email}
    user = mysql.query_db(query, data)#will return an array
    if len(user) == 0:#array does not exist
        flash("That is not a valid e-mail")
        return redirect('/')
    else:
        user = user[0]
        if user["password"] == password:#grab 1st user, and first user's pw
            flash("Logged in!")
            session['user'] = user
            return redirect ('/wall')
        else:
            flash ("Invalid password")
            return redirect('/')

@app.route('/wall', methods=['POST', 'GET']) #shows success
def success():
    print "wall"
    query = "SELECT * FROM messages"
    messages = mysql.query_db(query)
    return render_template('wall.html', messages = messages)

@app.route('/post', methods=['POST', 'GET'])
def post():
    message = request.form['message']
    user = session['user']['id']

    if len(message) > 0: #send to db
        query= "INSERT INTO messages (message, users_id) VALUES (:message, :user_id)"
        data = {
            'message': message,#column "name" = form value name
            'user_id': user
        }
        mysql.query_db(query, data)#defining
        flash ("You have successfully posted a message!")
        print "message posted"
        return redirect ('/wall')
    else:
        flash ("Please write a message")
        print "invalid"
        return redirect('/wall')


app.run(debug=True)

#if Get route, ask
#do I get data? do I render something?

#if Post route, ask
#do I handle data? do I add to db?
#redirect
