import math
import numpy as np
import matplotlib.pyplot as plt
def math(operator, fdigit, sdigit):
    if operator == "+":
        return fdigit+sdigit
    elif operator == "-":
        return fdigit-sdigit
    elif operator == "*":
        return fdigit*sdigit
    elif operator == "/":
        return fdigit/sdigit

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


def trigonometrische_funktionen(): 
    angle = float(input)
    angle_radian = math.radians(angle)
    sin_value = math.sin(angle_radian)
    cos_value = math.cos(angle_radian)
    tan_value = math.tan(angle_radian)

def solve_linear_gleichung(m, b):
    x = None
    y = None
    if m == 0:
        print("y = {}".format(b))
        return
    if b == 0:
        print("y = {}x".format(m))
        return
    x = -b / m
    y = m * x + b
    print("x = {}".format(x))
    print("y = {}".format(y))