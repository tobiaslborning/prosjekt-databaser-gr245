import sqlite3

def upload():
    conn = sqlite3.connect('teaterDB.db')
    cursor = conn.cursor()
    
    #Innsetning av skuspiller
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('5')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('6')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('7')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('8')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('9')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('10')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('11')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('12')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('13')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('14')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('15')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('16')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('17')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('18')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('19')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('20')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('21')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('22')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('23')")
    cursor.execute(
        "INSERT INTO Skuespiller VALUES ('24')")
    
    
    
    #Innsetning av direktør
    cursor.execute(
        "INSERT INTO Direktor VALUES ('25')")
    
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
    
    #Innsetning av roller
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Haakon Haakonssønn')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Inga fra Vartejg (Haakons Mor)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Skule jarl')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Fru Ragnhild (Skules hustru)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Margrete (Skules datter)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Sigrid (Skules søster)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Ingebjørg')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Biskop Nikolas')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Gregorius Jonssønn')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Paal Flida')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Trønder')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Baard Bratte')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Jatgeir Skald')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Dagfinn Bonde')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Peter (prest og Ingebjørgs sønn)')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Sunniva Du Mond Nordal')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Jo Saberniak')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Marte.M Steinholt')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Tor Ivar Hagen')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Trond-Ove Skrødal')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Natalie Grøndahl Tangen')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('Åsmund Flaten')")
    
    #Innsetning av ansatte
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Mina Rype Stokke', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Yury Butusov', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Eivind Myren', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Aleksandr Shishkin-Hokusai, 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Arturo Scotti, 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Ingunn Beate Strige Øyen, 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Hans Petter Nilsen, 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Madeleine Brandtzæg Nilsen, 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Synnøve Fossum Eriksen, 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Emma Caroline Deichmann, 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Thomas Jensen Takyi', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Per Bogstad Gulliksen', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Isak Holmen Sørensen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Fabian Heidelberg Lunde', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Emil Olafsson', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Snorre Ryen Tøndel', 'NULL', 'Fast')")
    
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Sunniva Du Mond Nordal', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Jo Saberniak', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Marte.M Steinholt', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Tor Ivar Hagen', 'NULL', 'Midlertidig')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Trond-Ove Skrødal', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Natalie Grøndahl Tangen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Åsmund Flaten', 'NULL', 'Innleid')")
    
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Jonas Corell Petersen', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('David Gehrt', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Gaute Tønder', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Magnus Mikaelsen', 'NULL', 'Innleid')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Kristoffer Spender', 'NULL', 'Fast')")
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Elisabeth Egseth Hansen', 'NULL', 'Fast')")
    
    #Innsetning av HarOppgave
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '1', 'Dramaturg')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '2', 'Regi og Musikkutvelgelse')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '3', 'Lysdesign')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '4', 'Scenografi og Kostymer')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '5', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '6', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '7', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '8', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '9', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '10', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '11', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '12', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '13', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '14', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '15', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('1', '16', 'Skuespiller')")
    
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '17', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '18', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '19', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '20', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '21', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '22', 'Skuespiller')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '23', 'Skuespiller')")
    
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '24', 'Regi')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '25', 'Scenografi og Kostymer')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '26', 'Musikalsk ansvarlig')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '27', 'Lysdesign')")
    cursor.execute(
        "INSERT INTO HarOppgaver VALUES ('2', '28', 'Dramaturg')")
   
   

    #Innsetning av kunde
    cursor.execute(
        "INSERT INTO Kunde VALUES ('1', 'Eivind Holmen', '94129340', 'Klaebuveien 49')")
    cursor.execute(
        "INSERT INTO Kunde VALUES ('2', 'Åsmund Løvoll', '95239450', 'Mollenbergveien 8')")
    cursor.execute(
        "INSERT INTO Kunde VALUES ('3', 'Tobias Borning', '98593210', 'Gloshaugveien 5')")

    
    
    
   
    #Innsetning av saler
    cursor.execute(
        "INSERT INTO TeaterSal VALUES ('Hovedscenen')")
    cursor.execute(
        "INSERT INTO TeaterSal VALUES ('Gamle Scene')")
    
    #Innsetning av teaterstykke
    cursor.execute(
        "INSERT INTO TeaterStykke VALUES ('Størst av alt er kjærligheten', '2')")
    cursor.execute(
        "INSERT INTO TeaterStykke VALUES ('Kongsemnene', '1')")
    
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

    #Innsetning av Akter
    cursor.execute(
        "INSERT INTO Akt VALUES ('2', 'Intro')")
    cursor.execute(
        "INSERT INTO Akt VALUES ('2', ''Midt 1)")
    cursor.execute(
        "INSERT INTO Akt VALUES ('2', 'Midt 2')")
    cursor.execute(
        "INSERT INTO Akt VALUES ('2', 'Midt 3')")
    cursor.execute(
        "INSERT INTO Akt VALUES ('2', 'Avslutning')")
    cursor.execute(
        "INSERT INTO Akt VALUES ('1', 'Kjærlighet')")
    
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
    
    #Innsetning av pris tabell
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '1', '350')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '2', '300')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '3', '220')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '4', '220')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '5', '320')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('1', '6', '270')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', '1', '450')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', '2', '380')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', '3', '280')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', '4', '420')")
    cursor.execute(
        "INSERT INTO PrisTabell VALUES ('2', '5', '360')")
    
    
    