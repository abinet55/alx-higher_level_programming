#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_lists = list(a_dictionary.keys())
    order_lists.sort()
    for i in order_lists:
        print("{}: {}".format(i, a_dictionary.get(i)))
        
