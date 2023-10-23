# > Write a Python code to configure the MySQL Connector
# in your system and Insert data to MySQL Table after 
# which you Fetch and Display data from Table


import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
)

mycursor = mydb.cursor()

mycursor.execute('create database if not exists python_project ')

mycursor.execute('use python_project')

mycursor.execute('create table if not exists user( name VARCHAR(255), age INT)')

mycursor.execute('INSERT into user values ("dummy",19)')

mydb.commit()

mycursor.execute('select * from user')

for x in mycursor:
    print(x)