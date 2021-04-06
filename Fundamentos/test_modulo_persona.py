# Si estan en una misma carpeta es from 'archivo' import 'clase'
# from modulo_persona import Persona
# Si estan en una carpeta diferente from 'carpeta'.'archivo' import 'clase'
from modulos.modulo_persona import Persona


p1 = Persona("Juan", 28)
print(p1)