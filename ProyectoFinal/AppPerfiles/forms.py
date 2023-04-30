from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from AppBase.models import *

class UsuarioEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    descripcion = forms.CharField(label="Descripción", widget=forms.TextInput)
    enlace_pagina = forms.URLField(label="Enlace a página web", widget=forms.URLInput)
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'password1', 'password2', 'descripcion', 'enlace_pagina')
    def clean_password2(self):
        print(self.cleaned_data)
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
    
class Avatar_Formulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields = ['imagen']