import math

class Trig:
    def __init__(self, op, zahlen) -> None:
        self.op = op
        self.zahlen = zahlen
        
    def rechnen(self):
        for i, op in enumerate(self.op):
            if op == "sin":
                self.zahlen[i]=round(math.sin(math.radians(self.zahlen[i])),3)
            elif op == "cos":
                self.zahlen[i]=round(math.cos(math.radians(self.zahlen[i])),3)
            elif op == "tan":
                self.zahlen[i]=round(math.tan(math.radians(self.zahlen[i])),3)
            del self.op[i]