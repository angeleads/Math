##
## EPITECH PROJECT, 2021
## trigo_operations
## File description:
## all the trigo operations
##

import math
from matrix.operations import *

def ExpOperation(matrix):
    temp = CheckMatrix(len(matrix))
    for y in range(1, 50):
        temp = SumMatrix(temp, DivMatrix(PowMatrix(matrix, y), math.factorial(y)))
    return temp

def CosOperation(matrix):
    temp = CheckMatrix(len(matrix))
    for y in range(1, 40):
        if y % 2 == 0:
            temp = SumMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y), math.factorial(2 * y)))
        else:
            temp = SubMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y), math.factorial(2 * y)))
    return temp

def SinOperation(matrix):
    temp = matrix
    for y in range(1, 40):
        if y % 2 == 0:
            temp = SumMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y + 1), math.factorial(2 * y + 1)))
        else:
            temp = SubMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y + 1), math.factorial(2 * y + 1)))
    return temp

def CoshOperation(matrix):
    temp = CheckMatrix(len(matrix))
    for y in range(1, 40):
        temp = SumMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y), math.factorial(2 * y)))
    return temp

def SinhOperation(matrix):
    temp = matrix
    for y in range(1, 40):
        temp = SumMatrix(temp, DivMatrix(PowMatrix(matrix, 2 * y + 1), math.factorial(2 * y + 1)))
    return temp