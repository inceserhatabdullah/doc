#!/usr/bin/env python3

_list = [1,2,3,4,5]
__list = [-1,-2,-3,-4,-5]

for index, value in enumerate(_list, start=0):
    pass
    
for _, __ in zip(_list, __list):
    pass
# https://note.nkmk.me/en/python-for-enumerate-zip/


# ?                 ITERATOR

_iterator = iter(_list)
while True:
    try:
        element = _iterator.__next__()
        #next(_iterator)
        print(element)
        # ! The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.
    except StopIteration:
        break
    
# We can also customize the iterator! Check out the doc: https://www.programiz.com/python-programming/iterator