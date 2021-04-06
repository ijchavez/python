from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        # para acceder a esta variable usamos el nombre de la clase y la variable
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones # le asignamos este valor que es unico
        # argumentos protegidos
        self._marca = marca
        self._tipo_entrada = tipo_entrada
    
    def __str__(self):
        cadena = (
            #f"" es f-string
            f"ID:  {self.__id_raton}, "
            f"Marca: {self._marca}, "
            f"Tipo de Entrada: {self._tipo_entrada}"
            
        )
        return cadena

#raton = Raton("hp","usb")
#print(raton)