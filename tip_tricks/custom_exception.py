#!/usr/bin/env python3

_input = int(input("Enter a number: "))
_number = 10

class Error(Exception):
    pass

class ValueTooBigError(Error):
    pass
class ValueTooSmallError(Error):
    pass

class CustomizeException(Exception):
    def __init__(self, number, message="Number is not be negative") -> None:
        self.number = number
        self.message = message
        super().__init__(self.message)
        
    def __str__(self) -> str:
        return f'{self.number} -> {self.message}'

try:
    if _input > _number:
        raise ValueTooBigError
    elif _input < _number:
        raise ValueTooSmallError
except ValueTooBigError:
    print("This value is too big!")
except ValueTooSmallError:
    print("This value is too small!")
    
if not _input > 0:
    raise CustomizeException(_input)