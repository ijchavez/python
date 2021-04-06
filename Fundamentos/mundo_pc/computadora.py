from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:
    contador_computadora = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.__id_computadora = Computadora.contador_computadora
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self):
        cadena = (
            # separamos entre diferentes lineas con f """""" >> se imprimen todos los espacios tabulados
            f"""
            {self.__nombre}: {self.__id_computadora}
                Monitor: {self.__monitor}
                Teclado: {self.__teclado}
                Ratón: {self.__raton}
            
            """
        )
        return cadena

# monitor1 = Monitor("HP", 15)
# teclado1 = Teclado("Genius","usb")
# raton1 = Raton("Logitech", "bluetooth")
# computadora1 = Computadora("HP", monitor1, teclado1,raton1)
# print(computadora1)