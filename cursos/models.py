from django.db import models

# Create your models here.

from django.db import models

# Lógica de la Clase Persona (Imagen 1)
class Persona(models.Model):
    dni = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    nro_telef = models.CharField(max_length=20)

# Lógica para la Interfaz de Cursos (Imagen 2)
class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=150)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    
class Persona(models.Model):
    # Atributos de tu imagen
    dni = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10)
    nro_telef = models.CharField(max_length=20)

    # Métodos funcionales de tu imagen
    def hablar(self):
        return f"{self.nombre} está hablando."

    def trabajar(self):
        return f"{self.nombre} está trabajando."