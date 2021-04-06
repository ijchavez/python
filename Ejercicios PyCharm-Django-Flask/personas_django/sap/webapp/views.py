from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
   # cadena = 'Hola Mundo'
   # return HttpResponse(cadena)
   no_personas = Persona.objects.count()
   # comento la siguiente linea para cambio orderby en la tabla
   #personas = Persona.objects.all()
   personas = Persona.objects.order_by('id')
   no_domicilio = Domicilio.objects.count()
   # comento la siguiente linea para cambio orderby en la tabla
   #domicilio = Domicilio.objects.all()
   domicilio = Domicilio.objects.order_by('id') # -id para de forma descendente (id,nombre) >> podria agregar mas de un campo para ordenar
   #{'definicion del termino': variable}
   # return render(request, 'bienvenido.html', {'no_personas': no_personas})
   return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas, 'no_domicilio': no_domicilio, 'domicilios': domicilio})

