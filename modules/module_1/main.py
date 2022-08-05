#!/usr/bin/env python3

import os
import sys

# access to outside directory
sys.path.append("..")

# relative import
# Also I can import values from module_2 -> from module_2 import DEFAULT_VALUE
from module_2 import get_module_2

def get_module_1():
    # os.path.basename(__file__)
    print(__file__)
    
     # print(f'Default value coming from module_2 which is: {DEFAULT_VALUE}')
    get_module_2()