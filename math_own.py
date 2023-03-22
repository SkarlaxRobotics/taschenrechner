import math

def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    for i in rechnung:
        if i.isdigit() or i == ".":
            zahl += i 
        elif i in ["+","-","*","/","**2"]:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
    if zahl:
        zahlen.append(float(zahl))
    return zahlen, operatoren

def main(rechnung):
    zahlen, operatoren = split_taschenrechner(rechnung)
    for o in range(len(operatoren)):
        if operatoren[o] == '+':
            addieren(zahlen)
        if operatoren[o] == '-':
            subtrahieren(zahlen)
        if operatoren[o] == '/':
            dividieren(zahlen)
        if operatoren[o] == '*':
            multiplizieren(zahlen)


def addieren(zahlen):
    ergebnis = 0
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis

def subtrahieren(zahlen):
    ergebnis = zahlen[0]
    for i in range (1, len(zahlen)):
        ergebnis -= zahlen[1]
    return ergebnis

def multiplizieren(zahlen):
    ergebnis = 1
    for zahl in zahlen:
        ergebnis *= zahl
    return ergebnis

def dividieren(zahlen):
    ergebnis = zahlen[0]
    if zahlen == 0:
        print('matheatischer fehler')
    else:
        for i in range(1, len(zahlen)):
            ergebnis /= zahlen[i]
        return ergebnis

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
