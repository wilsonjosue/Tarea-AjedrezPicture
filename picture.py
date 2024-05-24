from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    """ Invertimos el orden de las filas vertical = self.img[::-1] return vertical"""
    vertical = []#Almacena las imagen del espejo vertucal.
    for value in self.img:
    	vertical.append(value[::-1])  
    return Picture(vertical)
    
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen"""
    horizontal = [] #Almacena las imagen en orden inverso.
    for i in range(len(self.img)-1,-1,-1):#Invierte el orden de las líneas en la imagen.
      horizontal.append(self.img)
    return Picture(horizontal)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

