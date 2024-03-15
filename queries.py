import sqlite3


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
    sysout = "SeteID: " + str(seteID[0])
    print(sysout)
    return seteID[0]

getSeteID(2, 1, 1, "Balkong")