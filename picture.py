from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  """ row en Python,se refiere a una fila específica dentro de una estructura de datos bidimensional."""

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    #Invertimos el orden de las filas vertical = self.img[::-1] return vertical"""
    vertical = []#Almacena las imagen del espejo vertucal.
    for row in self.img:
    	vertical.append(row[::-1]) 
    return Picture(vertical)
      
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen"""
    horizontal = [] #Almacena las imagen en orden inverso.
    for i in range(len(self.img)-1,-1,-1):#Invierte el orden de las líneas en la imagen.
      horizontal.append(self.img) #Para añadir un elemento al final de una lista
    return Picture(horizontal)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = [] # Almacena el negatico de la imagen.
    for row in self.img: #Convierte cada carácter de fila a su color negativo
      neg_row = ''.join([self._invColor(c) for c in row])
      negative.append(neg_row)#Une los caracteres en una nueva fila
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    imgUnido = []  # Lista para almacenar la imagen unida
    for row1, row2 in zip(self.img,p.img):#Itera sobre las filas de ambas imágenes
       imgUnido.append(row1+row2)#Une las filas de ambas imágenes y las añade a la lista
    return Picture(imgUnido) #Devuelve una nueva instancia de Picture con la imagen unida

  def up(self, p):
    devolver = p.img + self.img # Une las filas de p.img encima de las filas de self.img
    return Picture(devolver)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p debajo de la
        figura actual """
    devolver = self.img + p.img  #Une las filas y colocar la figura p debajo de la figura actual.
    return Picture(devolver)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repitiendo = []#Lista para almacenar la imagen repetida 
    for row in self.img: #Itera sobre cada fila de la imagen
      repitiendo.append(row*n) #Repite la fila n veces y la añade a la lista
    return Picture(repitiendo)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo la cantidad de veces que indique el valor de n """
    repetirV = (self.img*n) 
    return Picture(repetirV)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario o antihorario"""
    #Luego invierte el orden de las filas
    #rotated = [''.join(row) for row in zip(*self.img[::-1])]
    transpose= list.zip(*self.img)#Transpone la matriz (intercambia filas por columnas)
    rotar= ["".join(row) for row in transpose[::-1]]#Luego invierte el orden de las filas
    return Picture(rotar)# Devuelve una nueva instancia de Picture con la imagen rotada
# Fin de la clase Picture 

