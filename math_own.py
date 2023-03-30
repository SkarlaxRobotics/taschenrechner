import math
from rechnungen import *
from split import *

def loese(rechnung):
    if split.split_rechnung(rechnung)=="Syntax Error":
        return "Syntax Error"
    
    else:
        zahlen, operatoren = split.split_rechnung(rechnung)

    while "!" in operatoren:
        if rechnungen.berechne_fakultaet(rechnung, zahlen, operatoren)=="Mathematischer Fehler":
            return "Mathematischer Fehler"
        else:
            rechnungen.berechne_fakultaet(rechnung, zahlen, operatoren)

    while "sin" in operatoren:
        rechnungen.berechne_sinus(zahlen, operatoren)

    while "cos" in operatoren:
        rechnungen.berechne_cosinus(zahlen, operatoren)

    while "tan" in operatoren:
        rechnungen.berechne_tangens(zahlen, operatoren)

    while "%" in operatoren:
        rechnungen.berechne_prozent(zahlen, operatoren)

    while "^" in operatoren:
        rechnungen.berechne_potenz(zahlen, operatoren)
    
    while "*" in operatoren or "/" in operatoren:
        if rechnungen.berechne_dividierenundmultiplizieren(zahlen, operatoren)=="Mathematischer Fehler":
            return "Mathematischer Fehler"
        else:
            rechnungen.berechne_dividierenundmultiplizieren(zahlen, operatoren)

    while len(operatoren) > 0:
        rechnungen.berechne_plusminus(zahlen, operatoren)

    return zahlen[0]    

def berechne_klammern(rechnung):
    if rechnung.count("(")<rechnung.count(")") or rechnung.count("(")>rechnung.count(")"):
        return "Syntax Fehler"
    elif "(" in rechnung and ")" in rechnung:
        start = rechnung.index("(")
        end = rechnung.rindex(")")
        inner_rechnung = rechnung[start+1:end]
        result = berechne_klammern(inner_rechnung)
        rechnung = rechnung[:start] + str(result) + rechnung[end+1:]
        return berechne_klammern(rechnung)
    else:
        return loese(rechnung)

