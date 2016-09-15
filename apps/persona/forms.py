from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple

from .models import EstadoCivil

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