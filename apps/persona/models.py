from django.db import models
# from apps.administracion.models import 

# Create your models here.


class TipoCalle(models.Model):
	nombre = models.CharField(max_length=25)
	codigo = models.CharField(max_length=10)
	tipo = models.CharField(max_length=10)
	
	def __str__(self):
		return self.nombre

class Ubigeo(models.Model):
	coddep = models.CharField(max_length=2)
	codprov = models.CharField(max_length=2)
	coddist = models.CharField(max_length=2)
	nombreubigeo = models.CharField(max_length=50)
	nombrecapital = models.CharField(max_length=50)

	def __str__(self):
		return self.nombreubigeo

class EstadoCivil(models.Model):
	nombre = models.CharField(max_length=45)
	codigo = models.CharField(max_length=45)

	def __str__(self):
		return self.nombre


class Persona(models.Model):
	MASCULINO = 'M'
	FEMENINO = 'F'
	SEXO = (
		(MASCULINO, 'Masculino'),
		(FEMENINO, 'Femenino'),
	)
	nombre = models.CharField(max_length=45)
	paterno = models.CharField(max_length=45)
	materno = models.CharField(max_length=45)
	dni = models.CharField(max_length=8)
	sexo = models.CharField(max_length=1,choices=SEXO,default=MASCULINO,)
	correos = models.EmailField(max_length=45, blank=True, null=True)
	clave = models.CharField(max_length=45, blank=True, null=True)
	fnacimiento = models.DateField(blank=True, null=True)
	estadocivil = models.ForeignKey(EstadoCivil)
	tipocalle = models.ForeignKey(TipoCalle)
	direccion = models.CharField(max_length=600, blank=True, null=True)
	ubigeonacimiento = models.ForeignKey(Ubigeo, related_name='nacimiento')
	ubigeoresidencia = models.ForeignKey(Ubigeo,related_name='residencia')
	
	def __str__(self):
		return self.nombre
