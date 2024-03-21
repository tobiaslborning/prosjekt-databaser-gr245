import sqlite3
import queries

def scan_seats_hovedscenen():

    
    # Open the file in read mode ('r')
    with open('seats/hovedscenen.txt', 'r') as file:
        # Read the contents of the file
        data = file.read()

    # Henter dato
    splitdata = data.split('\n')
    dato = splitdata[0][5:].split('-')
    dato.reverse()
    dato = '-'.join(dato)


    # Henter parkett
    parkett = splitdata[7:-1]
    parkett.reverse()

    salNr = 1
    stykkeID = 2
    ordreNr = queries.genererNyttOrdreNr()
    takenSeatIDs = queries.hentSolgteSeter(stykkeID, dato)

    # connect to db
    conn = sqlite3.connect('teaterDB.db')
    cursor = conn.cursor()

    # Sletter Ordre
    cursor.execute("DELETE FROM Ordre WHERE Antall = ?", (100,))

    # Oppretter ordre
    cursor.execute(
        "INSERT INTO Ordre VALUES (?,'10:00', '18-02-2024', NULL, NULL, 4)",(ordreNr,)) 

    success = True
    # Oppretter billetter
    radNr = 0
    seteNr = 0
    for row in parkett:
        radNr += 1
        for sete in row:
            seteNr += 1
            if (sete == '1'):
                cursor.execute("SELECT SeteID FROM Sete WHERE SalNr = ? AND SeteNr = ? AND RadNr = ? AND Omrade = ?", (salNr, seteNr, radNr, 'Parkett'))
                seteID = cursor.fetchone()
                seteID = seteID[0]
                if seteID not in takenSeatIDs:
                    cursor.execute("INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (?,?,?,'Ordinær',?,350)", (stykkeID, dato, seteID,ordreNr))
                else:
                    success = False
    conn.commit()
    conn.close()
  
    if success:
        print(f"Kjøp av seter i hovedscenen fullført")
        queries.oppdaterOrdrePrisOgAntall(ordreNr)  
    else:
        print(f"Billettene er allerede kjøpt")
        queries.slettOrdre(ordreNr)

    # GALLERI HAR INGEN STOLER, DROPPES

scan_seats_hovedscenen()
