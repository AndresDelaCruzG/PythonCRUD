from django.http import HttpResponse
from django.shortcuts import render
from gestionTienda.formularios import *

# Create your views here.
def Inicio(request):
    return render(request, "Inicio.html", {})

def Sugerencias(request):
    if request.method == "POST":
        sugerenciaFormulario = SugerenciaFormulario(request.POST)
        if sugerenciaFormulario.is_valid():
            nombre = sugerenciaFormulario.cleaned_data.get("nombre", "")
            descripcion = sugerenciaFormulario.cleaned_data.get("descripcion", "")
            a = Sugerencia(nombre=nombre, descripcion=descripcion)
            a.save()
            return HttpResponse("Gracias se ha guardado la sugerencia")
    else:
        sugerenciaFormulario = SugerenciaFormulario()

    return render(request, "Sugerenicas.html", {"form":sugerenciaFormulario})

def Directorios(request):
    if request.method == "POST":
        directorioFormulario = DirectorioFormulario(request.POST)
        if directorioFormulario.is_valid():
            nombre = directorioFormulario.cleaned_data.get("nombre", "")
            direccion = directorioFormulario.cleaned_data.get("direccion", "")
            correo = directorioFormulario.cleaned_data.get("correo", ""),
            telefono = directorioFormulario.cleaned_data.get("telefono", "")
            referencia = directorioFormulario.cleaned_data.get("referencia", "")
            a = Directorio(nombre=nombre,direccion=direccion,correo=correo,telefono=telefono,referencia=referencia)
            a.save()
            return HttpResponse("Gracias se ha guardado el directorio")
    else:
        directorioFormulario = DirectorioFormulario()

    return render(request, "Directorio.html", {"form":directorioFormulario})

def error_404(request, exception):
    return render(request, 'Errores/Error404.html', {})


