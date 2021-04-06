
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id)
    # si no existe redirige a una pagina no encontrada.
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


# PersonaForm = modelform_factory(Persona, exclude=[])

################ PERSONAS ################

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)

        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
        """return render(request, 'nueva pagina', {diccionario: elemento} """
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)

        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        persona = get_object_or_404(Persona, pk=id)
        formaPersona = PersonaForm(instance=persona)
        """return render(request, 'nueva pagina', {diccionario: elemento} """
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

################ DOMICILIOS ################

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle_domicilios.html', {'domicilio': domicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)

        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
        """return render(request, 'nueva pagina', {diccionario: elemento} """
    return render(request, 'domicilios/nuevo_domicilio.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)

        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        domicilio = get_object_or_404(Domicilio, pk=id)
        formaDomicilio = DomicilioForm(instance=domicilio)
        """return render(request, 'nueva pagina', {diccionario: elemento} """
    return render(request, 'domicilios/editar_domicilio.html', {'formaDomicilio': formaDomicilio})


def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('index')