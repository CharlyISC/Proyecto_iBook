# Generated by Django 3.2.4 on 2023-10-19 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.IntegerField(db_column='idAlumno', primary_key=True, serialize=False)),
                ('nameAlumno', models.CharField(db_column='nameAlumno', max_length=100)),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('idLibro', models.AutoField(db_column='idLibro', primary_key=True, serialize=False)),
                ('Titulo', models.CharField(db_column='Titulo', default='Titulo', max_length=100)),
                ('Autor', models.CharField(db_column='Autor', default='Autor_Random', max_length=60)),
                ('Genero', models.CharField(db_column='Genero', default='Genero_Random', max_length=60)),
                ('Sinopsis', models.CharField(db_column='Sinopsis', default='Sinopsis_Random', max_length=200)),
                ('Calificacion', models.IntegerField(db_column='Calificacion', default='0')),
            ],
            options={
                'db_table': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Resenas',
            fields=[
                ('idResenas', models.AutoField(db_column='idResenas', primary_key=True, serialize=False)),
                ('Resena', models.CharField(db_column='Resena', default='Resena_Random', max_length=200)),
                ('fk_Libro', models.ForeignKey(db_column='fk_Libro', on_delete=django.db.models.deletion.CASCADE, to='api.libros')),
                ('fk_Usuario', models.ForeignKey(db_column='fk_Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Resenas',
            },
        ),
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('idFavorito', models.AutoField(db_column='idFavorito', primary_key=True, serialize=False)),
                ('fk_Libro', models.ForeignKey(db_column='fk_Libro', on_delete=django.db.models.deletion.CASCADE, to='api.libros')),
                ('fk_Usuario', models.ForeignKey(db_column='fk_Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Favoritos',
            },
        ),
        migrations.CreateModel(
            name='Biblioteca_Personal',
            fields=[
                ('idBiblioteca', models.AutoField(db_column='idBiblioteca', primary_key=True, serialize=False)),
                ('estadoLectura', models.CharField(db_column='estadoLectura', default='No leido', max_length=20)),
                ('fk_Libro', models.ForeignKey(db_column='fk_Libro', on_delete=django.db.models.deletion.CASCADE, to='api.libros')),
                ('fk_Usuario', models.ForeignKey(db_column='fk_Usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Biblioteca_Personal',
            },
        ),
    ]
