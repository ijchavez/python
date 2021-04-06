class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        """Se realiza el cálculo del area"""
        return self.base * self.altura

#Comentado para ver el preview to the side
#base = int(input("Ingrese la base del rectangulo: "))
#altura = int(input("Ingrese la altura del rectangulo: "))

base = 4
altura = 3

rectangulo = Rectangulo(base,altura)
print ("Resultado Calculo de Area:",rectangulo.calcularArea())