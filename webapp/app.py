#!/usr/bin/env python

import datetime
import os
import mysql.connector
from flask import Flask

app = Flask(__name__) 

password = os.environ["SALUTATOR_DB_PASSWORD"]

try:
	connection = mysql.connector.connect(host="salutator-mysql", user="root", passwd=password, database="hello")
except mysql.connector.Error as err:
  print(err)

cursor = connection.cursor()  
cursor.execute("SELECT * FROM salutation") 
s = "<table style='border:1px solid black'>"  
for row in cursor:  
    s = s + "<tr>"  
for x in row:  
    s = s + "<td>" + str(x) + "</td>"  
s = s + "</tr>"
  
connection.close()  
  
@app.route('/')  
@app.route('/home')  
def home():  

    return "<html><body>" + s + "</body></html>"  

