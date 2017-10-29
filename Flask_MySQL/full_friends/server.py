from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "secret_key"

import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
mysql = MySQLConnector(app, 'full_friends_db')

@app.route('/')
def index(): #Display all of the friends on the index.html page
    query = "SELECT * FROM friends" #defines what the query below will do
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends) #passes data to template

@app.route('/addfriends', methods=['POST'])
def create(): #Handle the add friend form submit and create the friend in the DB
    query= "INSERT INTO friends (first_name, last_name, email, created_at) VALUES(:first_name, :last_name, :email, NOW())"
    data = { #Dict of data below from POST data received
		'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
	}
    mysql.query_db(query, data)
    print "friend added"
    return redirect('/')

@app.route('/edit_friend/<friend_id>', methods=['POST', 'GET'])
def edit(friend_id): #Display the edit friend page for the particular friend
    print "edit"
    return render_template('edit.html')

@app.route('/friend/<friend_id>', methods=['POST', 'GET'])
def update(friend_id):#Handle the edit friend form submit and update the friend in the DB
    query = "UPDATE friends SET first_name= :first_name, last_name= :last_name, email= :email WHERE id= :id"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'email': request.form['email'],
        'id': id
        }
    mysql.query_db(query, data)
    print "update"
    return redirect('/')

@app.route('/delete_friend/<friend_id>', methods=['POST', 'GET'])
def destroy(friend_id): #Delete the friend from the DB
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    print "delete"
    return redirect('/')

app.run(debug=True)
