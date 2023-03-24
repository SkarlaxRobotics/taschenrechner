import re
def split_taschenrechner(rechnung):
    zahlen = []
    operatoren = []
    zahl = ""
    o = ["+","-","*","/","^"]
    for i in rechnung:
        if i.isdigit() or i == ".":
            zahl += i 
        elif i == "-"  and i-1 in o:
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

def regu(rechnung):
    regex = r""

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



    print("Zahlen:", zahlen)
    print("Operatoren:", operatoren)