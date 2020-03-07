import numpy as np
import random 
d_main = '/Users/chris/desktop/md/code/'
f_o = d_main + 'file.txt'

n = 9
m = 4

a = np.random.randint(1, 1000, size=(n,m))

print (a)
print(a[2][3])

np.savetxt('file.txt', a, fmt='%i',)
#with open(f_o, 'w', encoding = 'utf-8') as w_o:
#    w_o.write(a.)
