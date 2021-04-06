class Persona:
    def __init__(this, name, age, *v, **d):
        """self o this es un apuntador al objeto que se esta ejecutando en este momento, * es un parametro opcional ** es diccionario"""
        this.nombre = name
        this.edad = age
        this.valores = v
        this.diccionario = d
        
    def desplegar(this):
        print("Nombre:", this.nombre)
        print("Edad:", this.edad)
        print("Valores (Tupla):",this.valores)
        print("Diccionario:", this.diccionario)       

        
p1 = Persona("Juan", 22)
print(p1.nombre, p1.edad)
p1.desplegar()
print("*****")
p2 = Persona("Jorge", 31, 2,4,5)
p2.desplegar()
print("*****")
p3 = Persona("Marla", 18, 4,9, m = "manzana", p = "pera", j = "jicama")
p3.desplegar()