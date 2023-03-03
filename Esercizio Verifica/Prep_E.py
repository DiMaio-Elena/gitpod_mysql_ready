import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

if Peso>2 :
    for x in listaAnimali:
        print (x)

#usare select from where...