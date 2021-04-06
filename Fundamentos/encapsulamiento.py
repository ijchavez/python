class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        """__ indica que es privado para accederlos necesitamos el get y set"""
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
        
    def set_edad(self, edad):
        self.__edad = edad


p1 = Persona("Juan",28)
# da error print(p1.__nombre)
print(p1.get_nombre(),p1.get_edad())

p1.set_nombre("Karla")
p1.set_edad(34)
#p1.nombre = "Karla"
print(p1.get_nombre(), p1.get_edad())
