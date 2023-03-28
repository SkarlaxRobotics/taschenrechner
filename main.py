import flask
from flask import Flask, render_template, request
import math_own
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
        db.openConnection()
        cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (int(number+1), rechnung, ergebnis))
        conn.commit()
        db.closeConnection()
    
    def deleteAllEntries(self, new_entry):
        db.openConnection()
        cursor.execute('DELETE FROM history')
        conn.commit()
        if new_entry: cursor.execute('INSERT INTO history VALUES (1, "new history", "empty")'); conn.commit()
        db.closeConnection()

    def readFromTable(self, number: str):
        db.openConnection()
        if number == "*":
            cursor.execute('SELECT * FROM history')
        else:
            cursor.execute('SELECT {number} FROM history')
        ausgabe = cursor.fetchone()
        db.closeConnection
        return ausgabe

    def getMaxNumber(self):
        db.openConnection()
        cursor.execute('SELECT MAX(number) FROM history')
        db.closeConnection()
        max = cursor.fetchone()
        global max_number
        max_number = int(max[0]) if max and max[0] is not None else 0



db = database("history_calc.db", "history")

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", history=reversed(database.readFromTable("*")), ergebnis="0")


@app.route("/result",methods = ['POST', 'GET'])
def result(debug=False):
    output = request.form.to_dict()
    
    if debug: print(output)
    
    digit = str(output["digit"])
    
    # Berechnung:
    ergebnis = math_own.main(digit)
    
    if debug: print("Ergebnis: ", ergebnis); print("Digit: ", digit)
    
    # getting max previous number
    max_number = database.getMaxNumber()
    if debug: print(max_number[0])
    a_max_number = int(sum(max_number[0])) if max_number[0] is not None else 0

    # verlauf erstellen
    database.insertToTable(number=int(a_max_number+1), rechnung=digit, ergebnis=ergebnis)

    last_ergebnis = ergebnis if ergebnis != "Mathematischer Fehler" and ergebnis != "Bitte Eingabe" else "0"
    if debug: print(last_ergebnis)

    return render_template("index.html", value=ergebnis, history=reversed(database.readFromTable("*")), last_ergebnis=last_ergebnis)


@app.route("/clear",methods = ['POST', 'GET'])
def clear():
    database.deleteAllEntries(True)
    return render_template("index.html", history=reversed(database.readFromTable("*")))


if __name__ == '__main__':
    app.run(port=5001, debug=True)