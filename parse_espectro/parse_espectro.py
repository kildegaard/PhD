# parse_espectro.py
'''
Programa para parsear los arhivos del espectro del PINMATE
'''

import sys
import csv


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


def main(args):
    if len(args) == 2:
        parse_espectro(*args)
    else:
        raise SystemExit('Uso: ...')  # TODO: Falta poner mensajito acá


if __name__ == '__main__':
    main(sys.argv[1:])
