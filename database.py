import sqlite3

class database:
    def __init__(self, filename, table, debug=False) -> None:
        self.filename = filename
        self.openConnection()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        result = cursor.fetchone()
        if result: print("Datenbank existiert bereits. fahre fort")
        else:
            cursor.execute('CREATE TABLE history(number INTEGER, rechnung TEXT, ergebnis TEXT)')
            if debug: print("Database table wurde erstellt")
        cursor.execute('SELECT * FROM history WHERE number="1"')
        no_entry_yet = cursor.fetchall()
        if debug: print("no_entry_yet", no_entry_yet)
        if not no_entry_yet:
            cursor.execute('INSERT INTO history VALUES (1, "new history", "empty")')
            conn.commit()
        self.closeConnection()

    def openConnection(self):
        global conn
        conn = sqlite3.connect(self.filename)
        global cursor
        cursor = conn.cursor() 

    def closeConnection(self):
        cursor.close()
        conn.close()

    def insertToTable(self, number, rechnung, ergebnis):
        self.openConnection()
        cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (int(number+1), rechnung, ergebnis))
        conn.commit()
        self.closeConnection()
    
    def deleteAllEntries(self, new_entry):
        self.openConnection()
        cursor.execute('DELETE FROM history')
        conn.commit()
        if new_entry: cursor.execute('INSERT INTO history VALUES (1, "new history", "empty")'); conn.commit()
        self.closeConnection()

    def readFromTable(self, number: str):
        self.openConnection()
        if number == "*":
            cursor.execute('SELECT * FROM history')
        else:
            cursor.execute('SELECT {number} FROM history')
        ausgabe = cursor.fetchall()
        self.closeConnection
        return ausgabe

    def getMaxNumber(self):
        self.openConnection()
        cursor.execute('SELECT MAX(number) FROM history')
        max = cursor.fetchall()
        self.closeConnection()
        read =  int(sum(max[0])) if max and max[0] is not None else 0
        return read
