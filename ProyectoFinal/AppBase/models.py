from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENERO_OPCIONES = [('aventura', 'Aventura'), ('deportes', 'Deportes'), ('estrategia', 'Estrategia'), ('rpg', 'RPG'), ('moba', 'MOBA'), ('hack and slash', 'Hack And Slash'), 
                   ('mmorpg', 'MMORPG'), ('shooter', 'Shooter'), ('cartas', 'Cartas'), ('city builder', 'City Builder'), ('simulador', 'Simulador'), ('carreras', 'Carreras'), 
                   ('arcade', 'Arcade'), ('plataformas', 'Plataformas'), ('pelea', 'Pelea'), ('terror', 'Terror'), ('sigilo', 'Sigilo'), ('battle royale', 'Battle Royale'), 
                   ('rpg por turnos', 'RPG Por Turnos'), ('roguelike', 'Roguelike'), ('sandbox', 'Sandbox'), ('musica', 'Música'), ('tower defense', 'Tower Defense'), 
                   ('rts', 'RTS'),]
GENERO_OPCIONES = sorted(GENERO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class Videojuego(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_salida = models.DateField()
    genero = models.CharField(max_length=255, choices=GENERO_OPCIONES)
    empresa = models.CharField(max_length=255)
    descripcion = models.TextField()
    valoracion = models.IntegerField(choices=VALORACIONES_OPCIONES, null=False)
    def __str__(self):
        return f"{self.nombre} - {self.fecha_salida} - {self.genero} - {self.empresa} / {self.descripcion} || {self.valoracion} ||"

