def sumar(a,b):
    suma = a + b
    return suma

def restar(a,b):
    resta = a - b
    return resta

def multiplicar(a,b):
    multiplica = a * b
    return multiplica

def dividir(a,b):
    if (b != 0):
        cociente = a / b
        return cociente
    else:
        mensaje = "No se puede dividir por 0"
        return mensaje