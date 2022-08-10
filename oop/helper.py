#!/usr/bin/env python3
# When to use class methods and when to use static methods ?

class Helper:
    #* https://learnpython.com/blog/custom-class-python/
    
    def __init__(self):
        self.helper = None
        self.__private = None
    
    @property
    def private(self):
        return self.__private
    
    @private.setter
    def private(self, value):
        self.__private = value
        
    def __repr__(self) -> str:
        #* https://www.pythontutorial.net/python-oop/python-__repr__/
        return f'{self.__class__.__name__}({self.value})'
    
    def __str__(self) -> str:
        return f'{self.value}'

    @staticmethod
    def is_integer():
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        '''
    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!
# NOTE: However, those could be also called from instances.

_ = Helper()