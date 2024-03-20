_Hvordan kjøre prosjektet:_

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



 