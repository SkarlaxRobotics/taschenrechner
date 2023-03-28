from math_own import *

def testNothing():
    result = main("")
    assert result == "Bitte Eingabe"

def testSubtraction():
    result = main("4 - 4")
    assert result == 0

testNothing()
testSubtraction()
