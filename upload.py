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
    
    #Innsetning av hvem som har hvilke oppgaver
    cursor.execute(
        "INSERT INTO Ansatte VALUES ('Kristoffer Spender', 'NULL', 'Fast')")
   
    #Innsetning av akter
    
    #Innsetning av hvem som har hvilke roller
    cursor.execute(
        "INSERT INTO Rolle VALUES ('5', '1')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('6', '2')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('7', '3')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('8', '4')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('9', '5')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('10', '6')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('10', '7')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('11', '8')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('12', '9')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('13', '10')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('13', '11')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('14', '11')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('14', '12')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('15', '13')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('15', '14')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('16', '15')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('17', '16')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('18', '17')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('19', '18')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('20', '19')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('21', '20')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('22', '21')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('23', '22')")
    cursor.execute(
        "INSERT INTO Rolle VALUES ('24', '23')")
    
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
    