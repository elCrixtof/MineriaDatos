#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:22:19 2020

@author: chris
"""

import math as mt

lista1 = [1.75, 1.63, 1.89, 1.93, 1.56, 1.72, 1.65, 1.80, 1.77, 1.71]
lista2 = [0,1,0,0,1,0,1,1,1,0]

x = sum(lista1)/len(lista1)
y = sum(lista2)/len(lista2)

suma1 = 0
suma2 = 0
suma3 = 0

for i in range(0, len(lista1)):
    suma1 += (lista1[i]-x)*(lista2[i]-y)
    suma2 += (lista1[i]-x)**2
    suma3 += (lista2[i]-y)**2
    
#raiz = (suma2*suma3)**(1/2)
suma2 = mt.sqrt(suma2)
suma3 = mt.sqrt(suma3)
raiz = suma2 * suma3
correlacion = suma1/raiz

print(correlacion)