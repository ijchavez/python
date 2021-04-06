from figura_geometrica import FiguraGeometrica
from cuadrado import Cuadrado
from rectangulo import Rectangulo

# no es posible crear objetos de una clase abstracta
# figuraGeometrica = FiguraGeometrica()

cuadrado = Cuadrado(4,"Verde")
print(cuadrado)
print("Area: "+ cuadrado.calculoArea())

rectangulo = Rectangulo(3,5,"Gris")
print(rectangulo)
print("Area: "+ rectangulo.calculoArea())

#ver las clases padre de una clase
print(Cuadrado.mro())

