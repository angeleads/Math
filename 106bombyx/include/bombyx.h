/*
** EPITECH PROJECT, 2021
** bombyx.h
** File description:
** bombyx's include file
*/

#ifndef BOMBYX_H_
#define BOMBYX_H_
#include "macros.h"
#include <stdio.h>

void helpfile(void);
int check_args(int argc, char **argv);
int gen_evolution(double n, double k);
double rate_formula(double k, double first);
void synth_scheme(double n, double i0, double i1);
int check_int(char *argv);
int bombyx(int argc, char **argv);

#endif /* !BOMBYX_H_ */
