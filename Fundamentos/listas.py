nombres = ['Juan', "Carla", "Ricardo", "María"]
print(nombres)

#largo de la lista
print("Cantidad de elementos de la lista:",len(nombres))

#elemento 0
print(nombres[0])

#mostrar posicion con while
i = 0
while i <= 3:
    print("Posicion",i,"Nombre", nombres[i])
    i += 1

#Navegacion inversa, ultimo nombre de la lista -1
print(nombres[-1])

#Imprimir Rango sin incluir el indice 2
print(nombres[0:2])

#Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3])

#Imprimir los elementos hasta el final desde el indice proporcionado 
print(nombres[1:])

#Cambiar los elementos de una lista
nombres[3] = "Ivonne"
print (nombres[3])
print(nombres)

#imprimir nombres con un for
for nombre in nombres:
    print(nombre)

#Revisar si existe un elemento en una lista
nombrePedido = input("Ingrese un nombre para verificar si esta en la lista: ")
if nombrePedido in nombres:
    print((nombrePedido), "Existe en la lista")
else:
    print((nombrePedido), "No existe en la lista")

#Ingresar un valor a una lista
nombrePedido = input("Ingrese un nombre para agregar en la lista: ")
nombres.append(nombrePedido)
print(nombres)

#Insertar un elemento en un indice proporcionado
nombrePedido = input("Ingrese un nombre para agregar en la lista: ")
indicePedido = int(input("ingrese el indice donde se va a ingresar el nombre: "))
nombres.insert(indicePedido,nombrePedido)
print(nombres[indicePedido])
print(nombres)

#Remover un elemento de la lista
nombreARemover = input("indique un nombre a remover: ")
if nombreARemover in nombres:
    nombres.remove(nombreARemover)
    print(nombres)
else:
    print((nombreARemover), "No existe en la lista")

#Remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

#Remover un elemento en un indice indicado
indiceIndicado = int(input("Indique el indice a remover"))
del(nombres[indiceIndicado])
print(nombres)

#Limpiar los elementos de una lista
nombres.clear()
print (nombres)

#Borrar la variable
del nombres