diccionario = {
    "IDE" : "Integrated Develompment Environment",
    "OOP" : "Object Oriented Programming",
    "DMBS": "Database Managment System"
}
print(diccionario)

# Largo
print(len(diccionario))

# Acceder a un elemento del diccionario:
print(diccionario["IDE"])

print(diccionario.get("IDE"))

# Modificando valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario["IDE"])
print(diccionario.get("IDE"))

# Iterar imprimiendo las llaves
for termino in diccionario:
    print(termino)
    
# Iterar imprimiendo los valores    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print (valor)

# Comprobar existencia
llave = input("Ingrese key para ver si existe: ")
print(llave in diccionario)

# Agregar elementos
diccionario["PK"] = "Primary Key"

termino = input("Ingrese llave: ")
valor = input("Ingrese valor de la llave: ")
diccionario[termino] = valor
print(diccionario)

# Remover elementos 
diccionario.pop("ASD")
print(diccionario)

# Limpiar/Eliminar elementos del diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario