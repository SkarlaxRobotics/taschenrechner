import re
def split_taschenrechner1(rechnung):
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
        elif i in ["+","-","*","/","^", "!"]:
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
    
    while "!" in operatoren:
        for i, op in enumerate(operatoren):
            if op == "!":
                    int(zahlen[i])
                    if i == "0":
                        zahlen[i]=1
                        del operatoren[i]
                    else:
                        zahlen[i]=math.factorial(zahlen[i])
                        del operatoren[i]
                # else:
                #     return "n muss eine positive ganze Zahl oder Null sein"