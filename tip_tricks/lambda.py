#!/usr/bin/env python3

"""                 LAMBDA
# * An anonymous function is a function that is defined without a name. Anonymous functions are defined using the lambda keyword.

# ? filter(): This method is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True
# ? map(): This method  is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
# * https://www.programiz.com/python-programming/anonymous-function
# * https://realpython.com/python-lambda/
"""

_ = [1,2,3,4,5,6,7,8,9,10,11]
_filter = list(filter(lambda x: (x % 2 == 0), _))
__ = list(map(lambda x: x ** 2, _))


data = [{'name': 'serhat','age': 1},{'name': 'abdullah','age': 2},{'name': 'ince','age': 3}]
sorted(data, key=lambda x: x['name'])