#!/usr/bin/env python3

"""                 GENERATOR
# * It is as easy as defining a normal function, but with a yield statement instead of a return statement.

# ? If a function contains at least one yield statement, it becomes a generator function.

# ? The difference is that while a return statement terminates a function entirely, 
yield statement pauses the function saving all its states and later continues from there on successive calls.

                    Differences between Generator function and Normal function
# ? Generator function contains one or more yield statements.
# ? When called, it returns an object (iterator) but does not start execution immediately.
# ? Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
# ? Once the function yields, the function is paused and the control is transferred to the caller.
# ? Once the function yields, the function is paused and the control is transferred to the caller.
# ? Finally, when the function terminates, StopIteration is raised automatically on further calls.
# * https://www.programiz.com/python-programming/generator
"""


def _generator():
    _value = 1
    print(f'First execution')
    yield _value
    
    _value += 1
    print(f'Second execution')
    yield _value
    
    _value += 2
    print(f'Third execution')
    yield _value

_execute = _generator()
_execute.__next__()

__generator = (_iterator ** 2 for _iterator in range(4))
__generator.__next__()

"""If we want to find out the sum of squares of numbers in the Fibonacci series, 
we can do it in the following way by pipelining the output of generator functions together."""

def _fibonacci(number):
    _first, _second = 0, 1
    for _ in range(number):
        _first, _second = _second, _first + _second
        yield _first

def square(number):
    for _ in number:
        yield _ ** 2

sum(square(_fibonacci(10)))