

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user=" root ",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(255), Razza VARCHAR(255), Peso INT, Eta INT)")