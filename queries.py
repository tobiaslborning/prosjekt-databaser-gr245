import sqlite3

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
    return seteID[0]

print(getSeteID(2, 1, 1, "Balkong"))

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

print(getSoldSeats("1","03-02-2024"))

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

print(isSeatSold("1","03-02-2024",1,1,"Parkett"))

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

print(getStykkerByDato("05-02-2024"))

def generateNewOrderNumber():
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute(
        "SELECT COUNT(*) FROM Ordre")
    antall = cursor.fetchone()
    con.close()
    return antall[0]+1

print(generateNewOrderNumber())

def getAkter(skuespillerNavn):
    """
    Returns list of tuples with the AktNr and StykkeID of the plays the actor has a role in.
    """
    con = sqlite3.connect('teaterDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    cursor.execute('''
                    SELECT DISTINCT AktRoller.AktNr, AktRoller.StykkeID
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
                    SELECT Navn
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

print(getAkter("Arturo Scotti"))
print(getSkuespillereInAkt(1,2))