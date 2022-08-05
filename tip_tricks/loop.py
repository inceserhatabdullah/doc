#!/usr/bin/env python3

_list = [1,2,3,4,5]
__list = [-1,-2,-3,-4,-5]

for index, value in enumerate(_list, start=0):
    pass
    
for _, __ in zip(_list, __list):
    pass

# https://note.nkmk.me/en/python-for-enumerate-zip/