# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : Kaushal Prajapati

# Define a function which can generate and print a list where the values
# are square of numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


def main():
    numbers = []

    for value in range(1, 21):
        numbers.append(str(value ** 2))
    print ','.join(numbers)
if __name__ == '__main__':
    main()
