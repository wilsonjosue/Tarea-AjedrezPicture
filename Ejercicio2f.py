from interpreter import draw
from chessPictures import *

"""Crear las imágenes necesarias."""
black_square = square.negative() # Imagen vacia negra.
white_square = square # Imagen vacia blanca. 

"""Crea la matriz row1 y row2 vacia"""

row1 = []  # Primera fila: empieza con casilla blanca.
row2 = []  # Segunda fila: empieza con casilla negra.

n = 8  # Número de casillas en una fila.

""" Se realizara un bucle for para llenar la matriz empezando con el casillero para cada tipo"""
for i in range(n):
    if i % 2 == 0:
        row1.append(white_square)
        row2.append(black_square)
    else:
        row1.append(black_square)
        row2.append(white_square)

"""Forma de unir los datos del arreglo row"""
row1_picture = row1[0]# Asignar a row_picture el primer elemento de row1.
row2_picture = row2[0]# Asignar a row_picture el primer elemento de row2.
"""join(self, p):Devuelve nueva figura poniendo la figura del argumento al lado derecho de la figura actual"""

for i in range(1,len(row1)):#Unir todas las imágenes en una fila.
    row1_picture=row1_picture.join(row1[i])#Los pone a su lado derecho.
    row2_picture=row2_picture.join(row2[i])#Los pone a su lado derecho.

"""Unir los dos con up para unir las filas de p.img encima de las filas de self.img""" 
nueva_tabla=row2_picture.up(row1_picture).up(row2_picture).up(row1_picture)
# Dibujar
draw(nueva_tabla)