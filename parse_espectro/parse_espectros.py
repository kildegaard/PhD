# parse_espectro.py
'''
Programa para parsear los arhivos del espectro del PINMATE
'''

import os


def parse_espectro(file_in, file_out):
    # Abro el archivo y guardo en una lista las líneas ya con formato csv

    # with open(sys.argv[1:][0], 'rt') as file:
    with open(file_in, 'rt') as file:
        data = []
        for linea in file:
            if not linea:
                continue
            linea_parseada = linea.strip().split('  ')
            try:
                data.append(linea_parseada[1] + ', ' + linea_parseada[2])
            except:
                pass

    # Creo un archivo a partir de la lista anterior
    with open(file_out, 'w') as output_file:
        for n_linea, linea in enumerate(data, start=1):
            if n_linea < len(data):
                print(linea, file=output_file)
            else:
                print(linea, file=output_file, end='')


def main():
    try:
        os.mkdir('archivos_csv')
    except:
        pass
    lista_archivos = os.listdir('./archivos_txt')
    lista_de_serial = [
        archivo for archivo in lista_archivos if 'serial' in archivo]

    print(lista_de_serial)

    for archivo in lista_de_serial:
        nombre_output = './archivos_csv/' + archivo[:-3] + 'csv'
        archivo = './archivos_txt/' + archivo
        parse_espectro(archivo, nombre_output)


if __name__ == '__main__':
    main()
