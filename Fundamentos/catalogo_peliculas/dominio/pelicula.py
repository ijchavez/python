class Pelicula:
    def __init__(self, nombre_pelicula):
        self.__nombre = nombre_pelicula
        
    def __str__(self):
        cadena =  self.__nombre
        return cadena
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre_pelicula):
        self.__nombre = nombre_pelicula
