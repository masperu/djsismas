from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple

from .models import EstadoCivil,TipoCalle,Persona

class EstadoCivilForm(forms.ModelForm):
	# YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(
			label = "Estado civil",
			max_length=50,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Estado Civil'
				})
		)
	codigo = forms.CharField(
				label = "Codigo",
				max_length=50,
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Codigo'
					})
			)

	class Meta:
		model = EstadoCivil
		fields = ('nombre','codigo',)


class TipoCalleForm(forms.ModelForm):
	nombre = forms.CharField(max_length=25, label = "Tipo de calle")
	codigo = forms.CharField(max_length=10, label = "Codigo del tipo de calle")
	tipo = forms.CharField(max_length=10, label = "Tipo")

	class Meta:
		model = TipoCalle
		fields = ('nombre', 'codigo', 'tipo',)

class PersonaForm(forms.ModelForm):


	class Meta:
		model = Persona
		fields = ('nombre', 'paterno', 'materno',
					'dni', 'sexo','correos', 'clave','fnacimiento', 
					'estadocivil','tipocalle','direccion',
					'ubigeonacimiento','ubigeoresidencia',)
