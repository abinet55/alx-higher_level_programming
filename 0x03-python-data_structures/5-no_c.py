#!/usr/bin/python3
def no_c(my_string):
    leng = len(my_string)

    ch = 0

    mynew_string = my_string[:]

    for j in range(leng):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            mynew_string = mynew_string[:(j - ch)] + my_string[(j + 1):]
            ch += 1

    return (mynew_string)
