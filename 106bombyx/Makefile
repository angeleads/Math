##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Makefile for 106bombyx
##

CC	=	gcc
LD	=	$(CC)

NAME	=	106bombyx

SRC	=	src/main.c					\
		src/check_args.c			\
		src/helpfile.c				\
		src/bombyx/gen_evolution.c	\
		src/bombyx/synth_scheme.c	\
		src/bombyx/bombyx.c

OBJ	=	$(SRC:.c=.o)

CFLAGS	=	-I ./include/

all:	$(NAME)

$(NAME):	$(OBJ)
	$(CC) -o $(NAME) $(OBJ)

clean:
	rm -f $(OBJ)

fclean:	clean
	rm -f $(NAME)
	rm data

re: fclean all