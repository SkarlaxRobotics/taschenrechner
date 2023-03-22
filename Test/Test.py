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

    # Sortiere Operatoren nach Reihenfolge der Operationen
    sorted_operators = []
    for op in ["**2", "/", "*", "+", "-"]:
        if op in operatoren:
            sorted_operators.append(op)

    return zahlen, sorted_operators

def berechne(rechnung):
    zahlen, operatoren = split_taschenrechner(rechnung)

    # Führe die Operationen in der richtigen Reihenfolge aus
    while "**2" in operatoren:
        idx = operatoren.index("**2")
        zahlen[idx] = zahlen[idx]**2
        del operatoren[idx]

    while "*"  or "/" in operatoren:

        if "*":
            

        idx = operatoren.index("*")
        zahlen[idx] = zahlen[idx] * zahlen[idx+1]
        del zahlen[idx+1]
        del operatoren[idx]


    while "+" in operatoren:
        idx = operatoren.index("+")
        zahlen[idx] = zahlen[idx] + zahlen[idx+1]
        del zahlen[idx+1]
        del operatoren[idx]

    while "-" in operatoren:
        idx = operatoren.index("-")
        zahlen[idx] = zahlen[idx] - zahlen[idx+1]
        del zahlen[idx+1]
        del operatoren[idx]

    return zahlen[0]
