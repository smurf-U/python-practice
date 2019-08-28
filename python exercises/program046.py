# !/user/bin/python
# -*- coding: utf-8 -*-
#- Author : Kaushal Prajapati

# Write a program which can map() to make a list whose elements are square
# of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.


def do(start_number, end_number):
    list = [value for value in range(start_number, end_number + 1)]
    print 'list :', list
    val = map(lambda number: number ** 2, list)
    print 'square of list Elements .......'
    print val


def main():
    do(int(raw_input('Enter Starting Number :')),
       int(raw_input('Enter Ending Number :')))

if __name__ == '__main__':
    main()
