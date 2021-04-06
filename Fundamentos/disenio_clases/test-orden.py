from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 200.00)
producto3 = Producto("Calcetines", 50.00)

productos = [producto1, producto2]
print(productos)

orden1 = Orden(productos)
print(orden1)
print("Total: $",orden1.calcular_total())


orden2 = Orden(productos)
orden2.agregar_producto(producto3) # agrego un producto a la lista de productos

print(orden2)
print("Total: $",orden2.calcular_total())