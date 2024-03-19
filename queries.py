import sqlite3
import datetime

def getTeaterStykkeID(stykkeNavn):
    """
    Retrieves the TeaterStykkeID from the database based on the provided parameters.

    Parameters:
    teaterStykke (str): The name of the play.

    Returns:
    int: The TeaterStykkeID of the play.

    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT StykkeID FROM TeaterStykke WHERE Navn = ?", (stykkeNavn,))
    stykkeID = cursor.fetchone()
    con.close()
    return stykkeID[0]

def getSeteID(salNr, seteNr, radNr, omrade):
    """
    Retrieves the SeteID from the database based on the provided parameters.

    Parameters:
    salNr (int): 1 Hovedscene 2 Gamle Scene
    seteNr (int): Nr på setet i raden.
    radNr (int): Nr på raden
    omrade (str): Område (Galleri, Parkett, Balkong for Gamle Scene)
                         (Parkett, Galleri Øvre, Galleri Nedre for Hovedscene)

    Returns:
    int: The SeteID of the seat.

    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT SeteID FROM Sete WHERE SalNr = ? AND SeteNr = ? AND RadNr = ? AND Omrade = ?", (salNr, seteNr, radNr, omrade))
    seteID = cursor.fetchone()
    con.close()
    if seteID == None:
        print(f"SeteID for {salNr}, {seteNr}, {radNr}, {omrade} er ikke i databasen")
        return None
    return seteID[0]


def getSoldSeats(stykkeID, dato):
    """
    Retrieves the sold seats from the database based on the provided parameters.

    Parameters:
    teaterStykke (str): The name of the play.
    dato (str): The date of the play.

    Returns:
    list: A list of the sold seatIDs.

    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT SeteID FROM Billett WHERE StykkeID = ? AND Dato = ?", (stykkeID, dato))
    seteID = cursor.fetchall()
    con.close()
    return [x[0] for x in seteID]


def getSoldSeatsWithInfo(stykkeID, dato):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT SeteID, SalNr, RadNr, SeteNr, Omrade FROM Billett 
                    NATURAL JOIN Sete
                    WHERE StykkeID = ? AND Dato = ?
                   ''', (stykkeID, dato))
    seteID = cursor.fetchall()
    con.close()
    return [x for x in seteID]


def isSeatSold(stykkeID, dato, seteNr, radNr, omrade):
    """
    Checks if a seat is sold based on the provided parameters.

    Parameters:
    teaterStykke (str): The name of the play.
    dato (str): The date of the play.
    seteNr (int): The number of the seat.
    radNr (int): The number of the row.
    omrade (str): The area of the seat.

    Returns:
    bool: True if the seat is sold, False if not.

    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT SalNr FROM TeaterStykke WHERE StykkeID = ?", (stykkeID))
    salNr = cursor.fetchone()
    con.close()
    seteID = getSeteID(salNr[0],seteNr,radNr,omrade)
    return seteID in [x for x in getSoldSeats(stykkeID,dato)]

def getSkuespillereIStykke():
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")
    
    cursor.execute('''
                    SELECT DISTINCT StykkeNavn, Ansatt.Navn AS SkuespillerNavn, RolleNavn
                    FROM (
                        SELECT ts.navn AS StykkeNavn, ts.StykkeID, a.AktNr, a.Navn AS AktNavn, Rolle.RolleNavn, Rolle.RolleID 
                        FROM Akt AS a	
                        JOIN RolleIAkt AS ria ON a.AktNr = ria.AktNr AND a.StykkeID = ria.StykkeID
                        NATURAL JOIN Rolle
                        JOIN TeaterStykke AS ts ON ts.StykkeID = a.StykkeID
                    ) AS AktRoller
                    JOIN HarRolle AS hr ON AktRoller.RolleID = hr.RolleID
                    NATURAL JOIN Skuespiller
                    NATURAL JOIN Ansatt
                    ORDER BY StykkeNavn;
                    ''')
    
    info = cursor.fetchall()
    con.close()
    
    for row in info:
        print(f"Stykke: {row[0]}, Skuespiller: {row[1]}, Rolle: {row[2]}")


    return [x for x in info]
    

