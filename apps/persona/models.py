from django.db import models
from apps.administracion.models import *

# Create your models here.


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=45)
    paterno = models.CharField(max_length=45)
    materno = models.CharField(max_length=45)
    correos = models.CharField(max_length=45)
    dni = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    fnacimiento = models.CharField(max_length=45)
    estadocivil = models.ForeignKey(EstadoCivil)
    tipocalle = models.ForeignKey(TipoCalle)
    direccion = models.CharField(max_length=600)
    ubigeonacimiento = models.ForeignKey(Ubigeo)
    ubigeoresidencia = models.ForeignKey(Ubigeo)
    
    def __str__(self):
        return self.nombre
