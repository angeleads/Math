##
## EPITECH PROJECT, 2021
## run_trigo
## File description:
## pointer function to run the trigo operations
##

from sys import argv
from trigo.trigo_operations import *
from matrix.tools import PrintMatrix

def RunTrigo(matrix):
    identify_trigo = ["EXP", "COS", "SIN", "COSH", "SINH"]
    function_trigo = [ExpOperation, CosOperation, SinOperation, CoshOperation, SinhOperation]
    for y in range(len(function_trigo)):
        if argv[1] == identify_trigo[y]:
            matrix = function_trigo[y](matrix)
    PrintMatrix(matrix)