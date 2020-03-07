#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:13:46 2020

@author: chris
"""

import pandas as pd
import matplotlib.pyplot as plt
import math 

data = [1.75, 1.63, 1.89, 1.93, 1.56, 1.72, 1.65, 1.8, 1.77, 1.71]
data.sort()
bins = 3
listab = []
listaaux = []

rango = (data[-1] - data[0]) / bins
binMe = data[0]
binMa = binMe + rango

print('Rango', rango)

for x in range(bins): 
    for i in data:
        if x == bins - 1 :
            if i <= binMa and i >= binMe:
                listaaux.append(i)
        elif i < binMa and i >= binMe:
            listaaux.append(i)
    listab.append(listaaux)
    listaaux = []
    binMe = binMa
    binMa += rango
    
    
print(listab)



