##
## EPITECH PROJECT, 2021
## main_formula
## File description:
## main formula of the project
##

from math import sin

def sinusFormula(elem, i):
    result = sin(elem / (2 * i + 1)) / (elem / (2 * i + 1))
    return (result)

def borweinFormula(nb, elem):
    i = 0
    result = 1
    while i <= nb:
        if elem != 0:
            result *= sinusFormula(elem, i)
        i += 1;
    return (result)