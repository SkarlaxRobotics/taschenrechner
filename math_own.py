import math

def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    for i,c in enumerate (rechnung):
        if i.isdigit() or i == ".":
            zahl += i
        elif c == "-" and (i == 0 or not rechnung[i-1].isdigit()):
            zahl = "-"
        elif i in ["+","-","*","/","**2"]:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(c)
    if zahl:
        zahlen.append(float(zahl))
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
        if op == "+":
            zahlen[0] += zahl
        elif op == "-":
            zahlen[0] -= zahl
            if zahlen[0]==0:
                zahlen[0]=zahlen[0]*1
            else:
                zahlen[0]=zahlen[0]*-1
    return zahlen[0]

def quadrieren(zahlen):
    ergebnis = [] #später gucken ob klappt
    for zahl in zahlen:
        ergebnis.append(zahl**2)
    return ergebnis

def wurzel(zahlen):
    ergebnis = [] #""""""
    for zahl in zahlen:
        ergebnis.append(math.sqrt(zahl))
    return ergebnis

def potenz(zahlen):
    result = zahlen[0]
    for zahl in zahlen[1:]:
        ergebnis = ergebnis ** zahl
    return ergebnis


def trigonometric_function():

    angle = float(input)
    angle_radian = math.radians(angle)

    # Berechnung der trigonometrischen Funktionen
    sin_value = math.sin(angle_radian)
    cos_value = math.cos(angle_radian)
    tan_value = math.tan(angle_radian)
