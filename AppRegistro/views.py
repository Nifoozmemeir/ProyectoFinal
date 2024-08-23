from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def registro_usuarios(request):
    if request.method == 'POST':
        mi_formulario = UserCreationFormEspanol(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            username = data["username"]
            email = data["email"]
            password = data["password1"]
            nuevo_usuario = User(username=username, email=email)
            nuevo_usuario.set_password(password)
            nuevo_usuario.save()
            return render(request, 'inicio.html', {"mensaje": f"Usuario {username} creado!"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = UserCreationFormEspanol()
        return render(request, "registro_usuarios.html", {"mi_formulario": mi_formulario})