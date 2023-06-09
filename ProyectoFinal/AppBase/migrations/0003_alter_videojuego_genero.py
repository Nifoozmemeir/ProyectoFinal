# Generated by Django 4.2 on 2023-04-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBase', '0002_remove_videojuego_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='genero',
            field=models.CharField(choices=[('accion', 'Acción'), ('arcade', 'Arcade'), ('aventura', 'Aventura'), ('battle_royale', 'Battle Royale'), ('carreras', 'Carreras'), ('cartas', 'Cartas'), ('city_builder', 'City Builder'), ('deportes', 'Deportes'), ('estrategia', 'Estrategia'), ('hack_and_slash', 'Hack And Slash'), ('mmorpg', 'MMORPG'), ('moba', 'MOBA'), ('musica', 'Música'), ('pelea', 'Pelea'), ('plataformas', 'Plataformas'), ('rpg', 'RPG'), ('rpg_por_turnos', 'RPG Por Turnos'), ('rts', 'RTS'), ('roguelike', 'Roguelike'), ('sandbox', 'Sandbox'), ('shooter', 'Shooter'), ('sigilo', 'Sigilo'), ('simulador', 'Simulador'), ('terror', 'Terror'), ('tower_defense', 'Tower Defense')], max_length=255),
        ),
    ]
