from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        """Vamos a utilizar todos los atributos, indicamos __all__
        Tipo de campo de formulario usamos el atributo widgets que es un diccionario, donde podemos
        especificar el tipo de dato a nivel HTML que va a tener cada uno de nuestros campos"""
        fields = '__all__'
        widgets ={
            'email': EmailInput(attrs={'type': 'email'})

        }


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        """Vamos a utilizar todos los atributos, indicamos __all__
        Tipo de campo de formulario usamos el atributo widgets que es un diccionario, donde podemos
        especificar el tipo de dato a nivel HTML que va a tener cada uno de nuestros campos"""
        fields = '__all__'
        widgets ={
            'no_calle': TextInput(attrs={'type': 'number'})

        }