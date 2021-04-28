from django.db import models

# Create your models here.

class Proyectos(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=500)
    codigo_fuente = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.nombre