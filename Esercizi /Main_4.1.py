#collega mysql a python e seleziona ogni valore dalla tabella Customers ( mycursor.execute("SELECT * FROM customers") ), fecthcall permette di prendere i valori dall atabella e metterli in una lista

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)