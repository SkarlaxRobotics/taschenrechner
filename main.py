import flask
from flask import Flask, render_template, request
import math_own
import sqlite3
from database import *



db = database("history_calc.db", "history")

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", history=reversed(db.readFromTable(number="*")), ergebnis="0")


@app.route("/result",methods = ['POST', 'GET'])
def result(debug=False):
    output = request.form.to_dict()
    
    if debug: print(output)
    
    digit = str(output["digit"])

    # Berechnung:
    ergebnis = math_own.main(digit)

    if debug: print("Ergebnis: ", ergebnis); print("Digit: ", digit)
    
    # getting max previous number
    max_number = db.getMaxNumber()
    if debug: print(max_number)
    a_max_number = max_number if max_number is not None else 0

    # verlauf erstellen
    if digit == "1 + 1": db.insertToTable(number=int(a_max_number+1), rechnung="Nutzer", ergebnis="doof")
    else: db.insertToTable(number=int(a_max_number+1), rechnung=digit, ergebnis=ergebnis)

    last_ergebnis = "0" if type == str and ' ' in ergebnis else ergebnis
    if debug: print(last_ergebnis)

    return render_template("index.html", value=ergebnis, history=reversed(db.readFromTable("*")), last_ergebnis=last_ergebnis)


@app.route("/clear",methods = ['POST', 'GET'])
def clear():
    db.deleteAllEntries(True)
    return render_template("index.html", history=reversed(db.readFromTable("*")))


if __name__ == '__main__':
    app.run(port=5001, debug=True)