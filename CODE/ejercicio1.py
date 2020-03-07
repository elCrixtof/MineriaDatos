#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:31:40 2020
@author: chris

Descripción:this program computes the frequencies for each
possible value of a nominal/ordinal variable. In case of an 
ordinal variable, it also computes the wighted mean
"""
            
lista = ['azul', 'rosa', 'azul', 'rojo', 'negro', 'rojo']
tp = 'ordinal'


#if tp == 'ordinal':
#    we = weightedmean(frequencies)
#    print(we)
dic = {}
 
for i in lista:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

frequencies = 0
for i in dic:
    frequencies += dic[i]
    
    

lista2 = [1,2,3,4]
weightedmean = 0
aux=0
for i in dic:
    weightedmean += dic[i] * lista2[aux]
    aux+=1
    
    

we = weightedmean/frequencies

if tp == 'nominal':
    print(dic)

if tp == 'ordinal':
    print(we)