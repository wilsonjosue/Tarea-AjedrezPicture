from interpreter import draw
from chessPictures import *
from interpreter import draw
from chessPictures import knight

# Crear las imágenes necesarias.
white_knight1 = knight # Imagen del caballo blanco. 
black_knight1 = knight.negative() # Imagen del caballo negro. 

white_knight_mirrow = white_knight1.horizontalMirror() # Imagen del caballo blanco 
black_knight1_mirrow = black_knight1.horizontalMirror() # Imagen del caballo negro 

# Posiciones de los caballos Mij variable.
M01 = white_knight1 # Caballo blanco en la esquina superior derecha
M00 = black_knight1 # Caballo negro en la esquina inferior derecha
# Posiciones de los caballos Mij variable Devuelve el espejo horizontal de la imagen
M10 = white_knight_mirrow # Caballo blanco en la esquina superior izquierda
M11 = black_knight1_mirrow # Caballo negro en la esquina inferior izquierda

# Unir las imágenes en una tabla 2x2
first_row = M00.join(M01)  # Primera fila de la tabla
second_row = M10.join(M11)  # Segunda fila de la tabla
table = first_row.under(second_row)  # Tabla completa 2x2

# Dibujar la tabla
draw(table)
