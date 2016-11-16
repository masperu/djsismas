from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple
from .models import Ficha


class FichaForm(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = ( 'comite', 'persona', 'estado', 'alcance', 'paterno', 'materno', 'nombres', 'estadocivil', 'sexo', 'lugarnacimiento', 'direccionactual', 'numeroactual', 'sectoractual', 'telefonoactual', 'correos',)


