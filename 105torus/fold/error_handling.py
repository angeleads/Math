##
## EPITECH PROJECT, 2021
## error_handling
## File description:
## error handling file
##

from fold.helpfile import helpfile
from sys import argv, stderr

def needHelp(argv):
    if ('-h' in argv):
        return True
    return False


def checkInt(value):
    try:
        int(value)
    except ValueError:
        return 84
    else:
        return 0


def verifyInt():
    x = 1

    while x != 8:
        if checkInt(argv[x]) == 84:
            print("Incorrect type of argument, integer expected", file=stderr)
            return 84
        else:
            x = x + 1


def checkMethod(argv):
    if argv[1] == "1" or argv[1] == "2" or argv[1] == "3":
        return 1
    else:
        print ("There's only three methods, run -h if needed!", file=stderr)
        return 84


def checkArgs(argv):
    if (len(argv) != 8):
        print ("Oups! There's an invalid argument! Run -h if needed", file=stderr)
        return 84
    verify = verifyInt()
    if verify == 84:
        return 84


def error_handling():
    if needHelp(argv) == True:
        helpfile()
    elif checkArgs(argv) == 84:
        return 84
    elif checkMethod(argv) == 84:
        return 84
    return 0