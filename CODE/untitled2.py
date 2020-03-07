#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:39:43 2020

@author: alanalvarez
"""

import pandas as pd
import matplotlib.pyplot as plt
import math 

def percentil_func(lista, perc):
    
    lista.sort()
    
    position = (len(lista) - 1 )*perc
    floor = math.floor(position)
    ceil = math.ceil(position)
    return lista[floor] +(lista[ceil]-lista[floor])*perc


w_d = '/Users/chris/desktop/MineriaDatos/code/'
i_f = w_d +'info_group.csv'


data = pd.read_csv(i_f, encoding = 'utf-8')
column = 'estatura'

lista = data[column].tolist()
lista.sort()

mini = lista[0]
maxi = lista[-1]

mediana = percentil_func(lista, 0.5)
fq = percentil_func(lista, 0.25)    
tq = percentil_func(lista, 0.75)    


iqr = tq - fq
uif = tq + 1.5 * ( iqr)
lif = fq - 1.5 * ( iqr)

for i in lista:
    if i >= lif:
        lw = i
        break
for i in lista[-1::-1]:
    if i <= uif:
        uw = i
        break
                 
outliers = []

for i in lista:
    if i < lw or i > uw:
        outliers.append(i)
        

# Media cortada
    

a = 30
n = len(lista)

media = sum(lista)/n

k = math.floor(((a/100)*n))
print(k)

suma = 0
lista_cortada = lista[k:n-k:]
for i in lista_cortada:
    suma += i
    
media_cortada = suma/(n-2*k)


#desviacion estandar

varianza  = sum([(i-media)**2 for i in lista])/(len(lista)-1)

#for i in lista:
#    suma += (i-media)**2

#varianza = suma / (n-1)

desviacion = varianza**(1/2)





print("Minimo ", mini)
print("MAximo ", maxi)
print("Mediana ", mediana)
print("1er quartil ", fq)
print("3r quartil ", tq)
print("lower interface ", lif)
print("Upper interface ", uif)
print("lower wisker ", lw)
print("upper wisker ", uw)
print( "outliers ", outliers )

print("media ", media )
print("media cortada ", media_cortada )

print("varianza ", varianza)
print("desviacion ", desviacion)