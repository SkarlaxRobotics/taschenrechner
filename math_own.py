import math

def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+","-","*","/","**2"]
    for i in rechnung:
        if i.isdigit() or i == ".":
            zahl += i 
        elif i == "-"  and i-1 in o:
            zahl = zahl * -1
        elif i in o:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
    if zahl:
        zahlen.append(float(zahl))
    print(zahlen, operatoren)
    return zahlen, operatoren

def main(rechnung):
    ergebnis = loese(rechnung)
    return ergebnis

def loese(rechnung):
    zahlen, operatoren = split_taschenrechner(rechnung)
    while "*" in operatoren or "/" in operatoren:
        for i, op in enumerate(operatoren):
            if op == "*":
                zahlen[i] = zahlen[i] * zahlen[i+1]
                del zahlen[i+1]
                del operatoren[i]
                break
            elif op == "/":
                if zahlen[i+1] == 0:
                    return "Mathematischer Fehler"
                zahlen[i] = zahlen[i] / zahlen[i+1]
                del zahlen[i+1]
                del operatoren[i]
                break
    while len(operatoren) > 0:
        op = operatoren.pop(0)
        zahl = zahlen.pop(0)
    for i, op in enumerate(operatoren):
        if op == "+":
            zahlen[i+1] = zahlen[i] + zahlen[i+1]
        elif op == "-":
            zahlen[i+1] = zahlen[i] - zahlen[i+1]
            i += 1
    return zahlen[-1]
