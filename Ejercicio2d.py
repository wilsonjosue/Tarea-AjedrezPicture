from interpreter import draw
from chessPictures import *
from chessPictures import square

"""Crear las imágenes necesarias."""
black_square = square # Imagen vasia negra
white_square = square.negative() # Imagen vasia blanca. 

"""Crea la matriz row vacia"""
row=[]
""" Se realizara un bucle for pra llenar la matriz luego imprimirla"""
for i in range(8):
    if i%2== 0:
        row.append(white_square) 
    else:
        row.append(black_square)

# Dibujar
draw(row)
