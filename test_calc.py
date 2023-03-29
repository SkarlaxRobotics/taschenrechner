from math_own import *
from main import *

# execute with "python3 -m pytest" in directory of this file 

# math file tests
def testNichts():
    result = main("")
    assert result == "Bitte Eingabe"

def testMinus():
    result = main("4 - 4")
    assert result == 0

def testPlus():
    result = main("4 + 4")
    assert result == 8

def testGeteilt():
    result = main("4 / 4")
    assert result == 1

def testGeteiltWithZero():
    result = main("4 / 0")
    assert result == "Mathematischer Fehler"
    
def testMal():
    result = main("4 * 4")
    assert result == 16


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
    
def testProcent():
    result = main("74 % * 854 ")
    assert result == 631.96
    

def testSinus():
    result = main(" sin 30")
    assert result == 0.5

def testCosinus():
    result = main(" cos 60")
    assert result == 0.5

def testTangent():
    result = main(" tan 45")
    assert result == 1
    
    
# main file tests
def testOverflow():
    result = result("400 !", debug=False)
    assert result == 1
    