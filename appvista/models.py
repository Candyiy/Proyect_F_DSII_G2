from django.db import models

# Create your models here.

class Educacion(models.Model):
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    año_finalizacion = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.institucion}"
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"