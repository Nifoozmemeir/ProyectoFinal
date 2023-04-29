from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def inicio(request):  
    return render(request, "inicio.html")

def agregar_videojuego(request):
    if request.method == 'POST':
        mi_formulario = VideojuegosForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            videojuego = Videojuego(nombre=request.POST['nombre'], fecha_salida=request.POST['fecha_salida'], genero=request.POST['genero'], empresa=request.POST['empresa'], descripcion=request.POST['descripcion'], valoracion=request.POST['valoracion'])
            videojuego.save()
            return HttpResponseRedirect('')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = VideojuegosForm()
        return render(request, "agregar_videojuego.html", {"mi_formulario": mi_formulario})
    
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, "ver_videojuegos.html", {"videojuegos": videojuegos})

def eliminar_videojuego(request, id):
    if request.method == 'POST':
        videojuego = Videojuego.objects.get(id=id)
        videojuego.delete()
        videojuegos = Videojuego.objects.all()
        return render(request, "ver_videojuegos.html", {"videojuegos": videojuegos})
    
def editar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = VideojuegosForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            videojuego.nombre = data['nombre']
            videojuego.fecha_salida = data['fecha_salida']
            videojuego.genero = data['genero']
            videojuego.empresa = data['empresa']
            videojuego.descripcion = data['descripcion']
            videojuego.valoracion = data['valoracion']
            videojuego.save()
            return HttpResponseRedirect('')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = VideojuegosForm(initial={
            "nombre": videojuego.nombre,
            "fecha_salida": videojuego.fecha_salida,
            "genero": videojuego.genero,
            "empresa": videojuego.empresa,
            "descripcion": videojuego.descripcion,
            "valoracion": videojuego.valoracion
        })
        return render(request, "editar_videojuegos.html", {"mi_formulario": mi_formulario, "id": videojuego.id})

