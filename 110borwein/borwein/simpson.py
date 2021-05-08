##
## EPITECH PROJECT, 2021
## simpson
## File description:
## simpson part
##

from borwein.main_formula import borweinFormula
from math import pi

def simpsonFormula(result1, result2, nb):
    f = 5000
    res = ((result1 * 4) + (result2 * 2) + borweinFormula(nb, 0) + borweinFormula(nb, f)) * (f / 60000)
    return (res)

def Simpson(nb):
    k = 0
    result1 = 0
    result2 = 0
    resultf = 0
    h =  5000 / 10000
    while k < 10000:
        result1 += borweinFormula(nb, (k * h) + (h / 2))
        k += 1
    k = 1
    while k < 10000:
        result2 += borweinFormula(nb, (k * h))
        k += 1
    resultf = simpsonFormula(result1, result2, nb)
    print ("\nSimpson:\nI%.0f = %.10f" % (nb, resultf))
    print ("diff = %.10f" % (abs((resultf - (pi / 2)))))
