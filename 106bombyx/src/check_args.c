/*
** EPITECH PROJECT, 2021
** check_args.c
** File description:
** function to check arguments
*/

#include "bombyx.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int is_int(char *argv)
{
    int x = 0;

    while (argv[x] != '\0') {
        if (isdigit(argv[x]) == 0)
            return (FAILURE);
        x++;
    }
    return (SUCCESS);
}

int is_float(char *str)
{
    int size = strlen(str);
    int x = 0;

	while (x < size) {
		if (!(str[x] >= '0' && str[x] <= '9') &&
			str[x] != '.')
			return (FAILURE);
        x++;
	}
	return (SUCCESS);
}

int check_args(int argc, char **argv)
{
    
    if (argc == 2 && strcmp(argv[1], "-h") == SUCCESS)
            helpfile();
    if (argc == 2 && strcmp(argv[1], "-h") != SUCCESS)
        return (ERROR);
    if (argc == 1 || argc > 4)
        return (ERROR);
    if (argc == 3) {
        if (atoi(argv[1]) < 0 || is_int(argv[1]) == FAILURE 
        || is_float(argv[2]) == FAILURE || atoi(argv[2]) < 1 || atoi(argv[2]) > 4)
            return (ERROR);
    } if (argc == 4) {
        if (is_int(argv[2]) == FAILURE || is_int(argv[3]) == FAILURE ||
            atoi(argv[2]) <= 0 || atoi(argv[2]) >= atoi(argv[3]))
        return (ERROR);
    }
    return (SUCCESS);
}