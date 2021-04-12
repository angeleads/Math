/*
** EPITECH PROJECT, 2021
** helpfile.c
** File description:
** function used if help is needed
*/

#include <stdio.h>

void helpfile(void)
{
    printf("USAGE\n");
    printf("\t./106bombyx n [k | i0 i1]\n\n");
    printf("DESCRIPTION\n");
    printf("\tn\tnumber of first generation individuals\n");
    printf("\tk\tgrowth rate from 1 to 4\n");
    printf("\ti0\tinitial genertion (included)\n");
    printf("\ti1\tfinal generation (included)\n");
}