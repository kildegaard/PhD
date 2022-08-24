import os
import pandas as pd
import sys

os.chdir('archivos_csv')
file_list = os.listdir('.')

list_of_df = []

for file in file_list:
    df = pd.read_csv(file, index_col=0, header=None,
                     names=['Long. de onda', file[:-4]+' ppm'])
    df.sort_index(inplace=True)

    list_of_df.append(df)

big_df = pd.concat(list_of_df, axis=1)

big_df.to_excel('algo.xlsx')
