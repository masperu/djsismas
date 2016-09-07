from django import forms
from .models import Menu


class MenuForm(forms.Form):
	YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
	descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
	ruta = forms.CharField(max_length=350,widget=forms.TextInput(attrs={'class': 'form-control', 'rows':'2'}))
	orden = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
	estado = forms.BooleanField(required=True,widget=forms.RadioSelect(choices=YES_OR_NO, attrs={'class': 'form-check-input'}))
	menupadre = forms.ModelChoiceField(required=False,
			queryset= Menu.objects.filter(estado=True), 
			empty_label="(Menu Padre)",
			widget=forms.Select(attrs={'class':'form-control'})
		)

