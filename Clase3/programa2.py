#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:20:58 2020

@author: chris
"""

def greet(name, msg = 'Good morning', number = 3):
    """This function greets a person with the desired message
    if the message is not passed, the default "Goodmorning" is used"""
    print('hello ' + name + ', ' + msg + str(number))
    

greet('Maria')
greet('Maria', 'how do you do?')
greet('Maria', 'how do you do?', 10)

greet('Maria', 'how do you do?')
greet( msg = 'how do you do?', name = 'Maria', number = 10)
greet('Maria' ,number = 9, 'how do you do?')
