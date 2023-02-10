# connetto MySql e python, definisco databse creato precedentemente, 
# aggiungo valori nella tabella, customers nelle colonne name e address, definisco i valori da aggiungere con val=()
#eseguo con mycursor.execute(sql, val)
# commito con mydb.commit()

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
