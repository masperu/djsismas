from django.db import models
from apps.comite.models import Comite

# Create your models here.

class Ficha(models.Model):
	comite = models.ForeignKey(Comite, on_delete=models.PROTECT)
	estado = models.CharField(max_length = 20)
	fechaafiliacion = models.DateField(auto_now_add=True)
	alcance = mmodels.CharField(max_length = 10)
	paterno = mmodels.CharField(max_length = 75)
	materno = mmodels.CharField(max_length = 75)
	nombres = mmodels.CharField(max_length = 75)
	estadocivil = mmodels.CharField(max_length = 1)
	sexo = mmodels.CharField(max_length = 1, default="S")
	lugarnacimiento = mmodels.CharField(max_length = 255)
	direccionactual = mmodels.CharField(max_length = 255)
	numeroactual = mmodels.IntegerField()
	sectoractual = mmodels.CharField(max_length = 255)
	telefonoactual = mmodels.CharField(max_length = 20)
	correos = mmodels.TextField(blank = True, null=True)

	def __str__(self):
		return self.nombres + " " + self.paterno + " " + self.materno
				