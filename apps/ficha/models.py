from django.db import models
from apps.comite.models import Comite

# Create your models here.

class Ficha(models.Model):
	comite = models.ForeignKey(Comite, on_delete=models.PROTECT)
	estado = models.CharField(max_length = 20)
	fechaafiliacion = models.DateField(auto_now_add=True)
	alcance = models.CharField(max_length = 10)
	paterno = models.CharField(max_length = 75)
	materno = models.CharField(max_length = 75)
	nombres = models.CharField(max_length = 75)
	estadocivil = models.CharField(max_length = 1)
	sexo = models.CharField(max_length = 1, default="S")
	lugarnacimiento = models.CharField(max_length = 255)
	direccionactual = models.CharField(max_length = 255)
	numeroactual = models.IntegerField()
	sectoractual = models.CharField(max_length = 255)
	telefonoactual = models.CharField(max_length = 20)
	correos = models.TextField(blank = True, null=True)

	def __str__(self):
		return self.nombres + " " + self.paterno + " " + self.materno
				