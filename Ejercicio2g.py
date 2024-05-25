from interpreter import draw
from chessPictures import *


"""Crear las imágenes necesarias."""
black_square = square.negative() # Imagen vacia negra.
white_square = square # Imagen vacia blanca. 
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

""" Se realizara un bucle for para llenar la matriz empezando con el casillero para cada tipo"""
# Crea una matriz 8x8 para representar el tablero
tablero = [[None] * 8 for _ in range(8)]

# Llena el tablero con las casillas alternadas
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            tablero[i][j] = white_square
        else:
            tablero[i][j] = black_square

# Coloca las piezas de ajedrez sobre las casillas correspondientes
# Por ejemplo, aquí colocamos peones en las filas 2 y 7
for j in range(8):
    tablero[1][j] = pawn_black.over(pawn_black) # Superponer peón negro sobre casilla
    tablero[6][j] = pawn_white.over(pawn_white) # Superponer whire negro sobre casilla

# Dibuja el tablero con las piezas
draw(tablero)


