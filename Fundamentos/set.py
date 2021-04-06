#SET es una coleecion sin orden, sin indices o elementos repetidos y los elementos son inmodificables, si agregar nuevos o existentes

planetas = {"Mercurio", "Venus", 'Tierra', "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"}
print (planetas)

#largo
print(len(planetas));

#Elemento presente en el set
print("Marte" in planetas)
print("Pluton" in planetas)

#agregar
planetas.add("Pluton")
print(planetas)

#agregar existente
planetas.add("Tierra")

#remover
planetas.remove("Pluton")
print(planetas)

planetas.discard("Jupiter")
print(planetas)

#limpiar el set
planetas.clear()
print(">>",planetas)

#Eliminar el set
del planetas