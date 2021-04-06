frutas= ("Naranja",'Platano', 'Guayaba')
print (frutas)

#Largo de la tupla
print(len(frutas))

#acceder a un elemento
print(frutas[0])

#navegacion inversa
print(frutas[-1])

#rango
print(frutas[0:2])

#rango
print(frutas[1:])

#rango
print(frutas[:2])

#Modificar una tupla a traves de una lista
#Pasamos tupla > lista
frutasLista = list(frutas)
print(frutasLista)
#Modificamos
frutasLista[1] = "Platanito"
#Pasamos lista > tupla
frutas = tuple(frutasLista)
print(frutas)

#iterar una tupla
for fruta in frutas:
    print(fruta)
    

for fruta in frutas:
    print(fruta, end=" ") #imprime todo junto

#eliminar la variable frutas
del frutas