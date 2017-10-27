from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "secret_key"

import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
mysql = MySQLConnector(app, 'full_friends_db')

@app.route('/')
def index(): #Display all of the friends on the index.html page
    return render_template('index.html')



#@app.route('/friends', methods=["POST"])
#def create(): #Handle the add friend form submit and create the friend in the DB
    #return render_template('index.html')
    #@app.route('/friends/')
    #def edit(id): #Display the edit friend page for the particular friend

    #@app.route('/friends/<id>', methods=["POST"])
    #def update(id): #Handle the edit friend form submit and update the friend in the DB

    #@app.route('/friends/<id>/delete', methods=["POST"])
    #def destroy(id): #Delete the friend from the DB

app.run(debug=True)
