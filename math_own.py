import math
import re
from rechnungen import *
from split import *

def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe" 
    try:
        berechne_klammern(rechnung)
    except:
        print("Fehler")
    else:
        ergebnis = berechne_klammern(rechnung)
        return ergebnis
    
def loese(rechnung):
    if split.split_rechnung(rechnung)=="Syntax Error":
        return "Syntax Error"
    
    else:
        zahlen, operatoren = split.split_rechnung(rechnung)

    while "!" in operatoren:
        rechnungen.berechne_fakultaet(rechnung, zahlen, operatoren)

    while "%" in operatoren:
        rechnungen.berechne_prozent(zahlen, operatoren)

    while "^" in operatoren:
        rechnungen.berechne_potenz(zahlen, operatoren)
    
    while "*" in operatoren or "/" in operatoren:
        rechnungen.berechne_dividierenundmultiplizieren(zahlen, operatoren)

    while len(operatoren) > 0:
        rechnungen.berechne_plusminus(zahlen, operatoren)

    return zahlen[0]    
    
    
def berechne_klammern(rechnung):
    if "(" in rechnung and ")" in rechnung:
        start = rechnung.index("(")
        end = rechnung.rindex(")")
        inner_rechnung = rechnung[start+1:end]
        result = berechne_klammern(inner_rechnung)
        rechnung = rechnung[:start] + str(result) + rechnung[end+1:]
        return berechne_klammern(rechnung)
    else:
        return loese(rechnung)
    
