/*
** EPITECH PROJECT, 2021
** bombyx.c
** File description:
** main function of bombyx
*/

#include "bombyx.h"
#include <stdlib.h>

int bombyx(int argc, char **argv)
{
    if (check_args(argc, argv) == ERROR)
        return (ERROR);
    if (argc == 3)
        gen_evolution(atof(argv[1]), atof(argv[2]));
    else if (argc == 4)
        synth_scheme(atof(argv[1]), atof(argv[2]), atof(argv[3]));
    return (SUCCESS);
}