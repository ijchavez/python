# Si estan en la misma carpeta: import modulo_aritmetica as aritmetica
# Si estan en carpetas difedentes:
# from 'carpeta' import 'nombre de archivo' as 'nombre'
from modulos import modulo_aritmetica as aritmetica
#import modulos.modulo_aritmetica as aritmetica
# import carpeta.nombre_archivo as nombre
 
a = 1
b = 2

resultado = aritmetica.sumar(a,b)
print("Suma:",a,"+", b, "=",resultado)

a = 8
b = 6

resultado = aritmetica.restar(a,b)
print("Resta:",a,"-", b, "=",resultado)

a = 3
b = 7

resultado = aritmetica.multiplicar(a,b)
print("Multiplicacion:",a,"x", b, "=",resultado)

a = 10
b = 5

resultado = aritmetica.dividir(a,b)
print("División:",a,"%", b, "=",resultado)