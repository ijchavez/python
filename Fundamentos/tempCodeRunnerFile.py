class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    # sobreescribiendo de Object
    def __add__(self, otro):
        cadena = self.__nombre + " " + self.__apellido + " " + str(self.__edad)
        cadena2 = otro.__nombre + " " + otro.__apellido + " " + str(otro.__edad)
        cadenaTot = cadena + " " + cadena2
        return cadenaTot
    
    def __sub__(self,otro):
        return "Operacion no soportada" 

p1 = Persona("juan","perez", 21)
p2 = Persona("karla","gomez", 34)

print(p1 + p2)
print(p1 - p2)


