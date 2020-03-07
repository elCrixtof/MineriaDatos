#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:35:20 2020

@author: chris
"""

main_dir = '/Users/chris/Desktop/'

file_name = main_dir + 'test.txt'

with open(file_name, 'r', encoding = 'utf-8') as f:
    for line in f:
        print(line.rstrip())

with open(file_name, 'r', encoding = 'utf-8') as f:
    s = f.read()

print(s)

data = ['hello', 'world']
file_name = main_dir + 'test_out.txt'
with open(file_name, 'w', encoding='utf-8') as f:
    for word in data:
        f.write(word + '\n')
        
file_name_1 = main_dir+'test.txt'
file_name_2 = main_dir+'test_out_2.txt'
with open(file_name_2, 'r', encoding='utf-8') as f, open(file_name_2, 'w', encoding='utf-8') as fo:
    s = f.read()
    fo.write(s.lower())

        
    