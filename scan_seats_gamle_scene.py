import sqlite3
import queries

def scan_seats_gamle_scene():

    

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

    salNr = 2
    stykkeID = 1
    ordreNr = queries.genererNyttOrdreNr()
    takenSeatIDs = queries.hentSolgteSeter(stykkeID, dato)

    conn = sqlite3.connect('teaterDB.db')
    cursor = conn.cursor()

    # Oppretter ordre
    cursor.execute(
        "INSERT INTO Ordre VALUES (?,'10:02', '18-02-2024', NULL, NULL, 4)",(ordreNr,)) 

    global success
    success = True
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
        for rad in sted:
            radNr += 1
            seteNr = 0
            for sete in rad:
                seteNr += 1
                if (sete == '1'):
                    cursor.execute("SELECT SeteID FROM Sete WHERE SalNr = ? AND SeteNr = ? AND RadNr = ? AND Omrade = ?", (salNr, seteNr, radNr, sal))
                    seteID = cursor.fetchone()
                    seteID = seteID[0]
                    if seteID not in takenSeatIDs:
                        cursor.execute("INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (1,?,?,'Ordinær',?,350)", (dato, seteID,ordreNr))
                    else:
                        global success
                        success = False

    opprettBilett(galleri)
    opprettBilett(balkong)
    opprettBilett(parkett)

    conn.commit()
    conn.close()

    if success:
        print(f"Kjøp av seter i gamle scene fullført")
        queries.oppdaterOrdrePrisOgAntall(ordreNr)  
    else:
        print(f"Billettene er allerede kjøpt")
        queries.slettOrdre(ordreNr)

             
    

scan_seats_gamle_scene()