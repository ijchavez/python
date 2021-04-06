from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print("Tipo de variable que recibimos:",type(objeto))
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado_01 = Empleado("Juan", 1000.00)
empleado_02 = Gerente("Pedro", 1200.00, "Sistemas")

imprimir_detalles(empleado_01)
imprimir_detalles(empleado_02)

