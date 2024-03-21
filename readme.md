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


 