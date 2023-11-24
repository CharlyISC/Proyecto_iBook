import pytest 
from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Libros, Biblioteca_Personal, Resenas


"""
def test_mi_prueba():
    obj = Libros(name= 'example')
    assert obj.get_absolute_url() =='/'
"""
@pytest.mark.django_db

def test_crear_libro():
        libro = Libros.objects.create(
        Titulo ='El Quijote',
        Autor ='Miguel de Cervantes Saavedra',
        Genero = 'aventura',
        Sinopsis ='Una de las obras más importantes de la literatura universal.',
        Calificacion = 6,
    )
        #Obtiene desde base el dato del id
        libro_db = Libros.objects.get(pk=libro.idLibro)

        #Consulta datos de la tabla
        assert libro_db.Titulo == 'El Quijote'
        assert libro_db.Autor == 'Miguel de Cervantes Saavedra'
        assert libro_db.Genero == 'aventura'
        assert libro_db.Sinopsis == 'Una de las obras más importantes de la literatura universal.'
        assert libro_db.Calificacion == 6

        #Eliminar tabla
        libro_db.delete()

@pytest.mark.django_db

def test_crear_biblioteca():
        #crear usuario de prueba
        usuario = User.objects.create(username = 'prueba_usuario')
        libro = Libros.objects.create(idLibro = 1)

        #crear libro de prueba
        biblioteca = Biblioteca_Personal.objects.create(
                fk_Usuario = usuario,
                fk_Libro = libro,
                estadoLectura = 'Leido',
        )
        #Obtiene desde base el dato del id
        biblioteca_db = Biblioteca_Personal.objects.get(pk=biblioteca.idBiblioteca)

        assert biblioteca_db.fk_Usuario==usuario

        #Eliminar tabla
        biblioteca_db.delete()

@pytest.mark.django_db

def test_resenas():
        #crear usuario de prueba
        usuario = User.objects.create(username = 'prueba_usuario')
        libro = Libros.objects.create(idLibro = 1)

        #Crear resena de prueba

        resena = Resenas.objects.create(
                fk_Usuario = usuario,
                fk_Libro = libro,
                Resena = 'Reseña de prueba',
        )
        #Obtiene desde base el dato del id
        resena_db = Resenas.objects.get(pk=resena.idResenas)

        assert resena_db.fk_Usuario==usuario

        #Eliminar tabla
        resena_db.delete()

        
"""
class test_libros(TestCase):
    def setUp(self):
        #Configuracion inicial para la prueba
        libro = Libros.objects.create(
        Titulo="El Quijote",
        Autor="Miguel de Cervantes Saavedra",
        Genero= "aventura",
        Sinopsis="Una de las obras más importantes de la literatura universal.",
        Calificacion= 6,
        )
"""