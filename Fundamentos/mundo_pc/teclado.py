from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self, marca, tipo_entrada):
        # para acceder a esta variable usamos el nombre de la clase y la variable
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados # le asignamos este valor que es unico
        # argumentos protegidos
        self._marca = marca
        self._tipo_entrada = tipo_entrada
    
    def __str__(self):
        cadena = (
            #f"" es f-string
            f"ID:  {self.__id_teclado}, "
            f"Marca: {self._marca}, "
            f"Tipo de Entrada: {self._tipo_entrada}"
            
        )
        return cadena

# teclado = Teclado("hp","usb")
# print(teclado)