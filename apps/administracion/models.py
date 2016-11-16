from django.db import models
from apps.persona.models import *
from django.contrib.auth.models import User
# Create your models here.

class Menu(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=500)
	ruta = models.CharField(max_length=350)
	orden = models.IntegerField()
	estado = models.BooleanField(max_length=50)
	menupadre = models.ForeignKey('self', blank=True, null=True , on_delete=models.PROTECT )

	def __str__(self):
		return self.nombre

class Rol(models.Model):
	nombre = models.CharField(max_length=45)
	controltotal = models.BooleanField(default=True)
	menus = models.ManyToManyField(Menu)


	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	persona = models.ForeignKey(Persona)
	roles = models.ManyToManyField(Rol, through='Perfil', through_fields=('usuario', 'rol'),)

	def __str__(self):
		return self.persona.nombre


class Perfil(models.Model):
	usuario = models.ForeignKey(Usuario)
	rol = models.ForeignKey(Rol)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.usuario.user.username+' '+self.rol.nombre

class UbigeoPerfil(models.Model):
	perfil = models.ForeignKey(Perfil)
	ubigeo = models.ForeignKey(Ubigeo)



class Organizacion(models.Model):
	nombre = models.CharField(max_length=255)
	ruc = models.CharField(max_length=11)
	telefono = models.CharField(max_length=15, blank=True, null=True)
	email = models.EmailField(max_length=100, blank=True, null=True)
	alcance = models.CharField(max_length=10)
	siglas = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre






