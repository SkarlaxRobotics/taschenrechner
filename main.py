import flask
from flask import Flask, render_template, url_for, request
import math_own
import sqlite3

# Datenbank-Integration
conn = sqlite3.connect('history_calc.db')
cursor = conn.cursor()



table_name = 'history'
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
result = cursor.fetchone()

if result:
    print("Datenbank existiert bereits. fahre fort")
else:
    cursor.execute('CREATE TABLE history(number INTEGER, rechnung TEXT, ergebnis TEXT)')
    print("Database table wurde erstellt")





def rechner():
    x1 = int(input("Dein erste Zahl:"))
    operator = input("Rechenoperator:" )
    x2 = int(input("Deine zweite Zahl:"))
    if operator == "geteilt":
        print(x1/x2)
    if operator == "mal":
        print(x1*x2)
    if operator == "minus":
        print(x1-x2)
    if operator == "plus":
        print(x1+x2)


app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])

def index():
    return render_template("index.html")


@app.route("/result",methods = ['POST', 'GET'])
def result():
    conn = sqlite3.connect('history_calc.db')
    cursor = conn.cursor()
    output = request.form.to_dict()
    print(output)
    #ergebnis = output["num"]
    digit = str(output["digit"])
    ergebnis = math_own.main(digit)
    print(digit)
    cursor.execute('SELECT MAX(number) FROM history')
    letzte_number = cursor.fetchall()
    print(letzte_number)
    cursor.execute('INSERT INTO history VALUES (?, ?, ?)', (int(letzte_number+1), digit, ergebnis))
    conn.commit()
    cursor.execute('SELECT * FROM history')
    ausgabe = cursor.fetchone()
    print(ausgabe)
    #second_digit = float(output["sdigit"])
    #operator = str(output["operator"])
    #ergebnis = first_digit*second_digit
    cursor.close()
    conn.close()
    #math_own.math()
    return render_template("index.html", value=ergebnis)
    
'''math_own.math(operator, first_digit, second_digit)'''

if __name__ == '__main__':
    app.run(port=5001, debug=True)


