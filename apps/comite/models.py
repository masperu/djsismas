from django.db import models

# Create your models here.

class TipoCargo(models.Model):
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre


class NivelComite(models.Model):
	nombre = models.CharField(max_length = 50)
	codigo = models.CharField(max_length = 15)
	permiteafiliacion = models.BooleanField(default = False)

	def __str__(self):
		return self.nombre


class NivelCargo(models.Model):
	tipocargo = models.ForeignKey(TipoCargo, on_delete=models.PROTECT)
	nivelcomite = models.ForeignKey(NivelComite, on_delete=models.PROTECT)

	def __str__(self):
		return self.nivelcomite.nombre + ' ' + self.tipocargo.nombre


class Comite(models.Model):
	nombre = models.CharField(max_length = 100)
	actaconformacion = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 200)
	nivelcomite = models.ForeignKey(NivelComite, on_delete=models.PROTECT)
	comitepadre = models.ForeignKey('self', null=True, blank=True)

	def __str__(self):
		return self.nombre
