/*
** EPITECH PROJECT, 2021
** rate_evolution.c
** File description:
** function to get the evolution with rate
*/

#include "bombyx.h"

double rate_formula(double k, double first)
{
    double result = 0;

    result = k * first * ((1000 - first) / 1000);
    return (result);
}

int gen_evolution(double n, double k)
{
    double first = n;
    double after = 0;
    int x = 0;

    if (k < 1 || k > 4)
        return (ERROR);
    while (x < 100) {
        printf("%d %.2f\n", x + 1, first);
        after = rate_formula(k, first);
        first = after;
        x++;
    }
    return (SUCCESS);
}