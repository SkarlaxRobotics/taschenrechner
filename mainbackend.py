import math
from rechnungen import *
from split import *
from math_own import *


def main(rechnung: str):
    if not rechnung:
        return "Bitte Eingabe" 
    else:
        try:
            ergebnis= berechne_klammern(rechnung)
            return ergebnis
        except:
            return "Fehler! Bist du doof?!"