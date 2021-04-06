class Producto:
    """Contador que se incrementara con cada creacion de un producto"""   
    contador_productos = 0
 
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio

    def __str__(self):
        cadena = "ID Producto: " + str(self.__id_producto) + " Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
        return cadena