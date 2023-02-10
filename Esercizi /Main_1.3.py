##   database="mydatabase" serve a verificare se un database esiste nel sistema, se si riceve erore significa che non eistse nel sistema

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)