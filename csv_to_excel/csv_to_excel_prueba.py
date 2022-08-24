'''
Programa que agarra archivos .csv, los pasa a un DataFrame de Pandas y luego lo graba como Excel
'''
# %%
import pandas as pd
import os

file = '10.csv'

df1 = pd.read_csv(file, index_col=0, header=None,
                  names=['Long. de onda', file[:-4]+' ppm'])
df1.sort_index(inplace=True)
# %%
file2 = '100.csv'
df2 = pd.read_csv(file2, index_col=0, header=None,
                  names=['Long. de onda', file2[:-4]+' ppm'])
df2.sort_index(inplace=True)
# %%
frames = [df1, df2]
result = pd.concat([df1, df2], axis=1)
# %%
result
# %%
result.to_excel('10 y 100 ppm.xlsx')
