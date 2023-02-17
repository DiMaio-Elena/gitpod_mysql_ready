import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso,  Eta) VALUES (%s, %s, %s, %s)"
val = [
  ('Peter', 'Scimmia', 8, 3),
  ('Amy', 'Tigre', 220, 19),
  ('Hannah', 'Panda', 100, 1),
  ('Michael', 'Pitone', 2, 3),
  ('Sandy', 'aracnide', 0.3, 3),
]

mycursor.executemany(sql, val)

mydb.commit()
