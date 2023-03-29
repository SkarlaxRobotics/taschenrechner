import math
class split:
    def split_rechnung(rechnung):

        zahlen = []
        operatoren = []
        zahl = ""
        o = ["+","-","*","/","^", "!", "%"]
        x=True
        y=False
        n="%s" % math.pi 
        
        for i in rechnung:
            if rechnung[-2] in o and rechnung[-2]!="!":
                return "Syntax Error"
            if i==" " and rechnung[rechnung.index(i)-1].isdigit() and rechnung[rechnung.index(i)+1].isdigit() and zahl!="":
                    zahlen.append(float(zahl))
                    operatoren.append("*")
                    zahl = ""
            elif i.isdigit() or i == ".":
                zahl += i 
            elif i=="n" and rechnung[rechnung.index(i)-1]!= "i" and rechnung[rechnung.index(i)-1]!= "a":
                if rechnung[rechnung.index(i)-2] in o:
                    zahl += n
                else:
                    zahlen.append(float(zahl))
                    operatoren.append("*")
                    zahl = ""
                    zahl += n
            elif (i =="-" or i=="+" )and x==True:
                zahl += i
            elif i=="s" and rechnung[rechnung.index(i)+1]=="i" and rechnung[rechnung.index(i)+2]=="n":
                if zahl:
                    zahlen.append(float(zahl))
                    zahl = ""
                operatoren.append("sin")
            elif i=="c" and rechnung[rechnung.index(i)+1]=="o" and rechnung[rechnung.index(i)+2]=="s":
                if zahl:
                    zahlen.append(float(zahl))
                    zahl = ""
                operatoren.append("cos")
            elif i=="t" and rechnung[rechnung.index(i)+1]=="a" and rechnung[rechnung.index(i)+2]=="n":
                if zahl:
                    zahlen.append(float(zahl))
                    zahl = ""
                operatoren.append("tan")
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


