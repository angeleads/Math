##
## EPITECH PROJECT, 2021
## midpoint
## File description:
## midpoint function
##

from borwein.main_formula import borweinFormula
from math import pi

def Midpoint(nb):
    k = 0
    j = 0
    h = 5000 / 10000
    result = 0
    while k < 10000:
        result += (h * borweinFormula(nb, j + h / 2))
        k += 1
        j += h
    print ("Midpoint:\nI%.0f = %.10f" % (nb, result))
    print ("diff = %.10f" % (abs((result - (pi / 2)))))