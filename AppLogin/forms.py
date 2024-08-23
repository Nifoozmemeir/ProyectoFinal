from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AuthenticationFormEspanol(AuthenticationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autofocus': True}))
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']