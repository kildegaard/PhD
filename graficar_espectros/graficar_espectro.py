'''
Este programa agarra una carpeta 'archivos_csv' con los csv ya creados anteriormente y genera
un gráfico con los datos superpuestos.

USO: 
py graficar_espectro.py -> Te grafica todos los archivos csv juntos, con x e y en todo el rango de datos

py graficar_espectro.py lindo -> Idem pero y va de 0 a 1 (como sería de esperar para un espectro)

py graficar_espectro.py X_INF X_SUP Y_INF Y_SUP -> Grafica usando esos límites en particular

Por lo general conviene graficar sin argumentos y luego aplicarle los limites que uno crea convenientes

'''

import sys
import csv
import os
from matplotlib import pyplot as plt


def graficar_todo_junto(INF_X=0, SUP_X=None, INF_Y=0, SUP_Y=1, todo_el_rango=False, tipico_graf=False):
    os.chdir('archivos_csv')
    todos_los_path = os.listdir()

    fig, ax = plt.subplots()

    for path in todos_los_path:
        with open(path, 'rt', encoding='utf-8') as f:
            archivo = csv.reader(f)
            X = []
            Y = []
            for linea in archivo:
                X.append(float(linea[0]))
                Y.append(float(linea[1]))

        nombre = f'{path[:-4]} ppm'
        if todo_el_rango:
            ax.set_xlim([min(X), max(X)])
            ax.set_ylim([min(Y), max(Y)])
        elif tipico_graf:
            ax.set_xlim([min(X), max(X)])
            ax.set_ylim([0, 1])
        else:
            ax.set_xlim([INF_X, SUP_X])
            ax.set_ylim([INF_Y, SUP_Y])

        ax.grid(True)
        ax.plot(X, Y, label=nombre)
        ax.legend(loc='upper right')

    plt.show()


def main(args):
    if len(args) == 0:
        graficar_todo_junto(todo_el_rango=True)
    elif args[0] == 'beer':
        graficar_todo_junto(tipico_graf=True)
    if len(args) == 4:
        # Usando map le aplico la función float a todos los elementos de la lista
        args = list(map(float, args))
        INF_X, SUP_X, INF_Y, SUP_Y = args
        graficar_todo_junto(INF_X, SUP_X, INF_Y, SUP_Y)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
