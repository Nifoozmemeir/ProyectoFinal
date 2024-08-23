from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_usuarios, name="Login"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name="Logout"),
]