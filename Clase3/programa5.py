#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:49:08 2020

@author: chris
"""

import numpy as np

lista = [[1,2,3],[4,5,6]]

print('\nArrays creation')
nbrs_1= np.array([1,2,3,4,5,6])
nbrs_2= np.array(lista)
print(nbrs_1)
print(nbrs_2)
print('\n\n Arrys indexing')
print(nbrs_2[:,:2])

print('\n\n Arrys zeros')
print(np.zeros((5,3)))

print('\n\n Arrys ones')
print(np.ones((3,6)))

print('\n\n Arrys linespace')
print(np.linspace(0,100,11))

print('\n\n Arrys range')
print(np.arange(0,10,dtype='uint8'))

print('\n\n Arrys random')
print(np.random.rand(2,5))

x= np.array([[1,2],[3,4]])
y= np.array([[5,6], [7,8]])

v= np.array([9,10])
w= np.array([11,12])

print('\n\n Vector and matrix product')
print(v.dot(w))
print(np.dot(v,w))

print(v.dot(v))
print(np.dot(x,y))

print(x.dot(y))
print(np.dot(x,y))

print('\n\n Arrys extra operations')

lista_2 = [1,2,0,0,4,0]
a = np. array(lista_2)
print(np.nonzero(a))

print(a)
print(a.shape)
print(a.T)
a = np.atleast_2d(lista_2)
print(a)

print(a.shape)
print(a.T)

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b), axis=0))

for i in a:
    for j in i:
        print(j)
