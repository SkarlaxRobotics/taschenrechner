import re
import math
def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+","-","*","/","^", "!"]
    x=True
    for i in rechnung:
        if i.isdigit() or i == "." :
            zahl += i 
        elif i == "-"  and x==True:
            zahl += "-"
        elif i in o:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
        if i in o:
            x=True
        elif x==True and i==" ":
            x=True
        else:
            x=False
    if zahl:
        zahlen.append(float(zahl))
    print(zahlen, operatoren)
    return zahlen, operatoren



def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe"
    ergebnis = loese(rechnung)
    return ergebnis
    

