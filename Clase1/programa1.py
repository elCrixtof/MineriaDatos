#This is my first programs
"""
This is multiline
comment to describe better
py program
"""

#python int, float, complex
print('Python numbers')

a = 5
A = 10.7
b = 5.6
c = 5 + 6j
d = e = f = 87.9

print(a)
print(b)
print(c)
print('\nknow the type of an object')
print(a,b,c)
print(type(c))
print(isinstance(a, int))

#python strings
print ('\n\n Python strings')
s1 = 'Hello world! "how are you?' 
#s1 = 'Hello world! \'how are you\'' 
s2 = "Hello world! 'how are you' "

print(s2)
print(s1)


#python lists
print('\n\nPython lists')
a = [1, 2,2, 'python',[1,2,3]]
b = [1,2,3,4,5,6,7,8,9,10]

print(a)
print(b)
print(a[0])
print(b[:5])
print(b[5:])
print(a[-1]) #Access the last element
print(a[-2]) #Access the second-to-last element
print('\nChange the value of an element')
b[4] = 'two hundred'
print(b)
print('\nAdd an element to the list(at the end)')
b.append('two hundred')
print(b)
print('\nExtend a list with another list(at the end)(concatenation)')
b.extend(['a','b','c','d'])
print(b)
print(b+['e','f','g','h'])
print('\nList length')
print(len(b))
print('\nExtract an element')
last = b.pop()
print('b without the last element: ', b)
fifth  =b.pop(4)
print('b without the fifth element: ', b)
print('b original: ', b)
b.append('a')
b.remove('a')#Remove the first occurence of 'a'
print('b without the element: ', b)
print('\nKnow the index of the first of occurence of an element')
print(b.index('b'))
print(b.index('b',5,))#Search the element between a beginning and an end
print('\nInsert an element in a specific position')
b.insert(3,2000) #Insert the element 2000 at the index 3
print(b)
print('\nConcatenation')
print(a+b)
