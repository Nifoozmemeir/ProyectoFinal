from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from AppBase.models import *

# Create your views here.
def login_usuarios(request):
    if request.method == 'POST':
        mi_formulario = AuthenticationFormEspanol(request, data=request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            username = data["username"]
            email = data["email"]
            password = data["password"]
            user = authenticate(username=username, email=email, password=password)
            if user:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=user)
                    return render(request, 'inicio.html', {"mensaje": f"Bienvenido {username}", "url": avatar.imagen.url})
                except Avatar.DoesNotExist:
                    return render(request, 'inicio.html', {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, 'inicio.html', {"mensaje": "Error: datos incorrectos"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = AuthenticationFormEspanol()
        return render(request, "login.html", {"mi_formulario": mi_formulario})
