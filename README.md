# PhD
Programitas útiles para el doctorado :3

1. `parse_espectros.py`  Este programa está pensado para parsear los archivitos que salen del espectro del PINMATE usando el programa de Android **Serial USB Terminal**. Modo de uso: colocar los espectros en formato *.txt* dentro de una carpeta *archivos_txt*. Ejecutar el programa al mismo nivel que la carpeta.
2. `csv_to_excel.py`    Este programa convierte una serie de archivos csv a un excel. Los archivos csv deben estar en una carpeta *archivos_csv* al mismo nivel que el programa. Se le puede pasar un argumento que es el *path* de destino del excel (es necesario explicitar el .xlsx)
3. `graficar_espectros.py`  Este programa genera un gráfico de todos los espectros superpuestos en un mismo archivo. Se le puede especificar una serie de parámetros: *nada* -> grafica todo en todo el rango de datos; *beer* -> grafica eje X en todo el rango y el eje Y de 0 a 1; *MIN_X MAX_X MIN_Y MAX_Y* -> grafica con esos intervalos.