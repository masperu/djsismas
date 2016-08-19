from django.db import models

# Create your models here.

class TipoCargo(models.Model):
	nombre = mmodels.CharField(max_length = 50)

	def __str__(self):
		return self.nombre


class NivelComite(models.Model):
	nombre = mmodels.CharField(max_length = 50)
	codigo = mmodels.CharField(max_length = 15)
	permiteafiliacion = mmodels.BooleanField(default = False)

	def __str__(self):
		return self.nombre


class NivelCargo(models.Model):
	tipocargo = model.ForeignKey(TipoCargo, on_delete=models.PROTECT) #on_delete es para no borrar en cascada
	nivelcomite = model.ForeignKey(NivelComite, on_delete=models.PROTECT)

	def __str__(self):
		return self.nivelcomite.nombre + ' ' + self.tipocargo.nombre


class Comite(models.Model):
	nombre = mmodels.CharField(max_length = 100)
	actaconformacion = mmodels.CharField(max_length = 100)
	direccion = mmodels.CharField(max_length = 200)
	nivelcomite = model.ForeignKey(NivelComite, on_delete=models.PROTECT)
	comitepadre = model.ForeignKey('self', null=True, blank=True)

	def __str__(self):
		return self.nombre
