class Vehiculo: # Por defecto hereda de la clase object
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    """Definimos el __str__ sobreescribiendo el que viene por defecto, pasamos el self dentro"""
    def __str__(self):
        cadena = "Color: "+ self.color + ", Ruedas: " + str(self.ruedas)
        return cadena
    
class Coche(Vehiculo): # SIEMPRE PONER ENTRE PARENTESIS LA CLASE QUE HEREDA
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        cadena = super().__str__() + ", Velocidad: " + str(self.velocidad) + "km/h"
        return cadena    
    

class Bicicleta(Vehiculo): # SIEMPRE PONER ENTRE PARENTESIS LA CLASE QUE HEREDA
    def __init__(self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        cadena = super().__str__() + ", Tipo: " + self.tipo
        return cadena    

vehiculo = Vehiculo ("Rojo", 4)
print(vehiculo)

mercedesBenz = Coche("Verde", 4, 185.00)
print (mercedesBenz)

bmx = Bicicleta("Azul", 2, "Montaña")
print(bmx)
