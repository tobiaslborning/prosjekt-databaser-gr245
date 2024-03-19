import sqlite3
import queries

ordreNr = queries.generateNewOrderNumber()

conn = sqlite3.connect('teaterDB.db')
cursor = conn.cursor()

# Sletter Ordre
cursor.execute("DELETE FROM Ordre WHERE Antall = ?", (101,))

# Oppretter ordre
cursor.execute(
    "INSERT INTO Ordre VALUES (?,'10:00', '18-02-2024', NULL, NULL, 2)",(ordreNr,)) 

# Leser fil
with open('seats/gamle-scene.txt', 'r') as file:
    data = file.read()

# Henter dato
splitdata = data.split('\n')
dato = splitdata[0][5:].split('-')
dato.reverse()
dato = '-'.join(dato)


# Henter galleri
galleri = splitdata[2:5]
galleri.reverse()

# Henter balkong
balkong = splitdata[6:10]
balkong.reverse()

# Henter parkett
parkett = splitdata[11:21]
parkett.reverse()

# Oppretter billetter
def opprettBilett(sted):
    num_items = len(sted)
    if num_items == 3:
        sal = 'Galleri'
    elif num_items == 4:
        sal = 'Balkong'
    else:
        sal = 'Parkett'
    radNr = 0
    for row in sted:
        radNr += 1
        seteNr = 0
        for sete in row:
            seteNr += 1
            if (sete == '1'):
                cursor.execute("SELECT SeteID FROM Sete WHERE SalNr = ? AND SeteNr = ? AND RadNr = ? AND Omrade = ?", (2, seteNr, radNr, sal))
                seteID = cursor.fetchone()
                print(seteID)
                seteID = seteID[0]
                cursor.execute("INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (1,?,?,'Ordinær',?,350)", (dato, seteID,ordreNr))

opprettBilett(galleri)
opprettBilett(balkong)
opprettBilett(parkett)


# Må oppdatere ordre med setOrdreAntallOgPris(ordreNr)            



conn.commit()
conn.close()
