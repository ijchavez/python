a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
# la suma la pongo dentro de la funcion xq si la pongo afuera pone los valores de los input
def sumar(a=0, b=0):
    #return a+b;
    suma = a + b;
    return suma;

print("Resultado:",sumar(a,b))

print("Resultado sin especificar parametros:",sumar())

print("Resultado con valores especificos:",sumar(5,4))