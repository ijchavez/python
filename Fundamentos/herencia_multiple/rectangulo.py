from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def calculoArea(self):
        resultado = self.get_alto() * self.get_ancho()
        return str(resultado)

    def __str__(self):
        cadena = FiguraGeometrica.__str__(self) + ", Color: "+ self.get_color()
        return cadena