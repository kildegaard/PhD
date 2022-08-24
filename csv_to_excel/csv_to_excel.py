import os
import pandas as pd
import sys


def crear_excel(path_destino='archivo_Excel.xlsx'):
    os.chdir('archivos_csv')
    file_list = os.listdir('.')

    list_of_df = []

    for file in file_list:
        df = pd.read_csv(file, index_col=0, header=None,
                         names=['Long. de onda', file[:-4]+' ppm'])
        df.sort_index(inplace=True)

        list_of_df.append(df)

    big_df = pd.concat(list_of_df, axis=1)

    os.chdir('..')
    big_df.to_excel(path_destino[0])


def main(arg):
    if len(arg) == 0:
        crear_excel()
    elif len(arg) == 1:
        crear_excel(arg)
    else:
        SystemExit('Flashaste')


if __name__ == '__main__':
    arg = sys.argv[1:]
    main(arg)
