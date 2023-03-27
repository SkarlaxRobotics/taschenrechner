import math
import re

def split_taschenrechner(rechnung):

    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+","-","*","/","^", "!"]
    x=True
    y=False
    n="%s" % math.pi 
    
    for i in rechnung:
        if rechnung[-2] in o and rechnung[-2]!="!":
            return "Syntax Error"
        elif i.isdigit() or i == ".":
            zahl += i 
        elif i=="n":
            if rechnung[rechnung.index(i)-2] in o:
                zahl += n
            else:
                zahlen.append(float(zahl))
                operatoren.append("*")
                zahl = ""
                zahl += n
        elif (i =="-" or i=="+" )and x==True:
            zahl += i
        elif i in o:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
        if i in o and y==False and x==False:
            x=True
        elif i in o and x==True and y==False:
            y=True
        elif i in o and y==True:
            return "Syntax Error"
        elif x==True and i==" ":
            x=True
        else:
            x=False
            y=False

    if zahl:
        zahlen.append(float(zahl))
    # print(zahlen, operatoren)
    return zahlen, operatoren


def main(rechnung):
    if not rechnung:
        return "Bitte Eingabe" 
    ergebnis = loese(rechnung)
    return ergebnis
    
def loese(rechnung):
    if split_taschenrechner(rechnung)=="Syntax Error":
        return "Syntax Error"
    else:
        zahlen, operatoren = split_taschenrechner(rechnung)
    while "!" in operatoren:
        for i in rechnung:
            if rechnung[rechnung.index(i)-2] == "-":
                return "Mathematischer Fehler"
        for i, op in enumerate(operatoren):
            if op == "!":
                    if i == "0":
                        zahlen[i]=1
                        del operatoren[i]
                    else:
                        zahlen[i]=math.factorial(int(zahlen[i]))
                        del operatoren[i]
    
    while "%" in operatoren:
        for i, op in enumerate(operatoren):
            if op == "%":
                zahlen[i]=zahlen[i]/100
                del operatoren[i]

    while "^" in operatoren:
        for i, op in enumerate(operatoren):
            if op == "^":
                zahlen[i] = math.pow(zahlen[i],zahlen[i+1])
                del zahlen[i+1]
                del operatoren[i]
                break
    
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


    math.exp 

def Fakultät (rechnung, zahlen, operatoren):
    for i in rechnung:
            if rechnung[rechnung.index(i)-2] == "-":
                return "Mathematischer Fehler"
    for i, op in enumerate(operatoren):
            if op == "!":
                    if i == "0":
                        zahlen[i]=1
                        del operatoren[i]
                    else:
                        zahlen[i]=math.factorial(int(zahlen[i]))
                        del operatoren[i]

def Prozent (zahlen, operatoren):
     for i, op in enumerate(operatoren):
            if op == "%":
                zahlen[i]=zahlen[i]/100
                del operatoren[i]

def Potenz (zahlen, operatoren):
     for i, op in enumerate(operatoren):
            if op == "%":
                zahlen[i]=zahlen[i]/100
                del operatoren[i]