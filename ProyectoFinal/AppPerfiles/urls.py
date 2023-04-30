from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('ag-avatar', agregar_avatar, name='AgregarAvatar'),
    path('avatar', ver_avatar, name="Avatar"),
    path('el-avatar/<int:id>', eliminar_avatar, name="EliminarAvatar"),
    path('ed-perfil', editar_perfil, name="EditarPerfil"),
    path('perfil', ver_perfil, name="Perfil"),
]