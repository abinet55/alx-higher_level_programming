#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicti = a_dictionary.copy()
    list_key = list(new_dicti.keys())

    for j in list_key:
        new_dicti[j] *= 2

    return (new_dicti)
