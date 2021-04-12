/*
** EPITECH PROJECT, 2021
** exo_deux.c
** File description:
** jsp du tout encore
*/

#include "bombyx.h"

void synth_scheme(double n, double i0, double i1)
{
    double k = 1;
    double temp = n;
    double x = 1;

    while (k < 4) {
        x = 1;
        n = temp;
        while (x < i0) {
            n = rate_formula(k, n);
            x++;
        }
        while (x <= i1) {
            if (n > 0)
                printf("%.2f %.2f\n", k, n);
            else
                printf("%.2f 0.00\n", k);
            n = rate_formula(k, n);
            x++;
        }
        k = k + 0.01;
    }
}