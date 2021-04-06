condicion = True

if condicion == True:
    print("condicion es Verdadera")
elif condicion == False:
    print("condicion es Falsa")
else:
    print("condicion No Reconocida")

print(">>> Condicion Verdadera") if condicion else print(">>> Condicion Falsa")

numero = int(input("Ingrese un numero entre 1-3: "))

if numero == 1:
    numeroTexto = "Numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "Numero tres"
else:
    numeroTexto = "Numero invalido"

print("Numero proporcionado", numeroTexto)

