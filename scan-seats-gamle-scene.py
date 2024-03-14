import sqlite3

def insertIntoSql(file):
    conn = sqlite3.connect('teaterDB.db')
    cursor = conn.cursor()

    with open(file, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        if "Dato" in line:
            words = line.split()
            for word in words:
                if len(word) == 10 and word[4] == "-" and word[7] == "-":
                    date =  word
        # elif "Galleri" or "Parkett" in line: