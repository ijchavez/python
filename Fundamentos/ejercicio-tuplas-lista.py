#Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: 
tupla = (13, 1, 8, 3, 2, 5, 8)
listaMenoresDeCinco = []

for numero in tupla:
    if numero < 5:
        listaMenoresDeCinco.append(numero)

print("Numeros:",listaMenoresDeCinco)