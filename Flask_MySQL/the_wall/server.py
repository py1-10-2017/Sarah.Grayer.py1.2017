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
            #flash("Logged in!")
            get_id = mysql.query_db("SELECT id from users WHERE email=:email", data)
            session['id'] = get_id[0]['id']
            return redirect ('/wall')
        else:
            flash ("Invalid password")
            return redirect('/')

@app.route('/wall', methods=['POST', 'GET']) #shows success
def success():
    print "wall"
    query = "SELECT messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users ON users_id=users.id"
    messages = mysql.query_db(query) #messages is now name of dict, this query returns an array of key:val data which we will extract from
    print messages
    return render_template('wall.html', messages = messages)

@app.route('/post', methods=['POST', 'GET'])
def post():
    message = request.form['message']

    if len(message) > 0: #send to db
        print session['id']
        query= "INSERT INTO messages (message, users_id, created_at) VALUES (:message, :user_id, NOW())"
        #messages.user_id=users.id"
        data = {
            'message': message,#column "name" = form value name
            'user_id': session['id']
        }
        mysql.query_db(query, data)#defining
        flash ("You have successfully posted a message!")
        print "message posted"
        return redirect ('/wall')
    else:
        flash ("Please write a message")
        print "invalid"
        return redirect('/wall')

@app.route('/logout', methods=['POST'])
def reset():
    session.pop('id')
    return redirect('/')


app.run(debug=True)

#if Get route, ask
#do I get data? do I render something?

#if Post route, ask
#do I handle data? do I add to db?
#redirect
