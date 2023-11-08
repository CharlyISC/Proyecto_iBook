# Generated by Django 3.2.4 on 2023-10-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
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
    ]