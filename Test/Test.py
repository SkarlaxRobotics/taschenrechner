import re
import math
def split_taschenrechner1(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+","-","*","/","^"]
    for i in rechnung:
        z=rechnung[rechnung.index(i)-3]
        print(i)
        print(z)
        if i.isdigit() or i == ".":
            zahl += i 
        elif i == "-"  and z in o:
            zahl += "-"
        elif i in o:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
    if zahl:
        zahlen.append(float(zahl))
    print(zahlen, operatoren)
    return zahlen, operatoren


def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+", "-", "*", "/", "^"]
    last_was_op = True # flag to check if the last character was an operator
    for i in rechnung:
        if i.isdigit() or i == ".":
            zahl += i 
            last_was_op = False
        elif i in o:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            if not last_was_op:
                operatoren.append("+")
            operatoren.append(i)
            last_was_op = True
    if zahl:
        zahlen.append(float(zahl))
    return zahlen, operatoren



def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe"
    ergebnis = loese(rechnung)
    return ergebnis
    
def loese(rechnung):
    zahlen, operatoren = split_taschenrechner(rechnung)
    
    while "!" in operatoren:
        for i, op in enumerate(operatoren):
            if op == "!":
                    
                    if i == "0":
                        zahlen[i]=1
                        del operatoren[i]
                    else:
                        zahlen[i]=math.factorial(int(zahlen[i]))
                        del operatoren[i]
                # else:
                #     return "n muss eine positive ganze Zahl oder Null sein"

