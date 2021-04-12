##
## EPITECH PROJECT, 2021
## handling.c
## File description:
## error handling and check argument function
##

from sys import argv

def helpfile():
    print("USAGE")
    print("\t./107transfer [num den]*\n")
    print("DESCRIPTION")
    print("\tnum\tpolynomial numerator defined by its coefficients")
    print("\tden\tpolynomial denominator defined by its coefficients")


def InvalidChar(argv):
    for string in range(len(argv)):
        for char in range(0, len(argv[string])):
            if (argv[string][char] >= '0' and argv[string][char] <= '9' or argv[string][char] != '*'):
                return 0
            return (84)

def CheckAgs(argv):
    if len(argv) == 2 and argv[1] == "-h":
        helpfile()
    if len(argv) <= 2 or len(argv) % 2 == 0:
        return (84)
    if (InvalidChar(argv) == 84):
        return (84)
