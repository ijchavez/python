class Persona: # Por defecto hereda de la clase object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    """Definimos el __str__ sobreescribiendo el que viene por defecto, pasamos el self dentro"""
    def __str__(self):
        cadena = "Nombre: "+ self.nombre + ", Edad: " + str(self.edad)
        return cadena
    

class Empleado(Persona):
    """Definimos el init en esta clase, pasamos el self y todos los parametros de la clase padre"""
    """mas los atributos de la clase propia y para inicializar el super().__init__"""
    def __init__(self, nombre, edad, sueldo):
         super().__init__(nombre, edad)
         self.sueldo = sueldo
    
    """Sobreescribimos el metodo anterior llamando al super().__str__() + 'lo que queramos agregar' """
    def __str__(self):
        cadena = super().__str__() + ", Sueldo: " + str(self.sueldo)
        return cadena
             


persona = Persona("Juan", 28)
print(persona.nombre, persona.edad)
print(persona)

empleado = Empleado("Jorge", 22, 1200.00)
print(empleado)

empleado.nombre = "Karla Ivonne"
empleado.sueldo = 1000.00
print(empleado)