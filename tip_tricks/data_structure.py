#!/usr/bin/env python3

import sys

"""                 LIST
# * List is a collection which is ordered and changeable. Allows duplicate members.

# ? append(): Using dot notation, we can attach the append() method to a list to add an item to the list.
# ? insert(): When adding items to a list using the insert() method, you specify the index where it should be placed.
# ? pop(): Removes the last item in the list. You can also specify a particular item to be removed using its index   
# ? del(): If you do not specify any index when using the del keyword, the entire list will be deleted.
# ? count(): This method returns the number of times the specified element appears in the list.
# ? remove(): This method removes the first matching element (which is passed as an argument) from the list.
# ? reverse(): This method reverses the elements of the list.
# ? sort(): This method sorts the items of a list in ascending or descending order.
# ? index(): This method returns the index of the specified element in the list.
# ? extend(): This method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# ? copy(): This method returns a shallow copy of the list.
# ? clear(): If you want to empty a list and still have a reference to it without getting an error, then you can use this method.
# * https://www.programiz.com/python-programming/methods/list
"""

_list = [1,2, 3, 4, 5, 6, 7]
_list.append(8)
_list.insert(0, 9)
_list.remove(3) # ! It returns a KeyError if x is not part of the set:
_list.pop() # * _list.pop(2) remove second index from _list
_list.count(1)
_list.remove(2)
_list.reverse()
_list.sort()
_list.index(4)
_list.extend([10, 11, 12, 13])
_copy_list = _list.copy()
del _list[1] # delete first index from _list  -  del _list -> delete all items in _list
del _copy_list
_list.clear() # clear



"""                 TUPLE
# * Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# ? If you are using the tuple() method to create the tuple, don't forget that it needs double parentheses.
"""



"""                 SET
# * Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# ? As you've probably realized, whether you use the set() function or the {} to create a set, 
# ? each element needs to be an immutable object. 
# ! So if you add a list (which is a mutable object) to a set, you'll run into an error:
# ? We already know that sets are mutable. This means you can add/remove elements in a set.
# * https://www.programiz.com/python-programming/methods/set
"""

_set = set(('Integers',1,2,2,3,3,3))
__set = {'Integers',1,2,3}
_set.update((4,5,))
_set.remove(4) # * It returns a KeyError if x is not part of the set:
_set.discard(6) # * no error raised even though '6' is not present in the set
_set.clear() # * the clear() method removes all elements from a set

# ? Set Operations

_set.union(__set)  
# _set | __set
# * You can use the union() method or the | syntax to find the union of a Python set.

_set.intersection(__set)
# _set & __set
# * You can use the intersection() method of the & operator to find the intersection of a Python set. (Find all the common elements)

_set.difference(__set)
# _set - __set
# * The difference between two sets is the set of all the elements in first set that are not present in the second set
# * You would use the difference() method or the - operator to achieve this in Python. (Find all the difference between two Python sets)

_set.symmetric_difference(__set)
# _set ^ __set
# * The symmetric difference between two sets is the set of all the elements that are either in the first set or the second set but not in both.
# * You have the choice of using either the symmetric_difference() method or the ^ operator to do this in Python.

# the _set.issubset(__set) method or <= operator returns true if the _set is a subset of __set
# the _set.issuperset(__set) method or >= operator returns true if the _set is a superset of __set
# the _set.isdisjoint(__set) method return true if there are no common elements between sets _set and __set


"""                 FROZENSET
# ? Because sets are mutable, they are unhashable - which means you cannot use them as dictionary keys.
# ? Python allows you to work around this by using a frozenset instead. 
# ? This has all the properties of a set, except that it is immutable (this means that you cannot add/remove elements from the frozenset). 
# ? It is also hashable, so it can be used as keys to a dictionary.
# ? The frozenset datatype has all the methods of a set (such as difference(), symmetric_difference, and union) but because it is still immutable, 
# * https://www.freecodecamp.org/news/python-set-operations-explained-with-examples/
"""



"""                 DICTIONARY
# * Dictionary is a collection which is ordered** and changeable. No duplicate members.

# ? get(): The get method returns the value of a specified key.
# ? items(): This method returns all the entries of the dictionary in a list. In the list is a tuple representing each of the items.
# ? keys(): This method returns all the keys in the dictionary. It returns the keys in a tuple – another Python data structure.
# ? values(): This method returns accesses all the values in a dictionary. Like the keys() method, it returns the values in a tuple.
# ? pop(): This method returns removes a key-value pair from the dictionary. To make it work, you need to specify the key inside its parentheses.
# ? popitem(): This method returns works like the pop() method. The difference is that it removes the last item in the dictionary.
# ? update(): This method adds an item to the dictionary. You have to specify both the key and value inside its braces and surround it with curly braces.
# ? copy(): This method does what its name implies – it copies the dictionary into the variable specified.
# ? clear(): This method removes all the entries in the dictionary.
# ? setdefault(): This method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# ? fromkeys(): This method creates a dictionary from the given sequence of keys and values.
# * https://www.programiz.com/python-programming/methods/dictionary
"""

_dict = {'item': 'Samsung s10e', 'price': f'{4_500}₺'}
_dict.get('count') # get value from dictionary
_dict.items() # return all entries
_dict.keys() # return all keys
_dict.pop('count')
_dict.popitem()
_dict.update({'count': 1})
_copy_dict = _dict.copy()
_copy_dict.clear()
_dict.setdefault('count', 1) # set value
_from = 2
_new_dict = dict.fromkeys(_dict, _from)




# ?                 MERGE DICTIONARY
__dict = {'os': 'Android', 'version': 12}
{**_dict, **__dict}


# ?                 MEMORY

list(i for i in range(100))
tuple(x for x in range(100)) # less memory than

def get_size(data):
    return sys.getsizeof(data)