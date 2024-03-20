#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lists = set(my_list)
    number = 0

    for j in uniq_lists:
        number += j

    return (number)
