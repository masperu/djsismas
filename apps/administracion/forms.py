from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple,SelectMultiple

from .models import Menu, Rol, Organizacion, Usuario
from django.contrib.auth.forms import UserCreationForm, User


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


class OrganizacionForm(forms.ModelForm):
	# YES_OR_NO = ((True, 'Yes'),(False, 'No'))
	nombre = forms.CharField(
			label = "Organizacion",
			max_length=255,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Nombre'
				})
		)

	ruc = forms.CharField( 
			max_length=11,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control', 
					'rows':'2',
					'placeholder': 'Ingrese su Ruc'
				})
		)

	telefono = forms.CharField(
			max_length=15,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Ingrese el telefono'
				})
		)

	email = forms.CharField(
			max_length=100,
			widget=forms.EmailInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Ingrese el correo'
				})
				
		)

	alcance = forms.CharField(
			max_length=10,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Ingrese el alcance'
				})
		)

	siglas = forms.CharField(
			max_length=10,
			widget=forms.TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'Ingrese las siglas'
				})
		)

	class Meta:
		model = Organizacion
		fields = ('nombre','ruc', 'telefono','email','alcance','siglas',)

		
class UserForm(forms.ModelForm):
	error_messages = {
			'password_mismatch': ("The two password fields didn't match."),
		}
	password = forms.CharField(label=("Password"),
				widget=forms.PasswordInput(attrs={'class': 'form-control',}))
	password2 = forms.CharField(label=("Password confirmation"),
				widget=forms.PasswordInput(attrs={'class': 'form-control',}),
				help_text=("Enter the same password as above, for verification."))
	class Meta:
		model = User
		fields = ('username','password',"password2")

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields["username"].widget.attrs['class'] = 'form-control'
		
	def clean_password2(self):
		password1 = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ('persona',)

	def __init__(self, *args, **kwargs):
		super(UsuarioForm, self).__init__(*args, **kwargs)
		self.fields["persona"].widget.attrs['class'] = 'form-control selectpicker'
		self.fields["persona"].widget.attrs['data-live-search'] = 'true'		


class PerfilForm(forms.Form):
	roles = ModelMultipleChoiceField(
				queryset=Rol.objects.all(),
				widget=forms.CheckboxSelectMultiple(
					attrs={
						'class': 'custom-control-input',
					}
				),
			)
	class Meta:
		model = Usuario
		fields = ('roles',)

	def __init__(self, *args, **kwargs):
		super(PerfilForm, self).__init__(*args, **kwargs)