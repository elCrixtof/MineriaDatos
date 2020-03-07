#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:43:49 2020

@author: chris
"""

lista = [3, 3, 4 ,5 ,1, 1, 4, 5, 6]
lista2 = []
dic = {}
    
for i in lista:
    if i not in lista2:
        lista2.append(i)
    if i in lista2:
        continue
    
lista2.sort()

for i in lista2:
    a = 0
    for j in lista:
        if i == j:
            a+=1
    if a > 0:
        dic.update({i:a})
        

print(lista2)
print(dic)




