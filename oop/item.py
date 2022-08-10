#!/usr/bin/env python3

import csv

class Item:
    price = 16
    all = []
    
    # Initialize method
    # attribute type must be string
    def __init__(self, attribute: str, quantity: int):
        # if quantity is not greater than 0, then program will fail
        assert quantity > 0, f'Quantity: {quantity} must be greater than 0!'
        
        self.__attribute = attribute
        self.quantity = quantity
        #self.print_attributes()
        
        #actions to execute
        Item.all.append(self)
    
    @property
    def attribute(self):
        print(f"You are trying to get attribute: {self.__attribute}")
        return self.__attribute
    
    @attribute.setter 
    def attribute(self, value):
        print(f"You are trying to set attribute = {value}")
        if len(value) > 5:
            raise Exception("You must have at least 5 characters")
        self.__attribute = value
       
    @classmethod
    def instantiate_from_csv(cls):
        # cls search it
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
        for _ in data:
            Item(
                attribute=_.get('attribute'),
                quantity=int(_.get('quantity')),
            )
    @staticmethod
    def is_integer(number):
        # research decorators like staticmethod and classmethod etc.
        # For i.e: 5.0 
        if isinstance(number, float):
            # Count out the floats that are point zero
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
    
    def __repr__(self) -> str:   # research this method
        return f"{self.__class__.__name__}('{self.attribute}', {self.quantity})"