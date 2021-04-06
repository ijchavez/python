class Monitor:
    
    contador_monitores = 0
    
    def __init__(self, marca, tamanio):
        # para acceder a esta variable usamos el nombre de la clase y la variable
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio
    
    def __str__(self):
        cadena = (
            f"ID: {self.__id_monitor}, "
            f"Marca: {self.__marca}, "
            f"Tamaño: {self.__tamanio} Pulgadas"
            
        )
        return cadena

# monitor = Monitor("HP", "23")
# print(monitor)