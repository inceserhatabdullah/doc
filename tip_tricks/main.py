#!/usr/bin/env python3
# Write better code to be legend


"""                 Variables type
    # * 1. Numbers
    # * 2. String
    # * 3. List
    # * 4. Tuple: Tuples can be thought of as read-only lists
    # * 5. Dictionary
"""

# * first three values are the most common values
from collections import Counter
_counter = Counter([1,2,2,3,3,3,4,4,4,4])
_counter.most_common(3)  


sub, like, comment = 1, 2, 3
conditions = [
    sub > 0,
    like > 1,
    comment > 3
]

# * AND 
if all(conditions):
    pass

# * OR 
if any(conditions):
    pass

if True: print('Hello'); a = 5 # * One line if statement 

#                   DOCSTRING
def _docstring():
    """This is an example of a docstring statement"""
    pass
_docstring.__doc__

# ? palindrome --> text.find(text[::-1]) == 0  "Return boolean value"
