from chessPictures import *
from interpreter import draw
from chessPictures import knight

# Crear las imágenes necesarias
white_knight = knight # Imagen del caballo blanco 
black_knight = knight # Imagen del caballo negro 

hite_knight = Picture(knight)  # Imagen del caballo blanco
black_knight = Picture(knight.negative())  # Imagen del caballo negro
# Posiciones de los caballos
M11 = white_knight # Caballo blanco en la esquina superior derecha
M10 = black_knight # Caballo negro en la esquina inferior derecha
M01 = white_knight # Caballo blanco en la esquina superior izquierda
M00 = black_knight # Caballo negro en la esquina inferior izquierda

# Unir las imágenes en una tabla 2x2
first_row = M00.join(M01)  # Primera fila de la tabla
second_row = M10.join(M11)  # Segunda fila de la tabla
table = first_row.under(second_row)  # Tabla completa 2x2

# Dibujar la tabla
draw(table)