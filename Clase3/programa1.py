#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:09:58 2020

@author: chris
"""

def greet (name):
    """This function sends a greet to the person that is passed as argument"""
    print('Hello, ' + name + '.Good Morning!' )
    
greet('Juan')

def absolute_value(num, name):
    """This function returns the absolute value of a numbre"""
    print('Hello, '+ name + 'Good morning')
    if num >= 0:
        return num
    else: return -num
    
print(absolute_value(-89))
print(absolute_value(-89, 'Maria'))

import math
print(math.pi)

from math import pi as p
print(p)

from math import ceil as cl
print(cl(5.5))


## Path from where import libraries (or local directory)
import sys
print(sys.path)
