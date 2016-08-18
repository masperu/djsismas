from django.db import models

# Create your models here.
class Organizacion(models.Model):
    nombre = models.CharField(max_length=255)
    ruc = models.CharField(max_length=11)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    alcance = models.CharField(max_length=10)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class TipoCalle(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
