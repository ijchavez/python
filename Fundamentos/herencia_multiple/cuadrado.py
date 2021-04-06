from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def calculoArea(self):
        resultado = self.get_alto() * self.get_ancho()
        return str(resultado)

    def __str__(self):
        cadena = FiguraGeometrica.__str__(self) + ", Color: "+ self.get_color()
        return cadena