
d_main = '/Users/chris/desktop/md/code/'
f_1 = d_main + 'LuisSoriano.txt'
f_2 = d_main + 'Padilla.txt'

t_1 = t_2 = ''
with open(f_1, 'r', encoding = 'utf-8') as r_1:
    for line in r_1:
        t_1 += line.strip().lower()

with open(f_2, 'r', encoding = 'utf-8') as r_2:
    for line in r_2:
        t_2 += line.strip().lower()

w_1 = t_1.split()
w_2 = t_2.split()
d_1 = {}
d_2 = {}

for w in w_1:
    d_1[w] = d_1.get(w, 0) + 1

for w in w_2:
    d_2[w] = d_2.get(w, 0) + 1

p_1 = [(c, w) for w,c in d_1.items()]
p_2 = [(c, w) for w,c in d_2.items()]

p_1.sort()
p_2.sort()
p_1.reverse()
p_2.reverse()

s_1 = set([w for c,w in p_1[:10]])
s_2 = set([w for c,w in p_2[:10]])

print('Total de palabras repetidas = ', len(s_1.intersection(s_2)))