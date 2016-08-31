from django.db import models
from apps.persona.models import *
# Create your models here.




class Usuario(models.Model):
	usuario = models.CharField(max_length=45)
	clave = models.CharField(max_length=45)
	persona = models.ForeignKey(Persona)

	def __str__(self):
		return self.usuario

class Rol(models.Model):
	nombre = models.CharField(max_length=45)
	controltotal = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Perfil(models.Model):
	usuario = models.ForeignKey(Usuario)
	rol = models.ForeignKey(Rol)

	def __str__(self):
		return self.usuario

class Perfil(models.Model):
	usuario = models.ForeignKey(Usuario)
	rol = models.ForeignKey(Rol)

	def __str__(self):
		return self.usuario+' '+self.rol



class UbigeoPerfil(models.Model):
	perfil = models.ForeignKey(Perfil)
	ubigeo = models.ForeignKey(Ubigeo)

class Menu(models.Model):
	nombre = models.CharField(max_length=50)
	Descripcion = models.CharField(max_length=500)
	ruta = models.CharField(max_length=350)
	orden = models.IntegerField()
	estado = models.BooleanField(max_length=50)
	menupadre = models.ForeignKey('self')

	def __str__(self):
		return self.nombre

class Acceso(models.Model):
	rol = models.ForeignKey(Rol)
	menu = models.ForeignKey(Menu)

	def __str__(self):
		return self.rol + ' ' +self.menu


class Organizacion(models.Model):
	nombre = models.CharField(max_length=255)
	ruc = models.CharField(max_length=11)
	telefono = models.CharField(max_length=15, blank=True, null=True)
	email = models.EmailField(max_length=100, blank=True, null=True)
	alcance = models.CharField(max_length=10)
	siglas = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre





