numero = float(input("Ingrese una nota entre 1-10: "))
nota = None

if numero >= 9 and numero <= 10:
    nota = "A"
    
elif numero >= 8 and numero < 9:
    nota = "B"
    
elif numero >= 7 and numero < 8:
    nota = "C"
    
elif numero >= 6 and numero < 7:
    nota = "D"
    
elif numero >= 0 and numero < 6:
    nota = "F"
    
else:
    nota = "Valor desconocido"
    
print("Nota numérica", numero, "Corresponde la nota:", nota)