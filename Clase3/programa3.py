#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:29:06 2020

@author: chris
"""

def greet(*names):
    for name in names:
        print('hello',name)
        
greet (12.6, 'Maria', 'Lluis', 'Putona', 'putillo', ['pedro', 'juan'])

def factorial(x):
    if x==1:
        return 1
    else: 
        return (x * factorial(x-1))
    
print(factorial(5))

def multiple(x):
    i=0
    x=x*x
    return i,x

num = 4
print('the factorial of', num, 'is', factorial(num))

a,b = multiple(2)