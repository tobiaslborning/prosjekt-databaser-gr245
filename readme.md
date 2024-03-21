# TDT4145 - Gruppe 245 - DB2 
### Gruppemedlemer
- Åsmund Løvoll
- Eivind Biti Holmen
- Tobias Liene Borning

## Generell Info
Denne zip filen inneholder __alt__ som er knyttet til leveransen  
- Databasen vår er lagret i filen `teaterDB.db`  
- Tekstlig output fra spørringene er lagret i `tekstlig_output.txt`
- Guide på hvordan en kjører prosjektet står under, pass på at terminalen er startet i samme mappe `(/prosjekt-databaser-gr245)`, som alle python filene, samt databasen befinner seg.
- SQL filene til spørringene i oppgave 5,6 og 7 ligger i `queries` mappa, men disse er også implementer i selve programmet.
## Hvordan kjøre prosjektet:

__Initialisering av database__
```bash
#naviger til /prosjekt-databaser-gr245

# Kjør db med sqlite3
% sqlite3 teaterDB.db

# Fjern alt fra databasen
% .read remove.sql

# Innsetting av tabeller
% .read insert.sql

# Naviger ut av sqlite
% .q
```
__Insetting i database__
```bash
# naviger til /prosjekt-databaser-gr245

# fyll databasen
% python3 upload.py # denne kan også brukes til å resette data i databasen
% python3 scan_seats_hovedscenen.py
% python3 scan_seats_gamle_scene.py
```

__Kjør programmet__

```bash
# naviger til /prosjekt-databaser-gr245

# kjør main
% python3 main.py

```

## Endringer i Databaseoppsettet

### Endret Sete-entiteten
Vi har endret Sete-entiteten slik at alle seter har en unik SeteID. Dette ble gjort for å redusere antall kolonner i Billett-tabellen og gjøre det enklere for applikasjonen å sjekke om et sete er opptatt ved billettkjøp.

### Endret Ordre-entiteten
Vi fjernet `NOT NULL` fra `pris` og `antall` i Ordre-entiteten da det ble mer hensiktsmessig å opprette en tom ordre først og deretter fylle inn pris og antall senere.
Vi endret også navnet på primærnøkkelen `OrdreID` til `OrdreNr`.

### Endret Billett-entiten
Endret primærnøkkelen __BillettNr__ fra `INT` til `INTEGER`, slik at det auto-incrementing av en primærnøkkel.

## Ekstra funksjonalitet

- Registrering av nye brukere er nå mulig.
- Et billettbooking-system er implementert.
- Oversikt over en ordre kan nå fås ved vanlig kjøring av programmet.

## Antakelser

### scan_seats_hovedscenen.py
Det er ingen kjøpte seter i galleriet, så de blir derfor ikke scannet. Fremgangsmåten ville likevel vært lik som for gamle scenen.

### Brukerhistorie 5
Det ble ansett som mest ryddig at brukeren av programmet kunne angi hvilket stykke de ønsket å se skuespillerne til. Dette ble implementert ved å legge til en enkel linje i spørringen: `WHERE Stykkenavn = “?”`.

### Brukerhistorie 7
Vi har antatt at resultatet skal være en oversikt over alle skuespillere den inntastede skuespilleren har spilt med, inkludert akten og stykke de spilte sammen i. 

### Baard Bratte 
_Baard Bratte_, spilt av _Fabian Heidelberg Lunde_ var ikke lagt til i noen av aktene, vi la derfor til _Baard Bratte_ i akt 3 og 4.

### Trønder
De to skuespillerne som spiller Trønder; _Fabian Heidelberg Lunde_ og _Isak Holmen Sørensen_ har vi antatt at spiller trønder i alle andre aktene der de ikke spiller hovedrollen sin. Dette gjorde at vi måtte lage to roller; _Tronder(1)_ og _Tronder(2)_ Slik at disse rollene blir unike.


 