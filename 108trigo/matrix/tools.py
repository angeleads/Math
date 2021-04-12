##
## EPITECH PROJECT, 2021
## tools.py
## File description:
## all the necessities to create a matrix
##

def PrintMatrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            print ("%.2f%c" % (matrix[y][x], '\t' if (x != len(matrix[y]) -1) else '\n'), end="")