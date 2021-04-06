#ABC >> Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    
    def get_ancho(self):
            return self.__ancho
    
    def set_ancho(self, ancho):
        self.__ancho = ancho
    
    def get_alto(self):
            return self.__alto
    
    def set_alto(self, alto):
        self.__ancho = alto
        
    def __str__(self):
        cadena = "Alto: " + str(self.get_ancho()) + ", Ancho: " + str(self.get_alto()) # se ponen los gets a partir de que creo los constructores
        return cadena
    
    @abstractmethod
    def calculoArea(self):
        pass