from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserCreationFormEspanol(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
