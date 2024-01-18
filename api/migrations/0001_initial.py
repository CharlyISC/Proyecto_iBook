# Generated by Django 3.2.4 on 2024-01-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta1', models.TextField(db_column='Facilidad de uso del sistema')),
                ('pregunta2', models.TextField(db_column='Utilidad del sistema')),
                ('pregunta4', models.TextField(db_column='Frecuencia en problemas tecnicos')),
                ('pregunta5', models.TextField(db_column='Buen soporte al cliente')),
                ('pregunta6', models.TextField(db_column='Satisfaccion con actualizaciones')),
                ('pregunta7', models.TextField(db_column='Recomendacion del sistema')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(db_column='idEvento', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='evento_trampolin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Inflable',
            fields=[
                ('idInfla', models.AutoField(db_column='idInflable', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(db_column='Nombre', default='Nombre', max_length=100)),
                ('Ancho', models.IntegerField(db_column='Ancho', default='0')),
                ('Largo', models.IntegerField(db_column='Largo', default='0')),
                ('Alto', models.IntegerField(db_column='Alto', default='0')),
            ],
            options={
                'db_table': 'Inflable',
            },
        ),
        migrations.CreateModel(
            name='Toro',
            fields=[
                ('idToro', models.AutoField(db_column='idToro', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(db_column='Nombre', default='Nombre', max_length=100)),
                ('Ancho', models.IntegerField(db_column='Ancho', default='0')),
                ('Largo', models.IntegerField(db_column='Largo', default='0')),
                ('Alto', models.IntegerField(db_column='Alto', default='0')),
            ],
            options={
                'db_table': 'Toro',
            },
        ),
        migrations.CreateModel(
            name='Trampolin',
            fields=[
                ('idTramp', models.AutoField(db_column='idTramp', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(db_column='Nombre', default='Nombre', max_length=100)),
                ('Ancho', models.IntegerField(db_column='Ancho', default='0')),
                ('Largo', models.IntegerField(db_column='Largo', default='0')),
                ('Alto', models.IntegerField(db_column='Alto', default='0')),
                ('Resorte', models.IntegerField(db_column='Resorte', default='0')),
            ],
            options={
                'db_table': 'Trampolin',
            },
        ),
    ]
