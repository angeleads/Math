##
## EPITECH PROJECT, 2021
## main operations with matrix
## File description:
## operations.py
##

from sys import argv
import math

def CheckMatrix(element):
    matrix = []
    for y in range(element):
        x_matrix = []
        for x in range(element):
            x_matrix.append(1 if x == y else 0)
        matrix.append(x_matrix)
    return (matrix)


def SumMatrix(matrix1, matrix2):
    matrix = []
    for y in range(len(matrix1)):
        x_matrix = []
        for x in range(len(matrix1[0])):
            x_matrix.append(matrix1[y][x] + matrix2[y][x])
        matrix.append(x_matrix)
    return matrix


def SubMatrix(matrix1, matrix2):
    matrix = []
    for y in range(len(matrix1)):
        x_matrix = []
        for x in range(len(matrix1[0])):
            x_matrix.append(matrix1[y][x] - matrix2[y][x])
        matrix.append(x_matrix)
    return matrix


def MultMatrix(matrix1, matrix2):
    matrix = []
    for y in range(len(matrix1)):
        x_matrix = []
        for x in range(len(matrix2[0])):
            i = 0
            for j in range(len(matrix1[0])):
                i += matrix1[y][j] * matrix2[j][x]
            x_matrix.append(i)
        matrix.append(x_matrix)
    return matrix


def DivMatrix(matrix, div):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix[y][x] /= div
    return matrix

def PowMatrix(matrix, power):
    temp_matrix = matrix
    for y in range(power - 1):
        temp_matrix = MultMatrix(temp_matrix, matrix)
    return temp_matrix