#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    list_new = my_list[:]

    if 0 <= idx < length:
        list_new[idx] = element

    return (list_new)
