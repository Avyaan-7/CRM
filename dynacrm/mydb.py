#INSTALL MYSQL ON YOUR COMPUTER
#pip install mysql
#pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Avyaan7#",
)
#prepare a cursor object
#cursor analogy - The database is a big table → the cursor is your pointer/remote control to run queries and read rows.
mycursor = mydb.cursor()  #mydb in this case refers to the mydb variable created above

#create a database
mycursor.execute("CREATE DATABASE apt_directory")

print("Should be done")