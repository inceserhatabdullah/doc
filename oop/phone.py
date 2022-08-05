#!/usr/bin/env python3

from item import Item

# Inheritance
class Phone(Item):
    def __init__(self, attribute: str, quantity: int, broken: int):
        super().__init__(attribute, quantity)
        
        assert broken > 1, f"Broken Phones {broken} is not greater than one!"
        self.broken = broken