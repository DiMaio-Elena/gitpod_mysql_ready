import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

i=0
domanda = input("vuoi aggiungere un animale? (si/no)")

while domanda =="si":
    i = i+1
    nome = input("Inserisci il nome del nuovo animale")
    eta = int(input("Inserisci il eta del nuovo animale"))
    
    #iNSRTE
    #COMMIT

    domanda = input("vuoi aggiungere un animale? (si/no)")
        