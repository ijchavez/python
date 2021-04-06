class Caja:
    def __init__(self, base, altura, profundidad):
        self.base = base
        self.altura = altura
        self.profundidad = profundidad
    
    def calcularVolumen(self):
        """Se realiza el cálculo del Volumen"""
        return self.base * self.altura * self.profundidad


base = 5
altura = 3
profundidad = 6

volumen = Caja(base, altura, profundidad)
print("Volumen:",volumen.calcularVolumen(),"Metros cubicos")