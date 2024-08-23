from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from AppBase.models import *
from .forms import *

# Create your views here.
@login_required   
def agregar_avatar(request):
    if request.method == 'POST':
        mi_formulario = Avatar_Formulario(request.POST, request.FILES)
        if mi_formulario.is_valid():
            usuario = User.objects.get(username=request.user)
            avatar = Avatar(user=usuario, imagen=mi_formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'inicio.html', {"mensaje": "Avatar agregado ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = Avatar_Formulario()
        return render(request, "agregar_avatar.html", {"mi_formulario": mi_formulario})
    
@login_required
def eliminar_avatar(request, id):
    if request.method == 'POST':
        avatar = Avatar.objects.get(id=id)
        avatar.delete()
        avatar = Avatar.objects.all()
        return HttpResponseRedirect('/avatar')
    
@login_required
def ver_avatar(request):
    usuario = request.user
    avatares = Avatar.objects.filter(user=usuario)
    return render(request, "ver_avatar.html", {"avatares": avatares})


@login_required    
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UsuarioEditForm(request.POST, instance=request.user)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data["password1"])
            usuario.descripcion = data["descripcion"]
            usuario.enlace_pagina = data["enlace_pagina"]
            usuario.save()
            return render(request, "inicio.html", {"mensaje": "Datos actualizados ;)"})
        else:
            return render(request, "inicio.html", {"mi_formulario": mi_formulario})
    else:
        mi_formulario = UsuarioEditForm(instance=request.user)
        return render(request, "editar_perfil.html", {"mi_formulario": mi_formulario})

@login_required
def ver_perfil(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, 'ver_perfil.html', context)