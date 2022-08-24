'''
Programa que agarra archivos .csv, los pasa a un DataFrame de Pandas y luego lo graba como Excel
'''
# %%
import pandas as pd
import os

file = '10.csv'

df = pd.read_csv(file, index_col=0, header=None,
                 names=['Long. de onda', file[:-4]+' ppm'])
# %%
df.sort_index(inplace=True)
# %%
df.head()
# %%
file2 = '100.csv'
df_aux = pd.read_csv(file2, index_col=0, header=None,
                     names=['Long. de onda', file2[:-4]+' ppm'])
df.sort_index(inplace=True)
# %%
df_aux.head()
