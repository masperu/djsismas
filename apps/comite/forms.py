from django import forms
from .models import NivelComite, TipoCargo


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



