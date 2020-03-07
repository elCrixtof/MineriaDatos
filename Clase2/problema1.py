#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:20:18 2020

@author: chris
"""

lista = [10,20,30,20,10,50,60,40,80,50,40]
lista2 = []
    
for i in lista:
    if i not in lista2:
        lista2.append(i)
    if i in lista2:
        continue
        
lista2.sort()
print(lista2)






