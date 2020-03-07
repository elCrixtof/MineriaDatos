# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

def frequencies(lista):
    d_freq = {}
    for i in lista:
        d_freq[i] = d_freq.get(i,0)+1
    return d_freq

w_d = '/Users/chris/desktop/MineriaDatos/code/'
i_f = w_d + 'info_group.csv'

data = pd.read_csv (i_f, encoding = 'utf-8')

#print(data.columns)
#print(data['nombre'])

column = 'nombre'
valores = data[column].tolist()
valores = [a.upper().strip() for a in valores]
d_freq = frequencies(valores)
#print(d_freq)

#Sort a dictionario
l_dict = [(v,k) for v,k in d_freq.items()]
l_dict.sort(reverse = True)
print(l_dict)

data[column].str.upper().value_counts().plot(kind='pie')

plt.figure()
data[column].str.upper().value_counts(sort = 0).plot(kind='pie')
