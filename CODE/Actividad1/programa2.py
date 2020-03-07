d_main = '/Users/chris/desktop/md/code/'
f_1 = d_main + 'LuisSoriano.txt'
f_o = d_main + 'file.txt'

n = 40
with open(f_1, 'r', encoding = 'utf-8') as r_1:
    t = r_1.read()

b = 0
e = n
l = len(t)

with open(f_o, 'w', encoding = 'utf-8') as w_o:
    while b < l:
        w_o.write(t[b:e]+'\n')
        b = e
        e += n

