## (come precedente) in aggiunta si visualizzano tutti i database con mycursor.execute("SHOW DATABASES") e li stampo

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)