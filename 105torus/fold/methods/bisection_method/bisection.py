##
## EPITECH PROJECT, 2021
## bisection.py
## File description:
## bisection methode
##

def bisectionMethod(self, a0, a1, a2, a3, a4, n):
    xm = 0.5
    x1 = 0
    x2 = 1
    e = pow(10, -(n))
    i = 0
    p = 1
    while ((float(x2) - float(x1)) > float(e)):
        if (float(x1) + float(x2) == 0):
            print ('Determinant nul')
            return 84
        xm = (float(x1) + float(x2)) / 2
        f_m = a0 + a1 * xm + a2 * pow(xm, 2) + a3 * pow(xm, 3) + a4 * pow(xm, 4);
        f_a = a0 + a1 * float(x1) + a2 * pow(float(x1), 2) + a3 * pow(float(x1), 3) + a4 * pow(float(x1), 4)