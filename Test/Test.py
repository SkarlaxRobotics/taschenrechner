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

def split_operands(expression):
    regex = r'([a-zA-Z]*)(\d+)([^\w\s]*)'
    matches = re.findall(regex, expression)
    results = []
    for match in matches:
        if match[0]:
            results.append((match[0], None))
        results.append((match[1], match[2]))
    return results

    # Ausgabe der Zahlen und Operatoren
    print("Zahlen:", zahlen)
    print("Operatoren:", operatoren)