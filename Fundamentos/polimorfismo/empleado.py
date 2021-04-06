class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __str__(self):
        cadena = "Nombre: " + self.nombre + ", Sueldo: " + str(self.sueldo)
        return cadena