from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple

from .models import Menu, Rol

class MenuForm(forms.ModelForm):
	# YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(
			label = "Nombre del menu",
			max_length=50,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Nombre'
				})
		)

	descripcion = forms.CharField(
			required=False, 
			widget=forms.Textarea(
				attrs={
					'class': 'form-control', 
					'rows':'2',
					'placeholder': 'Descripcion'
				})
		)

	ruta = forms.CharField(
			max_length=350,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'URL'
				})
		)
	orden = forms.IntegerField(
			widget=forms.TextInput(
				attrs={
					'class': 'form-control', 
					'type':'number',
					'placeholder': 'Orden'
				})
		)

	choices=((False, 'Inactivo'), (True, 'Actvio'))

	estado = forms.BooleanField(
			initial=True,
			label='Activo', 
			required=False,
			# widget=forms.RadioSelect(choices=choices)
		)

	
	# menupadre = forms.ModelChoiceField(
	# 		required=False,
	# 		label = "Menu Padre",
	# 		queryset= Menu.objects.filter(estado=True), 
	# 		empty_label="(Menu Padre)",
	# 		widget=forms.Select(
	# 			attrs={
	# 				'class':'form-control selectpicker'
	# 			})
	# 	)

	class Meta:
		model = Menu
		fields = ('nombre','descripcion','ruta', 'orden','estado','menupadre',)

class RolForm(forms.ModelForm):
	# YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(
			label = "Nombre del rol",
			max_length=50,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Nombre'
				})
		)

	controltotal = forms.BooleanField(
			initial=True,
			label='Control total', 
			required=False,
			# widget=forms.RadioSelect(choices=choices)
		)

	class Meta:
		model = Rol
		fields = ('nombre','controltotal',)

class RolAccesoForm(forms.ModelForm):
	menus = ModelMultipleChoiceField(
				queryset=Menu.objects.filter(estado=True),
				widget=forms.CheckboxSelectMultiple(
					attrs={
						'class': 'custom-control-input',
					}
				),
			)
	class Meta:
		model = Rol
		fields = ('menus',)
