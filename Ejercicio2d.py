from interpreter import draw
from chessPictures import *
from chessPictures import square

"""Crear las imágenes necesarias."""
black_square = square.negative() # Imagen vacia negra.
white_square = square# Imagen vacia blanca. 

"""Crea la matriz row vacia"""
row=[]
n=8
""" Se realizara un bucle for pra llenar la matriz luego imprimirla"""
for i in range(n):
    if i%2== 0:
        row.append(white_square) 
    else:
        row.append(black_square)

"""Forma de unir los datos del arreglo row"""
row_picture = row[0]# Asignar a row_picture el primer elemento de row.

"""join(self, p):Devuelve nueva figura poniendo la figura del argumento al lado derecho de la figura actual"""
for i in range(1,len(row)):#Unir todas las imágenes en una fila.
    row_picture=row_picture.join(row[i])#Los pone a su lado derecho.

# Dibujar
draw(row_picture)
