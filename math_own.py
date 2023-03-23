import math
# def split_taschenrechner(rechnung):
#     zahlen = []
#     operatoren = []
#     zahl = ""
#     o = ["+","-","*","/","^"]
#     for i in rechnung:
#         if i.isdigit() or i == ".":
#             zahl += i 
#         elif i == "-"  and i-1 in o:
#             zahl[i]= zahl[i] * -1
#         elif i in o:
#             if zahl:
#                 zahlen.append(float(zahl))
#                 zahl = ""
#             operatoren.append(i)
#     if zahl:
#         zahlen.append(float(zahl))
#     print(zahlen, operatoren)
#     return zahlen, operatoren

def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    for i in rechnung:
        if i.isdigit() or i == ".":
            zahl += i 
        elif i in ["+","-","*","/","^"]:
            if zahl:
                zahlen.append(float(zahl))
                zahl = ""
            operatoren.append(i)
    if zahl:
        zahlen.append(float(zahl))
    return zahlen, operatoren

def main(rechnung):
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