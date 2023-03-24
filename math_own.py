import math
import re
# def split_taschenrechner(rechnung):
#     zahlen = []
#     operatoren = []
#     zahl = ""
#     o = ["+","-","*","/","^"]
#     for i in rechnung:
#         if i.isdigit() or i == ".":
#             zahl += i 
#         elif i == "-"  and i-1 in o:
#             zahl += "-"
        
#         elif i in o:
#             if zahl:
#                 zahlen.append(float(zahl))
#                 zahl = ""
#             operatoren.append(i)
#     if zahl:
#         zahlen.append(float(zahl))
#     print(zahlen, operatoren)
#     return zahlen, operatoren

def regu(rechnung):
    regex = r"\\(- [0-9]+ \\+ n\\) \\* [0-9]+ \\^ [0-9]+ \\^ [0-9]+ - - [0-9]+"

    matches = re.finditer(regex, rechnung)

    zahlen = []
    operatoren = []

    for match in matches:
        for group in range(1, 5):
            token = match.group(group)
            if token:
                if token.isnumeric() or '.' in token:
                    zahlen.append(token)
                else:
                    operatoren.append(token)

    # Ausgabe der Zahlen und Operatoren
    print("Zahlen:", zahlen)
    print("Operatoren:", operatoren)

def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    x="%s" % math.pi
    for i in rechnung:
        if i.isdigit() or i == "." :
            zahl += i 
        elif i == "n":
            zahl += x
        elif i in ["+","-","*","/","^"]:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
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