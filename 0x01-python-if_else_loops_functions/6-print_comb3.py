#!/usr/bin/python3
for first_digit in range(0, 9):
    for second_digit in range(first_digit + 1, 10):
        if first_digit == 8:
            print("{:d}{:d}".format(first_digit, second_digit))
            break
        print("{:d}{:d}".format(first_digit, second_digit), end=", ")
