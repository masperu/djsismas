from django import forms
from .models import NivelComite


class NivelComiteForm(forms.ModelForm):
	YES_OR_NO = ((True, 'Si'),(False, 'No'))
	nombre = forms.CharField(
				max_length = 50,
				widget = forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Nombre',
						'title':'Ingrese el nombre'
					}
				),
				help_text='Use puns liberally',
			)
	codigo = forms.CharField(
				max_length = 15,
				widget = forms.TextInput(
					attrs = {
						'class': 'form-control',
						'placeholder': 'Código',
						'title':'Ingrese el codigo'
					}
				),
				# label = 'Mi label',
				help_text='Use puns liberally liberally liberally',
			)
	permiteafiliacion = forms.BooleanField(
				# widget = forms.RadioSelect(
				# 	#choices=YES_OR_NO,
				# 	# attrs = {
				# 	# 	'class': 'form-radios',
				# 	# }
				# ),
				label = 'Permite afiliación',
				# initial = False,
			)
		
	class Meta:
		model = NivelComite
		fields = ('nombre','codigo','permiteafiliacion',)