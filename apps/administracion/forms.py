from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
	# YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(
		label = "Nombres",
		max_length=50,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control'
			})
		)

	descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'2'}))
	ruta = forms.CharField(max_length=350,widget=forms.TextInput(attrs={'class': 'form-control'}))
	orden = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
	menupadre = forms.ModelChoiceField(required=False,label = "Menu Padre",
			queryset= Menu.objects.filter(estado=True), 
			empty_label="(Menu Padre)",
			widget=forms.Select(attrs={'class':'form-control selectpicker'})
		)
	class Meta:
		model = Menu
		fields = ('nombre','descripcion','ruta', 'orden','estado','menupadre',)

