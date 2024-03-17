import sqlite3


conn = sqlite3.connect('teaterDB.db')
cursor = conn.cursor()

def addSkuespillere():
    #Fjerner alle skuespillere før innsetting
    cursor.execute(
        "DELETE FROM Skuespiller"
    )
    #Innsetning av skuspiller
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('5','5')") #Setter skuespillerID til å være lik AnsattID
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('6','6')") 
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('7', '7')") 
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('8', '8')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('9', '9')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('10', '10')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('11', '11')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('12', '12')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('13', '13')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('14', '14')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('15', '15')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('16', '16')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('17', '17')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('18', '18')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('19', '19')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('20', '20')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('21', '21')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('22', '22')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('23', '23')")
    
def addDirektor():
    # Fjerner alle direktører før innsetting
    cursor.execute(
        "DELETE FROM Direktor"
    )
    #Innsetning av direktør
    cursor.execute(
        "INSERT INTO Direktor VALUES ('25','30')")

def addHarRolle():
    #Fjerner alle HarRoller før innsetting
    cursor.execute(
        "DELETE FROM HarRolle"
    )
    #Innsetning av hvem som har hvilke roller
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('5', '1')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('6', '2')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('7', '3')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('8', '4')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('9', '5')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('10', '6')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('10', '7')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('11', '8')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('12', '9')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('13', '10')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('13', '11')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('14', '11')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('14', '12')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('15', '13')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('15', '14')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('16', '15')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('17', '16')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('18', '17')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('19', '18')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('20', '19')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('21', '20')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('22', '21')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('23', '22')")
    cursor.execute(
        "INSERT INTO HarRolle VALUES ('24', '23')")
    
def addRolle():
    #Fjerner alle roller før innsetting
    cursor.execute(
        "DELETE FROM Rolle"
    )
    #Innsetning av roller
    cursor.execute(
        "INSERT INTO Rolle VALUES ('1', 'Haakon Haakonssønn')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('2', 'Inga fra Vartejg (Haakons Mor)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('3', 'Skule jarl')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('4', 'Fru Ragnhild (Skules hustru)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('5', 'Margrete (Skules datter)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('6', 'Sigrid (Skules søster)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('7', 'Ingebjørg')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('8', 'Biskop Nikolas')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('9', 'Gregorius Jonssønn')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('10', 'Paal Flida')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('11', 'Trønder')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('12', 'Baard Bratte')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('13', 'Jatgeir Skald')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('14', 'Dagfinn Bonde')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('15', 'Peter (prest og Ingebjørgs sønn)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('16', 'Sunniva Du Mond Nordal')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('17', 'Jo Saberniak')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('18', 'Marte.M Steinholt')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('19', 'Tor Ivar Hagen')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('20', 'Trond-Ove Skrødal')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('21', 'Natalie Grøndahl Tangen')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('22', 'Åsmund Flaten')")

def addAnsatte():
    #Fjerner alle ansatte før innsetting
    cursor.execute(
        "DELETE FROM Ansatt"
    )
    #Innsetning av Ansatt
    cursor.execute(
        "INSERT INTO Ansatt VALUES (1, 'Mina Rype Stokke', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (2, 'Yury Butusov', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (3, 'Eivind Myren', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (4, 'Aleksandr Shishkin-Hokusai', 'NULL', 'Fast')")
    

    cursor.execute(
        "INSERT INTO Ansatt VALUES (5, 'Arturo Scotti', 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (6, 'Ingunn Beate Strige Øyen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (7, 'Hans Petter Nilsen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (8, 'Madeleine Brandtzæg Nilsen', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (9, 'Synnøve Fossum Eriksen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (10, 'Emma Caroline Deichmann', 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (11, 'Thomas Jensen Takyi', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (12, 'Per Bogstad Gulliksen', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (13, 'Isak Holmen Sørensen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (14, 'Fabian Heidelberg Lunde', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (15, 'Emil Olafsson', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (16, 'Snorre Ryen Tøndel', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (17, 'Sunniva Du Mond Nordal', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (18, 'Jo Saberniak', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (19, 'Marte.M Steinholt', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (20, 'Tor Ivar Hagen', 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (21, 'Trond-Ove Skrødal', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (22, 'Natalie Grøndahl Tangen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (23, 'Åsmund Flaten', 'NULL', 'Innleid')")
    

    cursor.execute(
        "INSERT INTO Ansatt VALUES (24, 'Jonas Corell Petersen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (25, 'David Gehrt', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (26, 'Gaute Tønder', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (27, 'Magnus Mikaelsen', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (28, 'Kristoffer Spender', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (29, 'Elisabeth Egseth Hansen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatt VALUES (30, 'Lars Kirksæther','NULL', 'Fast')")
    
