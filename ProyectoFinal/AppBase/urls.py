from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-videojuego', agregar_videojuego, name="AgregarVideojuego"),
    path('l-videojuegos', lista_videojuegos, name="ListaVideojuegos"),
    path('el-videojuegos/<int:id>', eliminar_videojuego, name="EliminarVideojuego"),
    path('ed-videojuegos/<int:id>', editar_videojuego, name="EditarVideojuego"),
    path('agregar_resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
]