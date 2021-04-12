##
## EPITECH PROJECT, 2021
## transfer.py
## File description:
## main operation function
##

def formula(array, parse_elem):
    result = ((array / 1000) ** parse_elem)
    return (result)


def transfer(content):
    #take the array for each 0.001
    for array in range(0, 1001):
        #initialize the result to 1
        transfered = 1
        #parse each string parsed 2 by 2
        for string in range(0, len(content), 2):
            #elements of each string parsed
            elem1 = 0
            elem2 = 0
            #pretty self explanatory
            if content[string] != content[string + 1]:
                #the whole operation
                for parse_elem in range(0, len(content[string])):
                    elem1 = elem1 + content[string][parse_elem] * formula(array, parse_elem)
                for parse_elem in range(0, len(content[string + 1])):
                    elem2 = elem2 + content[string + 1][parse_elem] * formula(array, parse_elem)
                transfered = transfered * (elem1 / elem2)
        print("%.3f -> %.5f" % (array / 1000, transfered))