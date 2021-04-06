#Imprimir solo las letras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break # en el primer encuentro rompe el ciclo for
else:
        print("Fin ciclo for")
        
#Imprimir pares en un rango

for i in range(6):
    if i %2 == 0:
        print (i)


for i in range(6):
    #Si el residuo es distinto de cero segui (continue)
    if i %2 != 0:
        continue
    print(i)