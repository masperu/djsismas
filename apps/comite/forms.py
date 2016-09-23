from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple
from .models import NivelComite, TipoCargo, Comite, NivelCargo


class NivelComiteForm(forms.ModelForm):
	YES_OR_NO = ((True, 'Si'),(False, 'No'))
	nombre = forms.CharField(
				required = True,
				max_length = 50,
				widget = forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Nombre',
						'title':'Ingrese el nombre',
					}
				),
				#help_text='Use puns liberally',
			)
	codigo = forms.CharField(
				required = True,
				max_length = 15,
				widget = forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Código',
						'title':'Ingrese el codigo'
					}
				),
			)
	permiteafiliacion = forms.BooleanField(
				label = 'Permite afiliación',
				required = False,
			)
		
	class Meta:
		model = NivelComite
		fields = ('nombre','codigo','permiteafiliacion',)



class TipoCargoForm(forms.ModelForm):
	nombre = forms.CharField(
				max_length = 50,
				widget = forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Nombre',
						'title':'Ingrese el nombre',
					}
				),
			)
		
	class Meta:
		model = TipoCargo
		fields = ('nombre',)


class ComiteForm(forms.ModelForm):
	
	class Meta:
		model = Comite
		fields = ('nombre', 'actaconformacion', 'direccion', 'nivelcomite', 'comitepadre', 'ubigeo' )


class NivelCargoTipoForm(forms.ModelForm):
	tipocargos = ModelMultipleChoiceField(
				queryset=TipoCargo.objects.all(),
				widget=forms.CheckboxSelectMultiple(
					attrs={
						'class': 'custom-control-input',
					}
				),
			)
	
	class Meta:
		model = NivelComite
		fields = ('tipocargos',)



class NivelCargoForm(forms.ModelForm):
	class Meta:
		model = NivelCargo
		fields = ('tipocargo', 'nivelcomite', )



