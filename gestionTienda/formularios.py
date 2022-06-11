from django import forms
from gestionTienda.models import *

# DIRECTORIO SUGERENCIA

sugerencia = Sugerencia.objects.all()
choices_sugerencias = []
for item in sugerencia:
    choices_sugerencias.append((item.id, item.nombre, item.descripcion))
choices_sugerencias = tuple(choices_sugerencias)

class SugerenciaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=150)


# DIRECTORIO FORMULARIO

directorio = Directorio.objects.all()
choices_directorio = []
for item in directorio:
    choices_directorio.append((item.id, item.nombre, item.direccion, item.correo, item.telefono, item.referencia))
choices_directorio = tuple(choices_directorio)

class DirectorioFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=200)
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=10)
    referencia = forms.CharField(max_length=100)



