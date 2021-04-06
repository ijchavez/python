class MiClase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod #Decorador
    def metodo_estatico():
        print("Ejecucion del Metodo Estático >>>")
        print(">>>",MiClase.variable_clase) # si no lo llamo asi pincha porque no tiene manera el metodo de ver a la variable de clase
        # Desde un metodo estatico no podemos acceder a una  variable de instancia
        # print(MiClase.variable_instancia)
    
    @classmethod #Decorador
    def metodo_clase(cls):
        print("Ejecucion del Metodo de Clase -->", str(cls))
        print("-->",cls.variable_clase) # aca no hace falta usar la clase, porque le pasamos el parametro cls y el mismo nos permite acceder a las variables
        # No podemos acceder a la variable de instancia desde un contexto estatico o de clase
        # print(cls.variable_instancia)
        
    def metodo_instancia(self):
        print("Ejecucion de metodo_instancia")
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_estatico()
MiClase.metodo_clase()

print()
objeto1 = MiClase()
objeto1.metodo_instancia()