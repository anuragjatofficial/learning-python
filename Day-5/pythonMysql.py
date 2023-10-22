import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'pyhonProgramming'
)

# print(mydb)

mycursor= mydb.cursor()

# mycursor.execute('create database pythonDemo')

print(mycursor)

mycursor.execute('show databases')

for x in mycursor: # to check how many db's are creaetd in mysql
    print()
    

# to create a table in mysql using python

# mycursor.execute('drop database pythonDemo')

mycursor.execute('create table if not exists customers(name Varchar(255), address varchar(255))')

mycursor.execute('show tables')

for x in mycursor:
    print(x)

