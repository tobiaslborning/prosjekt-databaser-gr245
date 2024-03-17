import sqlite3
import queries

ordreNr = queries.generateNewOrderNumber()

# Open the file in read mode ('r')
with open('seats/hovedscenen.txt', 'r') as file:
    # Read the contents of the file
    data = file.read()

# Henter dato
splitdata = data.split('\n')
dato = splitdata[0][5:]

# Henter parkett
parkett = splitdata[7:-1]
parkett.reverse()
print(dato)
print(parkett)

# connect to db
conn = sqlite3.connect('teaterDB.db')
cursor = conn.cursor()

# Sletter Ordre
cursor.execute("DELETE FROM Ordre WHERE Antall = ?", (100,))

# Oppretter ordre
cursor.execute(
    "INSERT INTO Ordre VALUES (?,'10:00', '18-02-2024', 100, 100, 4)",(ordreNr,)) # pris og antall 100 må endres

# Oppretter billetter
radNr = 0
seteNr = 0
for row in parkett:
    radNr += 1
    for sete in row:
        seteNr += 1
        #print('Rad:', radNr, 'Sete:', seteNr, 'Status:', sete)
        if (sete == '1'):
            print('Rad:', radNr, 'Sete:', seteNr, 'Status:', sete)
            cursor.execute("SELECT SeteID FROM Sete WHERE SalNr = ? AND SeteNr = ? AND RadNr = ? AND Omrade = ?", (1, seteNr, radNr, 'Parkett'))
            seteID = cursor.fetchone()
            print(seteID)
            seteID = seteID[0]
            cursor.execute("INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (1,?,?,'Ordinær',?,350)", (dato, seteID,ordreNr))
            print('Rad:', radNr, 'Sete:', seteNr, 'Status:', sete)
        

# GALLERI HAR INGEN STOLER, DROPPES
            
conn.commit()
conn.close()

