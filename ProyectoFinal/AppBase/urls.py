from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-videojuego', agregar_videojuego, name="AgregarVideojuego"),
    path('l-videojuegos', lista_videojuegos, name="ListaVideojuegos"),
    path('el-videojuegos/<int:id>', eliminar_videojuego, name="EliminarVideojuego"),
    path('ed-videojuegos/<int:id>', editar_videojuego, name="EditarVideojuego"),
]