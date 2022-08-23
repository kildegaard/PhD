import csv
import os
from matplotlib import pyplot as plt
import pandas as pd

# path = '../parse_espectro/archivos_csv'
# file_1 = os.listdir(path)[2]
# path_util = os.path.join(path, file_1)
# print(path_util)

# path_1 = 'C:\\Users\\Gustavo\\Desktop\\cosas lignina\\CurvaCalibLignina\\archivos_csv'
# path_2 = os.listdir(path_1)[0]
# todos_los_path = [os.path.join(path_1, os.listdir(path_1)[i])
#                   for i in range(len(os.listdir(path_1)))]
# path_util = os.path.join(path_1, path_2)

os.chdir('archivos_csv')
todos_los_path = os.listdir()
print(todos_los_path)
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

    ax.set_ylim([0, 1])
    ax.set_xlim([309, max(X)])

    ax.grid(True)
    ax.plot(X, Y, label=nombre)
    ax.legend(loc='upper right')

ax.text(320, 0.07, '10 ppm')
ax.text(323, 0.35, '100 ppm')
ax.text(450, 0.6, '1000 ppm')

plt.show()
