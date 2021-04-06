listaNumeros = [0,1,2,3,4,5,6,7,8,9,10]
print(listaNumeros)
for numero in listaNumeros:
    if numero %3 != 0:
        continue
    else:
        print(numero)
        
#Alternativa
print(listaNumeros)
for numero in listaNumeros:
    if numero %3 == 0:
        print(numero)
