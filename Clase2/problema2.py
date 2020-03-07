#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:35:24 2020

@author: chris
"""

a = [[2,4], [1,5], [3,8]]
b =[]
c = 0

for i in a:
    for j in i:
        if j > c:
            c = j
    b.append(c)
    
print(b)