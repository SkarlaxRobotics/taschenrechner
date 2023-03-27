import flask
from flask import Flask, render_template, request
import math_own
import sqlite3


class database:
    def open_connection():
        global conn
        conn = sqlite3.connect('history_calc.db')
        global cursor
        cursor = conn.cursor() 

    def close_connection(self):
        cursor.close()
        conn.close()
        
    def insert_to_table(self): pass
    
    def delete_all_entries(self):
        database.open_connection()
        cursor.execute('DELETE FROM history')
        conn.commit()
        database.close_connection()

    def readFromTable(self): pass

    def getMaxNumber(self):
        database.open_connection()
        cursor.execute('SELECT MAX(number) FROM history')
        database.close_connection()
        max = cursor.fetchone()
        global max_number
        max_number = int(max[0]) if max and max[0] is not None else 0
    
    def __init__(self) -> None:
        database.open_connection()
        table_name = 'history'
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        if result:
            print("Datenbank existiert bereits. fahre fort")
        else:
            cursor.execute('CREATE TABLE history(number INTEGER, rechnung TEXT, ergebnis TEXT)')
            print("Database table wurde erstellt")
        cursor.execute('SELECT * FROM history WHERE number="1"')
        no_entry_yet = cursor.fetchall()
        print("no_entry_yet", no_entry_yet)
        if not no_entry_yet:
            cursor.execute('INSERT INTO history VALUES (1, "new history", "empty")')
            conn.commit()
        database.close_connection()




app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])


def index():
    # sqlite connection
    database.open_connection()
    cursor.execute('SELECT * FROM history')
    ausgabe = cursor.fetchall() 
    cursor.close()
    conn.close()
    reversed_ausgabe = reversed(ausgabe)

    return render_template("index.html", history=reversed_ausgabe, ergebnis="0")


@app.route("/result",methods = ['POST', 'GET'])
def result():
    # sqlite connection
    database.open_connection()
    
    output = request.form.to_dict()
    print(output)
    digit = str(output["digit"])
    ergebnis = math_own.main(digit)
    print("Ergebnis:", ergebnis)
    print(digit)
    
    # getting max previous number
    cursor.execute('SELECT MAX(number) FROM history')
    get_max_number = cursor.fetchall()
    print(get_max_number[0])
    max_number = int(sum(get_max_number[0])) if get_max_number[0] is not None else 0
    
    # verlauf erstellen
    cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (int(max_number+1), digit, ergebnis))
    conn.commit()
    cursor.execute('SELECT * FROM history')
    ausgabe = cursor.fetchall()
    print("Aktueller Verlauf:", ausgabe)
    
    last_ergebnis = ergebnis if ergebnis != "Mathematischer Fehler" and ergebnis != "Bitte Eingabe" else "0"
    print(last_ergebnis)

    cursor.close()
    conn.close()
    # ausgabe
    reversed_ausgabe = reversed(ausgabe)
    return render_template("index.html", value=ergebnis, history=reversed_ausgabe, last_ergebnis=last_ergebnis)


@app.route("/clear",methods = ['POST', 'GET'])
def clear():

    cursor.execute('INSERT INTO history VALUES (1, "new history", "empty")')
    conn.commit()
    cursor.execute('SELECT * FROM history')
    ausgabe = cursor.fetchall()
    reversed_ausgabe = reversed(ausgabe)
    cursor.close()
    conn.close()
    # ausgabe

    return render_template("index.html", history=reversed_ausgabe)


if __name__ == '__main__':
    app.run(port=5001, debug=True)


def get_max_number():
    cursor.execute('SELECT MAX(number) FROM history')
    return cursor.fetchone()


max_number = int(get_max_number()[0]) if get_max_number() and get_max_number()[0] is not None else 0

