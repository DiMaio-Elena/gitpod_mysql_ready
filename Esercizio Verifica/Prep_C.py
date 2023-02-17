
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()
mycursor.execute = ("SELECT * FROM Mammiferi")
listaAnimali = mycursor.fetchall()


for x in listaAnimali:
  print(x)