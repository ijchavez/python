class MiClase:
    """cualquier variable definida fuera de cualquier metodo pero dentro de la clase"""
    variable_clase = "Variable de Clase"
    
    """cualquier variable definida dentro del metodo __init__ y en la cual estamos inicializando este valor dentro del metodo"""
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
        
print(MiClase.variable_clase)
objeto1 = MiClase("Variable Instancia")
MiClase.variable_instancia = "Modificando variable de Instancia"
print(MiClase.variable_instancia)
print (objeto1.variable_instancia)

#Podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)

#Podemos acceder a las variables de clase con el nombre de la clase
print(MiClase.variable_clase)

# Si desde el objeto modificamos el valor de la variable de clase solamente se va a ver afectado para el objeto que hizo la modificacion
# Si desde otro objeto no hemos hecho una modificacion vamos a acceder al valor de la variable de clase.
# Si cambiamos la variable de clase, todos los objetos creados a partir de esta clase van a ver este cambio, excepto los que modificaron el valor dentro
# de su objeto
objeto1.variable_clase = "Modificando variable de Clase"
print(objeto1.variable_clase)
print(MiClase.variable_clase)

objeto2 = (MiClase("Nuevo valor Variable Instancia"))
print(objeto2.variable_clase)

objeto3 = MiClase("tercer objeto")

MiClase.variable_clase = "Cambio desde la clase"


print("objeto1, variable de clase >>>", objeto1.variable_clase)
print("objeto2, variable de clase >>>", objeto2.variable_clase)
print("objeto3, variable de clase >>>", objeto3.variable_clase)