#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:12:55 2020

@author: chris
"""

lista = "I love python, python is a great programming language and i love it"
dic = {}



for i in lista.split(' '):
   if i is in dic:
       dic[i] += 1
    

print(dic)
        