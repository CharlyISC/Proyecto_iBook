from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Libros(models.Model):
    idLibro = models.AutoField(primary_key=True,db_column='idLibro')
    Titulo = models.CharField(max_length=100,default='Titulo',db_column='Titulo')
    Autor = models.CharField(max_length=60,default= 'Autor_Random',db_column='Autor')
    Genero = models.CharField(max_length=60,default= 'Genero_Random',db_column='Genero')
    Sinopsis = models.CharField(max_length=200,default= 'Sinopsis_Random',db_column='Sinopsis')
    Calificacion = models.IntegerField(default='0',db_column='Calificacion')
    class Meta:
        db_table= 'Libros'

class Biblioteca_Personal(models.Model):
    idBiblioteca = models.AutoField(primary_key=True, db_column='idBiblioteca')
    fk_Usuario = models.ForeignKey(User, on_delete=models.CASCADE,db_column='fk_Usuario')
    fk_Libro = models.ForeignKey(Libros, on_delete=models.CASCADE, db_column='fk_Libro')
    estadoLectura = models.CharField(max_length=20, default='No leido',db_column='estadoLectura')
    class Meta:
        db_table= 'Biblioteca_Personal'

class Resenas(models.Model):
    idResenas = models.AutoField(primary_key=True, db_column='idResenas') 
    fk_Usuario = models.ForeignKey(User, on_delete=models.CASCADE,db_column='fk_Usuario')
    fk_Libro = models.ForeignKey(Libros, on_delete=models.CASCADE, db_column='fk_Libro')
    Resena = models.CharField(max_length=200, default='Resena_Random',db_column='Resena')
    class Meta:
        db_table= 'Resenas'

class Favoritos(models.Model):
    idFavorito = models.AutoField(primary_key=True, db_column='idFavorito')
    fk_Usuario = models.ForeignKey(User, on_delete=models.CASCADE,db_column='fk_Usuario')
    fk_Libro = models.ForeignKey(Libros, on_delete=models.CASCADE, db_column='fk_Libro')
    class Meta:
        db_table= 'Favoritos'



class Encuesta(models.Model):
    pregunta1 = models.TextField(db_column='Facilidad de uso del sistema')    
    pregunta2 = models.TextField(db_column='Utilidad del sistema')    
    pregunta4 = models.TextField(db_column='Frecuencia en problemas tecnicos')    
    pregunta5 = models.TextField(db_column='Buen soporte al cliente')    
    pregunta6 = models.TextField(db_column='Satisfaccion con actualizaciones')    
    pregunta7 = models.TextField(db_column='Recomendacion del sistema')    
