#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:15:38 2020

@author: chris
"""

b = ['hola', 1, 9.4]

#List iteration over values
for x in b:
    print(x)

for i in range(len(b)):
    print(b[i])
    

print('\n\nStrings are (inmutables) list')
s = 'Hello world'
print(s)
print(s[0])
print(s[:5])
print(s[5:])
print(s[:5:2]) #Begining, end, step
#s[5] = 'd'
print('\nConcatenation')
s = 'Hello'
t = 'world'
u = s + ' '+ t 
print(u)
print('\nRepetition')
print(s*3)
print(len(u) # String length

#Break

for val in 'hello' :
    if val == "l":
        break
    print(val)
print('End')
print('\n\n')

for val in 'hello' :
    if val == "l":
        continue
    print(val)
print('End')

#Python sets
print('\n\nPython sets')
a = {1,2,3,4,5.5,1,2,3}
print(a)
a = {5,1,2,3,4,5,5,5,5,4,3,2,1}
print(a)
#print(a[0])
b = {3,4,5,6,7,8}
print(b)
print('\nUnicon of sets')
print(a.union(b))
print('\nIntersection of sets')
print(a.intersection(b))
print('\nDifference of sets')
print(a.difference(b))
b = {1,2}
print('\nCheck for subset')
print(a.issuperset(b))
print('\nAdd element to set')
print(a.add('hola'))
print('\nAdd several elements to set')
a.update(['one', 'two', 'three'])
print(a)
print('\'nRemove an elements from set')
a.remove(3)
print(a)



#python dictionaries
print('\nPython dictionaries')
d = {'uno':'value', 'numbre':2, 3:'test'}
print(d)
print(d['uno'])
print(d['number'])
print(d[3])
print('\nAdd element to dictionary')
d['five'] = 5
print(d)
print('\nAdd several elements to dictionary')
d.update({6:'six', 'eight':'hello', 9:1890})
d[6] = 'mundo'
print(d)

#Interate over elements of dictionary
d = {1:'hello', 2:'world', 'pene':'whats', 4:'up'}
for i in d:
    print(i, d[i])

for i, j in d.items():
    print(i, '\t', j)
    
#Python tuples
print('\n\nPython tuples')
t = ('tuples', 'are', 'list', 'but', 'inmutable')
print(t)
print(t[0])
print(t[:3])
t[0] = 'assignements to elements in a tuple are'
t = t + (9,) #merge of tuples
print(t)
print('\nAdd several elements to tuple')
t = t + (10, 11, 'hello')#merge of tuples
print(t)

for i in t:
    print(i)
    
for i in range(len(t)):
    print(t[i])
    
#data type conversion
print('\n\nData type conversion')
print(int(10.5))
print(str(50.6))
print(float(5))
print(int('50'))
print(float('50.7'))
print(list(t))
print(set(t))