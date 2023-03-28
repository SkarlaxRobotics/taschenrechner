from math_own import *

def testNichts():
    result = main("")
    assert result == "Bitte Eingabe"

def testMinus():
    result = main("4 - 4")
    assert result == 0

def testPlus():
    result = main("4 + 4")
    assert result == 8

def testFakultaet():
    result = main("4 !")
    assert result == 24

def testKlammer():
    result = main("2 * ( 2 + 3 )")
    assert result == 24

def testFakultaet():
    result = main("4 !")
    assert result == 24
