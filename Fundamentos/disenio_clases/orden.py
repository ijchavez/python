class Orden:
    """Contador que se incrementara con cada creacion de una orden"""
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
    
    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total

    def __str__(self):
        productos_str =  ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " | "

        cadena = "Orden: " + str(self.__id_orden) + ", Productos: " + productos_str
        return cadena