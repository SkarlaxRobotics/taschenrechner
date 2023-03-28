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
    assert result == 10

def testFakultaet():
    result = main("4 !")
    assert result == 24

def testPi():
    result = main("4 * n")
    assert result == 12.566370614359172

def testPowerof2():
    result = main("5 ^ 2")
    assert result == 25

def testRoot():
    result = main("8 ^ 0.5")
    assert result == 2.8284271247461903


def testPowerofX():
    result = main("8 ^ 8")
    assert result == 16777216.0