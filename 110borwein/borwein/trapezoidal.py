##
## EPITECH PROJECT, 2021
## trapezoidal
## File description:
## trapezoidal part of the project
##

from borwein.main_formula import borweinFormula
from math import pi

def trapezoidalFormula(result, nb):
    f = 5000
    res = ((result * 2) + borweinFormula(nb, 0) + borweinFormula(nb, f)) * (f / 20000)
    return (res)

def Trapezoidal(nb):
    k = 1
    result = 0
    h = 5000 / 10000
    while k < 10000:
        result += borweinFormula(nb, k * h)
        k += 1
    result = trapezoidalFormula(result, nb)
    print ("\nTrapezoidal:\nI%.0f = %.10f" % (nb, result))
    print ("diff = %.10f" % (abs((result - (pi / 2)))))