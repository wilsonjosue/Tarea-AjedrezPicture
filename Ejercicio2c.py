from interpreter import draw
from chessPictures import *
from chessPictures import queen

"""Crear las imágenes necesarias."""
white_queen = queen # Imagen del la reyna blanca. 

"""Posiciones de la reina blanca."""
M00 = white_queen # reyna blanca blanco. 

""" Devuelve una nueva figura repitiendo la actual al costado la cantidad que indique el valor de n """
repetir_queen = white_queen.horizontalRepeat(4) # Primera fila de la tabla

# Dibujar
draw(repetir_queen)
