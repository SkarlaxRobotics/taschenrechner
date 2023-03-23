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

    regex = r"([a-zA-Z])|(-?\d+(\.\d+)?)|([+\-*/^()])|([^\d])"

    test_str = rechnung

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


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