def addHarOppgave():
    #Fjerner alle HarOppgaver før innsetting
    cursor.execute(
        "DELETE FROM HarOppgave"
    )
    #Innsetning av HarOppgave
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '1', 'Dramaturg')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '2', 'Regi og Musikkutvelgelse')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '3', 'Lysdesign')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '4', 'Scenografi og Kostymer')")
    
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '5', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '6', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '7', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '8', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '9', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '10', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '11', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '12', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '13', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '14', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '15', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('1', '16', 'Skuespiller')")
    
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '17', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '18', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '19', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '20', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '21', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '22', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '23', 'Skuespiller')")
    
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '24', 'Regi')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '25', 'Scenografi og Kostymer')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '26', 'Musikalsk ansvarlig')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '27', 'Lysdesign')")
    cursor.execute(
        "INSERT INTO HarOppgave VALUES ('2', '28', 'Dramaturg')")
   
def addKunde():
    #Fjerner alle kunder før innsetting
    cursor.execute(
        "DELETE FROM Kunde"
    )
    #Innsetning av kunde
    cursor.execute(
        "INSERT INTO Kunde VALUES ('1', 'Eivind Holmen', '94129340', 'Klaebuveien 49')")
    cursor.execute(
        "INSERT INTO Kunde VALUES ('2', 'Åsmund Løvoll', '95239450', 'Mollenbergveien 8')")
    cursor.execute(
        "INSERT INTO Kunde VALUES ('3', 'Tobias Borning', '98593210', 'Gloshaugveien 5')")
    cursor.execute(
        "INSERT INTO Kunde VALUES ('4', 'Ola Nordmann', '94129340', 'Klaebuveien 48')")
    
def addTeaterStykke():    
    #Fjerner alle teaterstykker før innsetting
    cursor.execute("DELETE FROM TeaterStykke")
    #Innsetning av teaterstykke
    cursor.execute(
        "INSERT INTO TeaterStykke VALUES (1,'Størst av alt er kjærligheten', '2')") #Størst av alt er kjærligheten har id 1
    cursor.execute(
        "INSERT INTO TeaterStykke VALUES (2,'Kongsemnene', '1')") #Kongsemnene har id 2
    
def addTeaterOppsettning():
    #Fjerner alle teateroppsetninger før innsetting
    cursor.execute(
        "DELETE FROM TeaterOppsettning"
    )
    #Innsetning av teateroppsetning
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('03-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('06-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('07-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('12-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('13-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('14-02-2024', '1')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('01-02-2024', '2')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('02-02-2024', '2')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('03-02-2024', '2')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('05-02-2024', '2')")
    cursor.execute(
        "INSERT INTO TeaterOppsettning VALUES ('06-02-2024', '2')")

def addAkt():
    #Fjerner alle akt før innsetting
    cursor.execute(
        "DELETE FROM Akt"
    )
    #Innsetning av Akter
    cursor.execute(
        "INSERT INTO Akt VALUES (1, '2', 'Intro')")
    cursor.execute(
        "INSERT INTO Akt VALUES (2, '2', 'Midt 1')")
    cursor.execute(
        "INSERT INTO Akt VALUES (3, '2', 'Midt 2')")
    cursor.execute(
        "INSERT INTO Akt VALUES (4, '2', 'Midt 3')")
    cursor.execute(
        "INSERT INTO Akt VALUES (5, '2', 'Avslutning')")
    cursor.execute(
        "INSERT INTO Akt VALUES (1, '1', 'Kjærlighet')")

def addRolleIAkt():
    #Fjerner alle roller i akt før innsetting
    cursor.execute(
        "DELETE FROM RolleIAkt"
    )
    #Innsetning av Roller i Akter
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '1')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '1')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '1')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '1')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '1')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '14')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '14')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '14')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '14')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '14')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '13')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '6')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '6')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '6')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '7')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '3')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '3')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '3')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '3')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '3')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '2')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '2')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '10')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '10')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '10')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '4')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('', '2', '4')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '9')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '9')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '9')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '9')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '9')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '5')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '5')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '5')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '5')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '5')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '8')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('2', '2', '8')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '8')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '15')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '15')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '15')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '11')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '11')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '2', '11')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('5', '2', '11')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('3', '2', '12')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('4', '2', '12')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '16')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '17')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '18')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '19')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '20')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '21')")
    cursor.execute(
        "INSERT INTO RolleIAkt VALUES ('1', '1', '22')")
    
def addPrisTabell():
    #Fjerner alle priser før innsetting
    cursor.execute(
        "DELETE FROM PrisTabell"
    )
    #Innsetning av pris tabell
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', 'Ordinær', '350')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', 'Honnør', '300')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', 'Student', '220')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', 'Barn', '220')")
    # cursor.execute(                                       fjernes, skal håndteres av applikasjon
    #    "INSERT INTO PrisTabell VALUES ('1', '5', '320')") 
    # cursor.execute(
    #    "INSERT INTO PrisTabell VALUES ('1', '6', '270')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', 'Ordinær', '450')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', 'Honnør', '380')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', 'Student', '280')")
    # cursor.execute(                                       fjernes, skal håndteres av applikasjon
    #    "INSERT INTO PrisTabell VALUES ('2', '4', '420')")
    # cursor.execute(
    #     "INSERT INTO PrisTabell VALUES ('2', '5', '360')")

