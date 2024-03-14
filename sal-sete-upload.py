import sqlite3

def addSalAndSete():
    con = sqlite3.connect("teaterDB.db")

    cursor = con.cursor()
    cursor.execute("SELECT * FROM sqlite_master")

    # Slett alt i TeaterSal og Sete
    cursor.execute('DELETE FROM TeaterSal')
    cursor.execute('DELETE FROM Sete')


    # --------------------- HOVEDSCENE -----------------------

    # Opprett Hovedscene
    cursor.execute("INSERT INTO TeaterSal VALUES (1,'Hovedscenen')")

    # Parkett hovedscenen
    seteNr = 0
    for radNr in range(1,19): # rad 1-18
        for i in range(0,28): # fyller radene
            seteNr += 1
            if (seteNr in range(467,471) or seteNr in range(495,499)): # sete 1 - 504
                print(f"Did not insert:{seteNr}")
            else:
                cursor.execute("INSERT INTO Sete VALUES (1,?,?,'Parkett')", (seteNr, radNr))

    # Galleri øvre
    for i in range(505,525): # sete 505 - 524
        seteNr += 1
        if (seteNr < 515):
            cursor.execute("INSERT INTO Sete VALUES (1,?,?,'Galleri Nedre')", (seteNr, radNr))
        else:
            cursor.execute("INSERT INTO Sete VALUES (1,?,?,'Galleri Øvre')", (seteNr, radNr))

    # --------------------- GAMLE SCENE -----------------------

    # Opprett Gamle Scene
    cursor.execute("INSERT INTO TeaterSal VALUES (2,'Gamle Scene')")

    # Parkett
    for radNr in [1,4,5,7]: #Rader med 18 seter
        for seteNr in range(1,19): 
            cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Parkett')",(seteNr,radNr))

    for radNr in [3,6,8,9]: #Rader med 17 seter
        for seteNr in range(1,18): 
            cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Parkett')",(seteNr,radNr))

    for seteNr in range(1,17): # Rad med 16 seter
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Parkett')",(seteNr,2))

    for seteNr in range(1,15): # Rad med 14 seter
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Parkett')",(seteNr,10))

    # Balkong
    for seteNr in range(1,29): # 1-29 rad 1
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Balkong')",(seteNr,1))

    for seteNr in range(1,28): # 1-28 rad 2
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Balkong')",(seteNr,2))

    for seteNr in range(1,23): # 1-22 rad 3
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Balkong')",(seteNr,3))

    for seteNr in range(1,18): # 1-17 rad 4
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Balkong')",(seteNr,4))

    # Galleri 
    for seteNr in range(1,34): # 1-33 rad 1
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Galleri')",(seteNr,1))

    for seteNr in range(1,19): # 1-18 rad 1
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Galleri')",(seteNr,2))

    for seteNr in range(1,18): # 1-17 rad 1
        cursor.execute("INSERT INTO Sete VALUES (2,?,?,'Galleri')",(seteNr,3))

    # ----------------------- Lukk og commit --------------------------
    con.commit()
    con.close()

