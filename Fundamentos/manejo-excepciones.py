from numeros_identicos_exception import NumerosIdenticosException

division = None

try:
    divisor =  int(input("Ingrese un numero: "))
    dividendo = int(input("Ingrese un numero: "))
    
    if divisor == dividendo:
        raise NumerosIdenticosException("números idénticos")
    
    division = divisor / dividendo
    print("Resultado:",division)
    
except ZeroDivisionError as e:
    print("No se puede dividir por", dividendo, "excepción:", e)
    print("Tipo de excepción:",type(e))

except TypeError as e:
    print("No se puede dividir por un valor de cadena", "excepción:", e)
    print("Tipo de excepción:",type(e))

except ValueError as e:
    print("No se puede dividir una cadena", "excepción:", e)
    print("Tipo de excepción:",type(e))

except Exception as e:
    print("Se produjo un error", e)
    print("Tipo de excepción:",type(e))

else: # opcional
    print("No hubo ninguna excepción")

finally: # opcional
    print("Fin del manejo de excepciones")

print("continuamos")