def addSalAndSete():
    # Slett alt i TeaterSal og Sete
    cursor.execute('DELETE FROM TeaterSal')
    cursor.execute('DELETE FROM Sete')
    seteID = 0

    # --------------------- HOVEDSCENE -----------------------

    # Opprett Hovedscene
    cursor.execute("INSERT INTO TeaterSal VALUES (1,'Hovedscenen')")

    # Parkett hovedscenen
    seteNr = 0
    for radNr in range(1,19): # rad 1-18
        for i in range(0,28): # fyller radene
            seteNr += 1
            seteID += 1
            if (seteNr in range(467,471) or seteNr in range(495,499)): # sete 1 - 504
                print(f"Did not insert:{seteNr}")
            else:
                cursor.execute("INSERT INTO Sete VALUES (?,1,?,?,'Parkett')", (seteID, seteNr, radNr))

    # Galleri øvre
    for i in range(505,525): # sete 505 - 524
        seteNr += 1
        seteID += 1
        if (seteNr < 515):
            cursor.execute("INSERT INTO Sete VALUES (?,1,?,?,'Galleri Nedre')", (seteID, seteNr, radNr))
        else:
            cursor.execute("INSERT INTO Sete VALUES (?,1,?,?,'Galleri Øvre')", (seteID, seteNr, radNr))

    # --------------------- GAMLE SCENE -----------------------

    # Opprett Gamle Scene
    cursor.execute("INSERT INTO TeaterSal VALUES (2,'Gamle Scene')")

    # Parkett
    for radNr in [1,4,5,7]: #Rader med 18 seter
        for seteNr in range(1,19): 
            seteID += 1
            cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Parkett')",(seteID, seteNr,radNr))

    for radNr in [3,6,8,9]: #Rader med 17 seter
        for seteNr in range(1,18): 
            seteID += 1
            cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Parkett')",(seteID, seteNr,radNr))

    for seteNr in range(1,17): # Rad med 16 seter
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Parkett')",(seteID, seteNr,2))

    for seteNr in range(1,15): # Rad med 14 seter
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Parkett')",(seteID, seteNr,10))

    # Balkong
    for seteNr in range(1,29): # 1-29 rad 1
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Balkong')",(seteID, seteNr,1))

    for seteNr in range(1,28): # 1-28 rad 2
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Balkong')",(seteID, seteNr,2))

    for seteNr in range(1,23): # 1-22 rad 3
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Balkong')",(seteID, seteNr,3))

    for seteNr in range(1,18): # 1-17 rad 4
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Balkong')",(seteID, seteNr,4))

    # Galleri 
    for seteNr in range(1,34): # 1-33 rad 1
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Galleri')",(seteID, seteNr,1))

    for seteNr in range(1,19): # 1-18 rad 1
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Galleri')",(seteID, seteNr,2))

    for seteNr in range(1,18): # 1-17 rad 1
        seteID += 1
        cursor.execute("INSERT INTO Sete VALUES (?,2,?,?,'Galleri')",(seteID, seteNr,3))

def buy9Tickets():
    cursor.execute("SELECT COUNT(*) FROM Ordre")
    num_orders = cursor.fetchone()[0]

    # Bruk antall eksisterende ordre + 1 som OrdreID for den nye ordren
    ordre_id = num_orders + 1

    # legg til ny ordre
    cursor.execute(
        "INSERT INTO Ordre VALUES (?, '10:00', '03-02-2024', 9, 3150, 4)", (ordre_id,)
    )

    # Count the number of existing tickets
    cursor.execute("SELECT COUNT(*) FROM Billett")
    num_tickets = cursor.fetchone()[0]

    # legg til billetter
    for i in range(9):
        # Bruk antall eksisterende billetter + 1 som BillettNr for den nye billetten
        billett_nr = num_tickets + 1 + i
        cursor.execute("INSERT INTO Billett VALUES (?,1,'03-02-2024',?,'Ordinær',1,350)", (billett_nr, 525+billett_nr))

def upload():
    addSalAndSete() 
    addTeaterStykke() 
    addTeaterOppsettning() 
    addAnsatte()
    addSkuespillere()
    addDirektor()
    addRolle() 
    addHarRolle()
    addAkt()
    addRolleIAkt()
    addHarOppgave()
    addKunde()
    addPrisTabell()
    buy9Tickets()
    

upload()
conn.commit()
conn.close()
