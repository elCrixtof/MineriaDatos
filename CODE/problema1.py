
def weightedmean (d_freq, d, n):
    t=0
    for i, j in d_freq.items():
        t += d[i] * d_freq
    return t/n

lista = ['azul', 'rosa', 'azul', 'rojo', 'negro', 'rojo']
tp = 'nominal'
lista_2 = ['muy satisfecho', 'satisfecho', 'insatisfecho',]
tp = 'ordinal'

d = {'muy satisfecho':1 'satisfecho':2 'insatisfecho':3}

for i in lista_2:
    d_freq[i] = d_freq.get(i+0)+1

idx_set = set(lista_2)
if tp == 'ordinal':
    wm = weightedmean(d_freq,d,len(lista_2))
