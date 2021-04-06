# comparacion de dos expresiones booleanas
a = int(input("Ingrese un valor "))

#rango
valorMinimo = 0
valorMaximo = 5

# ambas deben ser verdaderas para que sea true
dentroRango = a >= valorMinimo and a <= valorMaximo
#print(dentroRango)
if(dentroRango):
    print("Dentro de rango")
else:
    print("Fuera de rango")
    
vacaciones = False
diaDescanso = False

# una sola debe ser verdaderas para que sea true
if(vacaciones or diaDescanso):
    print("podemos ir al parque")
else:
    print("tienes deberes que hacer")
    
# not invierte el resultado
print(not(vacaciones))

if(not(vacaciones or diaDescanso)):
    print("tienes deberes que hacer")
else:
    print("podemos ir al parque")
    
    