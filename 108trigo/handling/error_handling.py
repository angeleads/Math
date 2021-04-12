##
## EPITECH PROJECT, 2021
## error handling
## File description:
## error handling for the 108 project
##

from sys import argv, stderr
import math 

def HelpFile():
    print ("USAGE")
    print ("\t./108trigo fun a0 a1 a2 ...\n")
    print ("DESCRIPTION")
    print ("\tfun\tfunction to be applied, among at least 'EXP', 'COS', 'SIN', 'COSH'\n\t\tand 'SINH'")
    print ("\tai\tcoefficient of the matrix.")


def CheckInt():
    try:
        for i in range(2, len(argv)):
            argv[i] = int(argv[i])
    except:
        print ("Oups! There's an error.\nRun ./108trigo -h if needed.", file=stderr)
        return 84
    return 0


def CheckLenArg():
    length = len(argv) - 2
    argument = math.trunc(math.sqrt(length))
    if math.trunc(math.sqrt(length)) ** 2 != length:
        print ("Oups! There's an error.\nRun ./108trigo -h if needed.", file=stderr)
        return 84
    return argument


def VerifyArgs():
    if len(argv) == 2 and argv[1] == "-h":
        HelpFile()
        return 0
    elif len(argv) <= 2 or argv[1] not in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        print ("Oups! There's an error.\nRun ./108trigo -h if needed.", file=stderr)
        return 84
    elif CheckInt() == 84 or CheckLenArg() == 84:
        return 84
    return 0
    