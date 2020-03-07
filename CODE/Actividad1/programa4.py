import numpy as np 

d_main = '/Users/chris/desktop/md/code/'
f_1 = d_main + 'file.txt'

t_1 = ''
with open(f_1, 'r', encoding = 'utf-8') as r_1:
    for line in r_1:
        t_1 += line

print(t_1)

a = np.fromstring(t_1, dtype=int, sep=' ')

print('lectura', a)

