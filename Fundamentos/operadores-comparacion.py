a = 3
b = 2

# == devuelve un booleano comparacion de igualdad
resultado = a == b
print("Comparación de igualdad:",resultado)

# != comparacion de diferente
resultado = a != b
print("Comparacion de diferente:",resultado)

# > mayor
resultado = a > b
print("Comparador de mayor:",resultado)

# >= mayor o igual
resultado = a >= b
print("Comparador de mayor o igual:",resultado)

# < menor
resultado = a >= b
print("Comparador de menor:",resultado)

# <= menor
resultado = a <= b
print("Comparador de menor o igual:",resultado)

if  a%2 == 0:
    print("Es par")
else:
    print("Es impar")

if  b%2 == 0:
    print("Es par")
else:
    print("Es impar")
    
edadLimite = 18
edad = int(input("Ingrese una edad:"))

if edad >= edadLimite:
    print("es un adulto")
else:
    print("es menor de edad")
    