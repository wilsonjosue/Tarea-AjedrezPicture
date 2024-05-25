from interpreter import draw
from chessPictures import *


"""Crear las imágenes necesarias."""
pawn_black = pawn.negative() #_black negro
pawn_white = pawn
bishop_black = bishop.negative()
bishop_white = bishop
knight_black = knight.negative()
knight_white = knight
rock_black = rock.negative()
rock_white = rock
king_black = king.negative()
king_white = king
queen_black = queen.negative()
queen_white = queen

"""Ingresamos los datos a la tabla para las piezas negras"""
posicion_inicial =[
    rock_black, knight_black, bishop_black, queen_black, king_black, bishop_black, knight_black, 
    rock_black,pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, pawn_black, 
    pawn_black,
]

# Organiza las imágenes de las piezas en el tablero
tablero = posicion_inicial[0]  # Inicializa el tablero con la primera imagen de la lista

n = 8  # Número de casillas en una fila.

"""Une las imágenes horizontalmentelizara un bucle for para llenar la matriz empezando con el casillero para cada tipo"""
for img in initial_positions[1:]:
    tablero = tablero.join(img)  # Une las imágenes horizontalmente
"""Unir los dos con up para unir las filas de p.img encima de las filas de self.img""" 

# Dibujar
draw(tablero)

