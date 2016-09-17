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
	nombre = forms.CharField(max_length=25, 
				label = "Tipo de calle", 				
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Nombre'
					})
				)

	codigo = forms.CharField(max_length=10, 
				label = "Codigo del tipo de calle",
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Código'
					})			
				)
	tipo = forms.CharField(max_length=10, 
				label = "Tipo",
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
						'placeholder': 'Tipo'
					})
				)

	class Meta:
		model = TipoCalle
		fields = ('nombre', 'codigo', 'tipo',)



class PersonaForm(forms.ModelForm):
	nombre = forms.CharField(max_length=25, 				
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
				)

	paterno = forms.CharField(
				max_length=10, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})			
				)
	materno = forms.CharField(
				max_length=10, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
				)	
	dni = forms.CharField(
				max_length=8, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
				)	
	# sexo = forms.CharField(
	# 			max_length=10, 
	# 			widget=forms.TextInput(
	# 				attrs={
	# 					'class': 'form-control',
	# 				})
	# 			)	

	correos = forms.EmailField(
				required=False,
				max_length=45, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
				)	

	clave = forms.CharField(
				required=False,
				max_length=10, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
			)	

	fnacimiento = forms.DateField(widget=forms.DateInput(attrs={
						'class': 'form-control',

					})
				)


	direccion = forms.CharField(
				required=False,
				max_length=10, 
				widget=forms.TextInput(
					attrs={
						'class': 'form-control',
					})
				)

	class Meta:
		model = Persona
		fields = ('nombre', 'paterno', 'materno',
					'dni', 'sexo','correos', 'clave','fnacimiento', 
					'estadocivil','tipocalle','direccion',
					'ubigeonacimiento','ubigeoresidencia',)

	def __init__(self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields["sexo"].widget.attrs['class'] = 'form-control selectpicker'
		self.fields["sexo"].widget.attrs['data-live-search'] = 'true'		

		self.fields["estadocivil"].widget.attrs['class'] = 'form-control selectpicker'
		self.fields["estadocivil"].widget.attrs['data-live-search'] = 'true'		

		self.fields["tipocalle"].widget.attrs['class'] = 'form-control selectpicker'
		self.fields["tipocalle"].widget.attrs['data-live-search'] = 'true'
