from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    try: 
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html', {'url': avatar.imagen.url})
    except:
        return render(request, "inicio.html")
    
@login_required   
def agregar_videojuego(request):
    if request.method == 'POST':
        mi_formulario = VideojuegosForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            videojuego = Videojuego(nombre=request.POST['nombre'], fecha_salida=request.POST['fecha_salida'], genero=request.POST['genero'], empresa=request.POST['empresa'], descripcion=request.POST['descripcion'], valoracion=request.POST['valoracion'],)
            videojuego.save()
            return render(request, "inicio.html", {"mensaje": "Muy bien agregaste tu videojuego :D"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = VideojuegosForm()
        return render(request, "agregar_videojuego.html", {"mi_formulario": mi_formulario})

@login_required  
def lista_videojuegos(request):
    orden = request.GET.get('orden', None)
    videojuegos = Videojuego.objects.all()
    if orden == 'lanzamiento':
        videojuegos = videojuegos.order_by('-fecha_salida')
    elif orden == 'valoracion':
        videojuegos = videojuegos.order_by('-valoracion')
    return render(request, "ver_videojuegos.html", {"videojuegos": videojuegos})

@login_required
def eliminar_videojuego(request, id):
    if request.method == 'POST':
        videojuego = Videojuego.objects.get(id=id)
        videojuego.delete()
        videojuego = Videojuego.objects.all()
        return HttpResponseRedirect('/l-videojuegos')

@login_required    
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
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
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

@login_required    
def agregar_resena(request):
    mi_formulario = ResenaForm()
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return HttpResponseRedirect('/l-resenas')
    return render(request, 'agregar_resena.html', {'mi_formulario': mi_formulario})

@login_required
def lista_resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'lista_resenas.html', {'reseñas': resenas})

@login_required
def eliminar_resena(request, id):
    if request.method == 'POST':
        resena = Resena.objects.get(id=id)
        resena.delete()
        resena = Resena.objects.all()
        return HttpResponseRedirect('/l-resenas')

login_required    
def editar_resena(request, id):
    resena = Resena.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            resena.autor = data['autor']
            resena.contenido = data['contenido']
            resena.videojuego = data['videojuego']
            resena.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = ResenaForm(initial={
            "autor": resena.autor,
            "contenido": resena.contenido,
            "videojuego": resena.videojuego,
        })
        return render(request, "editar_resena.html", {"mi_formulario": mi_formulario, "id": resena.id})