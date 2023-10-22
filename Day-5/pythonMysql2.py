import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'sakila'
)

mycursor = mydb.cursor()

mycursor.execute('select * from actor')
# myres = mycursor.fetchall()

oneres = mycursor.fetchone()


print(oneres)

print('[######################]')

# for x in myres:
#     print(x)

