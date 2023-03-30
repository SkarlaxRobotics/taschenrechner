import math
from rechnungen import *
from split import *
from math_own import *
def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe" 
    else:
        try:
            ergebnis= math_own.berechne_klammern(rechnung)
            return ergebnis
        except:
            return "Fehler! Bist du doof?!"