def getStykkerByDato(dato):
    """
    Retrieves the plays from the database based on the provided date.

    Parameters:
    dato (str): The date of the play.

    Returns:
    list: A list of the plays on the date.

    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute(
        "SELECT DISTINCT TeaterStykke.Navn FROM TeaterOppsettning NATURAL JOIN TeaterStykke WHERE TeaterOppsettning.Dato = ?", (dato,)) # komma etter dato løser biding error
    navn = cursor.fetchall()
    con.close()
    return [x[0] for x in navn]


def generateNewOrderNumber(): 
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute(
        "SELECT OrdreID FROM Ordre ORDER BY OrdreID DESC LIMIT 1")
    antall = cursor.fetchone()
    con.close()

    if not antall:
        return 1
    return int(antall[0])+1


def getAkter(skuespillerNavn):
    """
    Returns list of tuples with the AktNr and StykkeID of the plays the actor has a role in.
    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT DISTINCT AktRoller.AktNr, AktRoller.StykkeID, AktRoller.StykkeNavn
                    FROM (
                        SELECT ts.navn as StykkeNavn, ts.StykkeID, a.AktNr, a.Navn as AktNavn, Rolle.RolleNavn, Rolle.RolleID 
                        FROM Akt as a
                        JOIN RolleIAkt as ria
                        ON a.AktNr = ria.AktNr AND a.StykkeID = ria.StykkeID
                        NATURAL JOIN Rolle
                        JOIN TeaterStykke as ts
                        ON ts.StykkeID = a.StykkeID
                        ) as AktRoller
                    JOIN HarRolle as hr
                    ON AktRoller.RolleID = hr.RolleID
                    NATURAL JOIN Skuespiller
                    NATURAL JOIN Ansatt
                    WHERE Ansatt.Navn = ?
                    ''',(skuespillerNavn,))
        
    akter = cursor.fetchall()
    con.close()
    return [x for x in akter]

def getSkuespillereInAkt(aktNr, stykkeID):
    """
    Returns list of tuples with the SkuespillerID and SkuespillerNavn of the actors in the play.
    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT DISTINCT Navn
                    FROM (
                        SELECT ts.navn as StykkeNavn, ts.StykkeID, a.AktNr, a.Navn as AktNavn, Rolle.RolleNavn, Rolle.RolleID 
                        FROM Akt as a
                        JOIN RolleIAkt as ria
                        ON a.AktNr = ria.AktNr AND a.StykkeID = ria.StykkeID
                        NATURAL JOIN Rolle
                        JOIN TeaterStykke as ts
                        ON ts.StykkeID = a.StykkeID
                        ) as AktRoller
                    JOIN HarRolle as hr
                    ON AktRoller.RolleID = hr.RolleID
                    NATURAL JOIN Skuespiller
                    NATURAL JOIN Ansatt
                    WHERE AktNr == ? AND StykkeID = ?
                    ''',(aktNr, stykkeID))
        
    skuespillere = cursor.fetchall()
    con.close()
    return [x[0] for x in skuespillere]

