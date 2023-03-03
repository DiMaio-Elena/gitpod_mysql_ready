import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

domanda = input("vuoi aggiungere un animale? (si/no)")

while domanda == "si":

    Nome = input("Inserisci il nome del nuovo animale")
    Eta = int(input("Inserisci eta del nuovo animale"))
    Peso = int(input("Inserisci il peso"))
    Razza = input("Inserisci la razza")

    sql = "INSERT INTO Mammiferi ( Nome_Proprio, Razza, Peso,  Eta ) VALUES (%s, %s, %s, %s)"
    val = [
      (Nome, Razza, Peso, Eta ), 
    ]

    #COMMIT

    domanda = input("vuoi aggiungere un animale? (si/no)")

mycursor.executemany(sql, val)




        