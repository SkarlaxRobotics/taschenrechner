import math
import re
import rechnungen
import split

def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe" 
    ergebnis = loese(rechnung)
    return ergebnis
    
def loese(rechnung):
    if split.split_rechnung(rechnung)=="Syntax Error":
        return "Syntax Error"
    else:
        zahlen, operatoren = split.split_rechnung(rechnung)
    while "!" in operatoren:
        rechnungen.fakultaet(rechnung, zahlen, operatoren)
    while "%" in operatoren:
        rechnungen.prozent(zahlen, operatoren)

    while "^" in operatoren:
        rechnungen.potenz(zahlen, operatoren)
    
    while "*" in operatoren or "/" in operatoren:
        rechnungen.dividierenundmultiplizieren(zahlen, operatoren)

    while len(operatoren) > 0:
        rechnungen.plusminus(zahlen, operatoren)

    return zahlen[0]    
    

