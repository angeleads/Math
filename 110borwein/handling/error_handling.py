##
## EPITECH PROJECT, 2021
## handling
## File description:
## error handling of the project
##

from sys import argv, stderr

def helpFile():
    print ("USAGE")
    print ("\t./110borwein n\n")
    print ("DESCRIPTION")
    print ("\tn constant defining the integral to be computed")

def checkInt(argv):
    try:
        int(argv[1])
        return 0
    except ValueError:
        return 84

def checkPositive(value):
    if int(value) < 0:
        return 84
    return 0

def errorHandling():
    if len(argv) == 2 and argv[1] == "-h":
        HelpFile()
        return 0
    elif len(argv) != 2 or checkInt(argv) == 84 or checkPositive(argv[1]) == 84:
        print ("Oups! Invalid arguments\nRun ./110borwein -h if needed", file=stderr)
        return 84