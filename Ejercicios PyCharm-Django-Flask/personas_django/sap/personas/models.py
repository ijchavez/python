from django.db import models

# Create your models here.
# Con este archivo creo lo necesario para importar luego otro archivo que finalizara creando una BD en postgres
# Los metodos STR son los que van a mostrarse en la pagina en django

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        cadena = f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'
        return cadena


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    #domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE(), null=True) # Esto es para que si se borra de una tabla se borra en cascada en la otra

    def __str__(self):
        cadena = f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
        return cadena