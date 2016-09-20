from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models.deletion import ProtectedError

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
		menu = Menu.objects.all().order_by('-orden')
		paginator = Paginator(menu, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			menu = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			menu = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			menu = paginator.page(paginator.num_pages)
		return render(request, 'administracion/menu_grilla.html',{'menu': menu})
	else:
		return redirect('/login/')

def MenuAgregar(request):
	if(request.session.get("idusuario", False)):
		menupadre = None
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = MenuForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				menu = form.save(commit=False)
				menu.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'administracion/menu_form.html',{'form':form ,'url':'/menu/agregar/', 'menupadre': menupadre})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = MenuForm()
			return render(request, 'administracion/menu_form.html',{'form':form, 'url':'/menu/agregar/' ,'menupadre': menupadre})
	
	else:
		return redirect('/login/')

def MenuEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idmenu = request.POST['idmenu']
			try:
				menu = Menu.objects.get(id = idmenu)
				menu.delete()
				response_data = {"success": "Menu Eliminado Correctamente"}
				if menu:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
					return HttpResponseRedirect('/menu/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar este menu porque tiene hijos"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')

def MenuAjax(request):
	if(request.session.get("idusuario", False)):
		menu = Menu.objects.filter(nombre__icontains = "" + request.GET.get('query') + "", estado= True)[:10]
		total = menu.count()
		return render(
			request,
			'administracion/menu.json',
			{
				'menu': menu,
				'total':total
			},
			content_type="application/json",
		)
		#return render(request, 'comite/comite.html',{'comite': comite})
	else:
		return redirect('/login/')


def MenuEditar(request):
	if(request.session.get("idusuario", False)):
		idmenu = request.GET.get('idmenu')
		instance = get_object_or_404(Menu, id=idmenu)
		form = MenuForm(request.POST or None, instance=instance)

		try:
			menupadre = Menu.objects.get(id=instance.menupadre.id)
		except Exception as e:
			menupadre = None
			
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'administracion/menu_form.html',
				{
					'form': form, 'url':'/menu/editar/?idmenu='+idmenu, 'menupadre': menupadre
				}
			)
	else:
		return redirect('/login/')

def MenuListar(request):
	menu = Menu.objects.filter(rol__id= 6)
	menus = []
	for menu in menu:
		menus.append({"nombre":menu.nombre, "ruta":menu.ruta, "menupadre":menu.menupadre.nombre if menu.menupadre else None })

	return render(request, 'administracion/perfil_grilla.html',{'menu':menus})


def ListaRol(request):
	if(request.session.get("idusuario", False)):
		rol = Rol.objects.all().order_by('-id')
		paginator = Paginator(rol, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			rol = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			rol = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			rol = paginator.page(paginator.num_pages)
		return render(request, 'administracion/rol_grilla.html',{'rol': rol})
	else:
		return redirect('/login/')

def RolAgregar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = RolForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				rol = form.save(commit=False)
				rol.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'administracion/rol_form.html',{'form':form ,'url':'/rol/agregar/'})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = RolForm()
			return render(request, 'administracion/rol_form.html',{'form':form, 'url':'/rol/agregar/'})
	
	else:
		return redirect('/login/')

def RolEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idrol = request.POST['idrol']
			try:
				rol = Rol.objects.get(id = idrol)
				rol.delete()
				response_data = {"success": "Rol Eliminado Correctamente"}
				if rol:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
					return HttpResponseRedirect('/rol/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar este rol porque tiene hijos"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')


def RolEditar(request):
	if(request.session.get("idusuario", False)):
		idrol = request.GET.get('idrol')
		instance = get_object_or_404(Rol, id=idrol)
		form = RolForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'administracion/rol_form.html',
				{
					'form': form, 'url':'/rol/editar/?idrol='+idrol
				}
			)
	else:
		return redirect('/login/')

def RolMenuAccesoEditar(request):
	if(request.session.get("idusuario", False)):
		idrol = request.GET.get('idrol')
		instance = get_object_or_404(Rol, id=idrol)
		form = RolAccesoForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'administracion/rol_menu_form.html',
				{
					'form': form, 'url':'/rol/accesomenu/?idrol='+idrol
				}
			)
	else:
		return redirect('/login/')

def ListaAccesos(request):

	if(request.session.get("idusuario", False)):
		print(request.POST['idrol']);
		idrol = request.POST['idrol']
		acceso = Menu.objects.filter(rol__id = idrol )
		paginator = Paginator(acceso, 100) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			acceso = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			acceso = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			acceso = paginator.page(paginator.num_pages)
		return render(request, 'administracion/acceso_grilla.html',{'acceso': acceso})
	else:
		return redirect('/login/')

def ListaPerfil(request):
	if(request.session.get("idusuario", False)):
		perfil = Perfil.objects.all()
		return render(request, 'administracion/perfil_grilla.html',{'perfil': perfil})
	else:
		return redirect('/login/')	



def ListaOrganizacion(request):
	if(request.session.get("idusuario", False)):
		organizacion = Organizacion.objects.all().order_by('-id')
		paginator = Paginator(organizacion, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			organizacion = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			organizacion = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			organizacion = paginator.page(paginator.num_pages)
		return render(request, 'administracion/organizacion_grilla.html',{'organizacion': organizacion})
	else:
		return redirect('/login/')

def OrganizacionAgregar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = OrganizacionForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				organizacion = form.save(commit=False)
				organizacion.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'administracion/organizacion_form.html',{'form':form ,'url':'/organizacion/agregar/'})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = OrganizacionForm()
			return render(request, 'administracion/organizacion_form.html',{'form':form, 'url':'/organizacion/agregar/'})
	
	else:
		return redirect('/login/')

def OrganizacionEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idorganizacion = request.POST['idorganizacion']
			try:
				organizacion = Organizacion.objects.get(id = idorganizacion)
				organizacion.delete()
				response_data = {"success": "Organizacion Eliminado Correctamente"}
				if organizacion:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
					return HttpResponseRedirect('/organizacion/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar esta organizacion porque datos relacionado"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')


def OrganizacionEditar(request):
	if(request.session.get("idusuario", False)):
		idorganizacion = request.GET.get('idorganizacion')
		instance = get_object_or_404(Organizacion, id=idorganizacion)
		form = OrganizacionForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'administracion/organizacion_form.html',
				{
					'form': form, 'url':'/organizacion/editar/?idorganizacion='+idorganizacion
				}
			)
	else:
		return redirect('/login/')