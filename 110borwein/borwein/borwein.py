##
## EPITECH PROJECT, 2021
## borwein
## File description:
## main integrals calls
##

from borwein.midpoint import Midpoint
from borwein.trapezoidal import Trapezoidal
from borwein.simpson import Simpson

def borwein(argv):
    Midpoint(int(argv[1]))
    Trapezoidal(int(argv[1]))
    Simpson(int(argv[1]))