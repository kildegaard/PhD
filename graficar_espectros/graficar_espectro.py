import csv
import os
from matplotlib import pyplot as plt

# path = '../parse_espectro/archivos_csv'
# file_1 = os.listdir(path)[2]
# path_util = os.path.join(path, file_1)
# print(path_util)

path_1 = 'C:\\Users\\Gustavo\\Desktop\\cosas lignina\\CurvaCalibLignina\\archivos_csv'
path_2 = os.listdir(path_1)[0]
todos_los_path = [os.path.join(path_1, os.listdir(path_1)[i])
                  for i in range(len(os.listdir(path_1)))]
path_util = os.path.join(path_1, path_2)

for path in todos_los_path:
    with open(path, 'rt', encoding='utf-8') as f:
        archivo = csv.reader(f)
        X = []
        Y = []
        for linea in archivo:
            X.append(float(linea[0]))
            Y.append(float(linea[1]))

    fig, ax = plt.subplots()
    ax.plot(X, Y)
    plt.show()
