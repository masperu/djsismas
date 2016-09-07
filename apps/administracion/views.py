from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def VistaInicio(request):
	if(request.session.get("idusuario", False)):
		return render( request, 'administracion/home.html')
	else:
		return redirect('/login/')

def Login(request):
	if(request.session.get("idusuario", False)):
		return render( request, 'administracion/home.html')
	else:
		p = request.POST
		if request.method == 'POST':
			user = authenticate(username= p['usuario'], password=p['password'])
			if user is not None:
				request.session['idusuario'] = user.id
				return redirect('/')
			else:
				return render( request, 'administracion/login.html', {'msj' : "Usuario o contraseña son incorrectas"})
		else:
			return render( request, 'administracion/login.html')
	
def Logout(request):
	try:
		del request.session['idusuario']
	except KeyError:
		pass
	logout(request)
	return redirect('/login/')

def ListaMenus(request):
	if(request.session.get("idusuario", False)):
		menu = Menu.objects.all()
		return render(request, 'administracion/menu_grilla.html',{'menu': menu})
	else:
		return redirect('/login/')

def MenuAgregar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = MenuForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				descripcion = form.cleaned_data['descripcion']
				estado = form.cleaned_data['estado']
				menupadre = form.cleaned_data['menupadre']
				nombre = form.cleaned_data['nombre']
				orden = form.cleaned_data['orden']
				ruta = form.cleaned_data['ruta']
			
				menu = Menu(
						nombre = nombre, 
						descripcion= descripcion, 
						ruta = ruta, 
						orden = orden, 
						estado = estado, 
						menupadre_id = menupadre, 
					)
				menu.save()

				return HttpResponseRedirect('/menu/')

			# if a GET (or any other method) we'll create a blank form
		else:
			form = MenuForm()
			return render(request, 'administracion/menu_form.html',{'form':form })
	
	else:
		return redirect('/login/')