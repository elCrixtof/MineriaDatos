#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:15:07 2020

@author: chris
"""

def percentil (lista, perc):
    pm = (len(lista)-1)*perc
    pl = math.floor(pm)
    pu = math.ceil(pm)
    return lista[pl]+(lista[pu]-lista[pl])*perc
    
import math

lista = [1.75, 1.63, 1.89, 1.93, 1.56, 1.72, 1.65, 1.80, 1.77, 1.71]

lista.sort()

mini = lista[0]
maxi = lista[-1]
mediana = percentil(lista, 0.5)
fq = percentil(lista, 0.25)
tq = percentil(lista, 0.75)

print(mini, maxi, mediana, fq, tq)