def isInDb(skuespillerNavn):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT * 
                    FROM Skuespiller
                    NATURAL JOIN Ansatt
                    WHERE Ansatt.Navn = ?
                    ''',(skuespillerNavn,))
        
    skuespillere = cursor.fetchall()
    con.close()
    return len(skuespillere) > 0

def getMedSkuespillere(skuespillerNavn):
    akter = getAkter(skuespillerNavn)
    medSkuespillere = dict()

    if not isInDb(skuespillerNavn):
        print(f"{skuespillerNavn} er ikke i databasen")
        return
    
    for akt in akter:
        skuespillere = getSkuespillereInAkt(akt[0],akt[1])
        for skuespiller in skuespillere:
            if skuespillerNavn != skuespiller:
                if skuespiller not in medSkuespillere.keys():
                    medSkuespillere[skuespiller] = ([akt[2]])
                elif akt[2] not in medSkuespillere[skuespiller]:
                    medSkuespillere[skuespiller] = [akt[2]]

    for skuespiller in medSkuespillere.keys():
        for akt in medSkuespillere[skuespiller]:
            print(f"{skuespillerNavn} spiller med {skuespiller} i {' og '.join(medSkuespillere[skuespiller])}")


def registrerKunde(navn, telefon, addresse):

    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    # generer ny ID
    cursor.execute("SELECT count(*) FROM Kunde")
    kundeID = cursor.fetchone()
    kundeID = kundeID[0] + 1

    # sjekk om mobilnr er i databasen
    cursor.execute("SELECT count(*) FROM Kunde WHERE Mobilnummer = ?", (telefon,))
    antall = cursor.fetchone()
    if antall[0] > 0:
        print("Telefonnummeret er allerede registrert")
        return

    print(kundeID, navn, telefon, addresse)
    cursor.execute("INSERT INTO Kunde VALUES (?,?,?,?)", (kundeID, navn, telefon, addresse))

    con.commit()
    con.close()

def getDatoByStykkeID(stykkeID):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT Dato FROM TeaterOppsettning WHERE StykkeID = ?", (stykkeID,))
    dato = cursor.fetchall()
    con.close()
    return [x[0] for x in dato]

def setOrdreAntallOgPris(ordreNr):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")
    
    cursor.execute("SELECT Pris FROM Billett WHERE OrdreNr = ?", (ordreNr))
    price = cursor.fetchall()
    total_price = sum(x[0] for x in price)
    
    num_rows = len(price)

    
    cursor.execute("UPDATE Ordre SET Pris = ?, ANtall = ? WHERE OrdreID = ?",(total_price, num_rows, ordreNr))
    
    con.close()
    
    return total_price, num_rows

def kjop9Billetter(ordreNr):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute(
        "INSERT INTO Ordre VALUES (?,'10:00', '03-02-2024', 9, 3150, 4)",(ordreNr,)
    )

    for i in range(9):
        cursor.execute("INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (1,'03-02-2024',?,'Ordinær',?,350)", (525+i,ordreNr,))

    con.close()
    return ordreNr
    
def getForestillingSolgtBest():
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")
    
    cursor.execute('''
                    SELECT stykke.navn, oppsettning.dato, ifnull(antallSolgt,0) as billetterSolgt
                    FROM TeaterStykke AS stykke
                    NATURAL JOIN TeaterOppsettning AS oppsettning
                    LEFT OUTER JOIN (
                        SELECT StykkeID, Dato, COUNT(*) AS antallSolgt
                        FROM Billett
                        GROUP BY StykkeID, Dato
                    ) AS b 
                    ON stykke.StykkeID = b.StykkeID AND oppsettning.dato = b.Dato
                    ORDER BY billetterSolgt DESC
                   ''')
    info = cursor.fetchall()
    con.close()
    return [x for x in info]

    

def getBillettTyperAndPris(StykkeID):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")
    

    cursor.execute("SELECT BillettType, Pris FROM PrisTabell WHERE StykkeID = ?", (StykkeID,))
    billettTyper = cursor.fetchall()
    con.close()
    return [x for x in billettTyper]

def getPrisByBilletType(StykkeID, billettType):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT Pris FROM PrisTabell WHERE StykkeID = ? AND BillettType = ?", (StykkeID, billettType))
    pris = cursor.fetchone()
    con.close()
    return pris[0]

def createOrdre(antall, totalpris, kundenr):

    ordreNr = generateNewOrderNumber()

    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    time = datetime.datetime.now().strftime("%H:%M")
    date = datetime.datetime.now().strftime("%d-%m-%Y")

    cursor.execute(
        "INSERT INTO Ordre VALUES (?,?,?,?,?,?)", (ordreNr, time, date, antall, totalpris, kundenr))
    
    con.commit()
    con.close()

    return ordreNr

def getStykkeAndSalByID(stykkeID):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT Navn, SalNr FROM TeaterStykke WHERE StykkeID = ?", (stykkeID,))
    stykke = cursor.fetchone()
    con.close()
    return stykke

def getKundeByTelefon(tlf):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT KundeNr, Navn FROM Kunde WHERE Mobilnummer = ?", (tlf,))
    kunde = cursor.fetchone()
    con.close()
    return kunde

def getOmraderBySal(salNr):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("SELECT DISTINCT Omrade FROM Sete WHERE SalNr = ?", (salNr,))
    omrader = cursor.fetchall()
    con.close()
    return [x[0] for x in omrader]

def createBillett(stykkeID, dato, seteID, billettType, ordreNr, pris):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute(
        "INSERT INTO Billett(StykkeID,Dato,SeteID,BillettType,OrdreNr,Pris) VALUES (?,?,?,?,?,?)", (stykkeID, dato, seteID, billettType, ordreNr, pris))
    
    con.commit()
    con.close()

def deleteOrdre(ordreNr):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute("DELETE FROM Ordre WHERE OrdreID = ?", (ordreNr,))
    
    con.commit()
    con.close()

def getBilletterInOrdre(ordreNr):
    '''
    returns (StykkeNavn, Dato, SalNavn, Område, RadNr, SeteNr, Pris)
    '''
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT tstykke.Navn,  topps.Dato, tsal.Navn,  s.Omrade, s.RadNr, s.SeteNr, b.Pris
                    FROM Ordre as o
                    JOIN Billett as b
                    ON o.OrdreID = b.OrdreNr
                    NATURAL JOIN Sete as s
                    JOIN TeaterOppsettning as topps
                    ON b.StykkeID = topps.StykkeID AND b.Dato = topps.Dato
                    NATURAL JOIN TeaterStykke as tstykke
                    JOIN TeaterSal as tsal
                    ON s.SalNr = tsal.SalNr
                    WHERE o.OrdreID = ?
                   ''', (ordreNr,))
    ordre = cursor.fetchall()
    con.close()
    return ordre

def getKundeOrdre(telefon):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT o.OrdreID
                    FROM Ordre as o
                    JOIN Kunde as k
                    ON o.KundeNr = k.KundeNr
                    WHERE k.Mobilnummer = ?
                   ''', (telefon,))
    ordre = cursor.fetchall()
    con.close()

    return [x[0] for x in ordre]

def getOrdrePris(OrdreNr):
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT Pris
                    from Ordre
                    WHERE OrdreID = ?
                   ''', (OrdreNr,))
    pris = cursor.fetchone()
    con.close()
    return pris[0]