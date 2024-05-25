from chessPictures import *
from interpreter import draw
from chessPictures import knight

# Crear las imágenes necesarias
white_knight = knight  # Imagen del caballo blanco
black_knight = knight.negative()  # Imagen del caballo negro

# Reflejar las imágenes para que el caballo mire hacia la izquierda
white_knight_left = white_knight.horizontalMirror()
black_knight_left = black_knight.horizontalMirror()

# Crear la tabla 2x2 con las posiciones especificadas
# M11: Caballo blanco mirando a la izquierda
# M10: Caballo negro mirando a la izquierda
# M01: Caballo blanco mirando a la izquierda
# M00: Caballo negro mirando a la izquierda

M11 = white_knight_left
M10 = black_knight_left
M01 = white_knight_left
M00 = black_knight_left

# Unir las imágenes en una tabla 2x2
first_row = M00.join(M01)  # Primera fila de la tabla
second_row = M10.join(M11)  # Segunda fila de la tabla
table = first_row.up(second_row)  # Tabla completa 2x2

# Dibujar la tabla
draw(table)