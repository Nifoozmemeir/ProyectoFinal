from django import forms
from .models import *

GENERO_OPCIONES = [('aventura', 'Aventura'), ('deportes', 'Deportes'), ('estrategia', 'Estrategia'), ('rpg', 'RPG'), ('moba', 'MOBA'), ('hack and slash', 'Hack And Slash'), 
                   ('mmorpg', 'MMORPG'), ('shooter', 'Shooter'), ('cartas', 'Cartas'), ('city builder', 'City Builder'), ('simulador', 'Simulador'), ('carreras', 'Carreras'), 
                   ('arcade', 'Arcade'), ('plataformas', 'Plataformas'), ('pelea', 'Pelea'), ('terror', 'Terror'), ('sigilo', 'Sigilo'), ('battle royale', 'Battle Royale'), 
                   ('rpg por turnos', 'RPG Por Turnos'), ('roguelike', 'Roguelike'), ('sandbox', 'Sandbox'), ('musica', 'Música'), ('tower defense', 'Tower Defense'), 
                   ('rts', 'RTS'),]
GENERO_OPCIONES = sorted(GENERO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class VideojuegosForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    fecha_salida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.CharField(max_length=255, widget=forms.Select(choices=GENERO_OPCIONES))
    empresa = forms.CharField(max_length=255)
    descripcion = forms.CharField(max_length=255)
    valoracion = forms.IntegerField(required=True, widget=forms.Select(choices=VALORACIONES_OPCIONES))

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ('__all__')

class BuscarNombre(forms.Form):
    nombre = forms.CharField(label='Nombre del videojuego', max_length=255)

class BuscarGenero(forms.Form):
    genero = forms.CharField(label='Nombre del género', max_length=255, widget=forms.Select(choices=GENERO_OPCIONES))

class BuscarEmpresa(forms.Form):
    empresa = forms.CharField(label='Nombre de la empresa', max_length=255)

class BuscarValoracion(forms.Form):
    valoracion = forms.IntegerField(label='Valoracion', widget=forms.Select(choices=VALORACIONES_OPCIONES))

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']