from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-videojuego', agregar_videojuego, name="AgregarVideojuego"),
    path('l-videojuegos', lista_videojuegos, name="ListaVideojuegos"),
    path('el-videojuegos/<int:id>', eliminar_videojuego, name="EliminarVideojuego"),
    path('ed-videojuegos/<int:id>', editar_videojuego, name="EditarVideojuego"),
    path('ag-resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
    path('busq-videojuego', busqueda_videojuegos, name="BusquedaVideojuegos"),
    path('buscar-nombre', buscar_nombre, name="BuscarNombre"),
    path('buscar-genero', buscar_genero, name="BuscarGenero"),
    path('buscar-empresa', buscar_empresa, name="BuscarEmpresa"),
    path('buscar-valoracion', buscar_valoracion, name="BuscarValoracion"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_temas, name='Foro'),
    path('crear-tema', crear_tema, name='CrearTema'),
    path('ed-tema/<int:pk>', editar_tema, name='EditarTema'),
    path('el-tema/<int:pk>', eliminar_tema, name='EliminarTema'),
    path('foro/<int:pk>/', detalle_tema, name='DetalleTema'),
    path('<int:pk>/crear-coment', crear_comentario, name='CrearComentario'),
]