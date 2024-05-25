from interpreter import draw
from chessPictures import *
from chessPictures import knight

# Crear las imágenes necesarias.
white_knight = knight # Imagen del caballo blanco. 
black_knight = knight.negative() # Imagen del caballo negro. 

white_knight_mirrow = white_knight.horizontalMirror() # Imagen del caballo blanco 
black_knight_mirrow = black_knight.horizontalMirror() # Imagen del caballo negro 

# Posiciones de los caballos Mij variable.
M00 = white_knight # Caballo blanco. 
M01 = black_knight # Caballo negro.
# Posiciones de los caballos Mij variable Devuelve el espejo horizontal de la imagen
M10 = black_knight_mirrow # Caballo blanco.
M11 = white_knight_mirrow # Caballo negro.

# Unir las imágenes en una tabla 2x2
first_row = M00.join(M01)  # Primera fila de la tabla
second_row = M10.join(M11)  # Segunda fila de la tabla
table = first_row.under(second_row)  # Tabla completa 2x2

# Dibujar la tabla
draw(table)
