from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import json
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.deletion import ProtectedError
# Create your views here.


def ListaEstadoCivil(request):
	if(request.session.get("idusuario", False)):
		estadocivil = EstadoCivil.objects.all().order_by('-id')
		paginator = Paginator(estadocivil, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			estadocivil = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			estadocivil = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			estadocivil = paginator.page(paginator.num_pages)
		return render(request, 'persona/estadocivil_grilla.html',{'estadocivil': estadocivil})
	else:
		return redirect('/login/')

def EstadoCivilAgregar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = EstadoCivilForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				estadocivil = form.save(commit=False)
				estadocivil.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'persona/estadocivil_form.html',{'form':form ,'url':'/persona.estadocivil/agregar/'})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = EstadoCivilForm()
			return render(request, 'persona/estadocivil_form.html',{'form':form, 'url':'/persona.estadocivil/agregar/'})
	
	else:
		return redirect('/login/')

def EstadoCivilEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idestadocivil = request.POST['idestadocivil']
			try:
				estadocivil = EstadoCivil.objects.get(id = idestadocivil)
				estadocivil.delete()
				response_data = {"success": "Estado Civil Eliminado Correctamente"}
				if estadocivil:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
					return HttpResponseRedirect('/persona.estadocivil/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar este estado civil"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')




def EstadoCivilEditar(request):
	if(request.session.get("idusuario", False)):
		idestadocivil = request.GET.get('idestadocivil')
		instance = get_object_or_404(EstadoCivil, id=idestadocivil)
		form = EstadoCivilForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'persona/estadocivil_form.html',
				{
					'form': form, 'url':'/persona.estadocivil/editar/?idestadocivil='+idestadocivil
				}
			)
	else:
		return redirect('/login/')


def ListaTipoCalle(request):
	if(request.session.get("idusuario", False)):
		tipocalle = TipoCalle.objects.all().order_by('-id')
		paginator = Paginator(tipocalle, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			tipocalle = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			tipocalle = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			tipocalle = paginator.page(paginator.num_pages)
		return render(request, 'persona/tipocalle_grilla.html',{'tipocalle': tipocalle})
	else:
		return redirect('/login/')


def TipoCalleAgregar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = TipoCalleForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				tipocalle = form.save(commit=False)
				tipocalle.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'persona/tipocalle_form.html',{'form':form ,'url':'/persona.tipocalle/agregar/'})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = TipoCalleForm()
			return render(request, 'persona/tipocalle_form.html',{'form':form, 'url':'/persona.tipocalle/agregar/'})
	
	else:
		return redirect('/login/')

def TipoCalleEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idtipocalle = request.POST['idtipocalle']
			try:
				tipocalle = TipoCalle.objects.get(id = idtipocalle)
				tipocalle.delete()
				response_data = {"success": "Tipo Calle Eliminado Correctamente"}
				if tipocalle:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
					return HttpResponseRedirect('/persona.tipocalle/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar este tipo de calle"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')




def TipoCalleEditar(request):
	if(request.session.get("idusuario", False)):
		idtipocalle = request.GET.get('idtipocalle')
		instance = get_object_or_404(TipoCalle, id=idtipocalle)
		form = TipoCalleForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'persona/tipocalle_form.html',
				{
					'form': form, 'url':'/persona.tipocalle/editar/?idtipocalle='+idtipocalle
				}
			)
	else:
		return redirect('/login/')		


def ListaPersona(request):
	if(request.session.get("idusuario", False)):
		persona = Persona.objects.all().order_by('-id')
		paginator = Paginator(persona, 5) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			persona = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			persona = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			persona = paginator.page(paginator.num_pages)
		return render(request, 'persona/persona_grilla.html',{'persona': persona})
	else:
		return redirect('/login/')


def PersonaDNI(request):
	if(request.session.get("idusuario", False)):
		dni = request.POST['dni']
		persona = Persona.objects.filter(dni=dni)
		
		if persona.count() == 0:
			response_data = {"error": "El DNI: " + dni + " no se ha encontrado" }
			return HttpResponse(
					json.dumps(response_data),
					content_type="application/json"
				)
		else:
			response_data = serializers.serialize('json', persona)
			return HttpResponse(
					response_data,
					content_type="application/json"
				)

	else:
		return redirect('/login/')

	# idarea = int(request.GET.get("idarea", "0"))
	# areasdatos = AreaDato.objects.filter(fin=None,area_id=idarea)

	# total = areasdatos.count()
	# return render(
	# 	request,
	# 	'mao/areasdatos/areadato.json',
	# 	{
	# 		'areasdatos': areasdatos,
	# 		'total' : total,
	# 	},
	# 	content_type="application/json",
	# )


def PersonaAgregar(request):
	if(request.session.get("idusuario", False)):
		ubigeonacimiento = None
		ubigeoresidencia = None
		if request.method == 'POST':
			if(request.POST['ubigeoresidencia']):

				ubigeoresidencia = Ubigeo.objects.get(id=request.POST['ubigeoresidencia'])
				Depresidencia = Ubigeo.objects.get(coddep=ubigeoresidencia.coddep,coddist = '00',codprov='00' )
				Provresidencia = Ubigeo.objects.get(coddep=ubigeoresidencia.coddep,coddist = '00',codprov=ubigeoresidencia.codprov)
				ubigeoresidencia = Depresidencia.nombreubigeo+"/"+Provresidencia.nombreubigeo+"/"+ubigeoresidencia.nombreubigeo
			if(request.POST['ubigeonacimiento']):
				ubigeonacimiento = Ubigeo.objects.get(id=request.POST['ubigeonacimiento'])
				Depnacimiento = Ubigeo.objects.get(coddep=ubigeonacimiento.coddep,coddist = '00',codprov='00' )
				Provnacimiento = Ubigeo.objects.get(coddep=ubigeonacimiento.coddep,coddist = '00',codprov=ubigeonacimiento.codprov)
				ubigeonacimiento = Depnacimiento.nombreubigeo+"/"+Provnacimiento.nombreubigeo+"/"+ubigeonacimiento.nombreubigeo

			# create a form instance and populate it with data from the request:
			form = PersonaForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				persona = form.save(commit=False)
				persona.save()
				form.cleaned_data
				# return redirect(ListaMenus)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else:
				return render(request, 'persona/persona_form.html',{'form':form ,'url':'/persona.persona/agregar/', 'ubigeonacimiento':ubigeonacimiento, 'ubigeoresidencia':ubigeoresidencia})

			# if a GET (or any other method) we'll create a blank form
		else:
			form = PersonaForm()
			return render(request, 'persona/persona_form.html',{'form':form, 'url':'/persona.persona/agregar/', 'ubigeonacimiento':ubigeonacimiento, 'ubigeoresidencia':ubigeoresidencia})
	
	else:
		return redirect('/login/')

def PersonaEliminar(request):
	if(request.session.get("idusuario", False)):
		if request.method == 'POST':
			idpersona = request.POST['idpersona']
			try:
				persona = Persona.objects.get(id = idpersona)
				persona.delete()
				response_data = {"success": "Persona Eliminado Correctamente"}
				if persona:
					return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
				return HttpResponseRedirect('/persona.persona/')
			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				response_data = {"error": "No se puede eliminar este tipo de calle"}
				return HttpResponse(
						json.dumps(response_data),
						content_type="application/json"
					)
	else:
		return redirect('/login/')




def PersonaEditar(request):
	if(request.session.get("idusuario", False)):
		idpersona = request.GET.get('idpersona')
		instance = get_object_or_404(Persona, id=idpersona)
		form = PersonaForm(request.POST or None, instance=instance)

		try:

			ubigeonacimiento = Ubigeo.objects.get(id=instance.ubigeonacimiento.id)
			Depnacimiento = Ubigeo.objects.get(coddep=ubigeonacimiento.coddep,coddist = '00',codprov='00' )
			Provnacimiento = Ubigeo.objects.get(coddep=ubigeonacimiento.coddep,coddist = '00',codprov=ubigeonacimiento.codprov)
			ubigeonacimiento = Depnacimiento.nombreubigeo+"/"+Provnacimiento.nombreubigeo+"/"+ubigeonacimiento.nombreubigeo
			
			ubigeoresidencia = Ubigeo.objects.get(id=instance.ubigeoresidencia.id)
			Depresidencia = Ubigeo.objects.get(coddep=ubigeoresidencia.coddep,coddist = '00',codprov='00' )
			Provresidencia = Ubigeo.objects.get(coddep=ubigeoresidencia.coddep,coddist = '00',codprov=ubigeoresidencia.codprov)
			ubigeoresidencia = Depresidencia.nombreubigeo+"/"+Provresidencia.nombreubigeo+"/"+ubigeoresidencia.nombreubigeo
		except Exception as e:
			ubigeos = None

		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos editados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		return render(
				request, 
				'persona/persona_form.html',
				{
					'form': form, 'url':'/persona.persona/editar/?idpersona='+idpersona, 'ubigeonacimiento':ubigeonacimiento, 'ubigeoresidencia':ubigeoresidencia
				}
			)
	else:
		return redirect('/login/')		

def UbigeoNacimientoDepListar(request):
	if(request.session.get("idusuario", False)):

		# estado = request.GET.get('departamento')

		ubigeo = Ubigeo.objects.filter(codprov='00').order_by('id')
		return render(request, 'persona/ubigeoDep_form.html',{'ubigeo': ubigeo})
	else:
		return redirect('/login/')

def UbigeoNacimientoProvListar(request, dep):
	if(request.session.get("idusuario", False)):

		# estado = request.GET.get('departamento')

		ubigeo = Ubigeo.objects.filter(~Q(codprov = '00'),coddep=dep, coddist = '00').order_by('id')
		return render(request, 'persona/ubigeoProv_form.html',{'ubigeo': ubigeo})
	else:
		return redirect('/login/')

def UbigeoNacimientoDistListar(request, dep, prov):
	if(request.session.get("idusuario", False)):

		# estado = request.GET.get('departamento')

		ubigeo = Ubigeo.objects.filter(~Q(coddist = '00'),coddep=dep, codprov=prov).order_by('id')
		return render(request, 'persona/ubigeoDist_form.html',{'ubigeo': ubigeo})
	else:
		return redirect('/login/')

def UbigeoListar(request):
	if(request.session.get("idusuario", False)):
		iddistrito = request.POST['iddistrito']
		
		# estado = request.GET.get('departamento')
		ubigeo = Ubigeo.objects.get(id=int(iddistrito))
		# print(ubigeo, "Distrito AAAAAAAAAAAA")

		msg = {"coddep" : ubigeo.coddep,"codprov" : ubigeo.codprov, "coddist" : ubigeo.coddist}
		return HttpResponse(
				json.dumps( msg ), 
				content_type="application/json"
			)
	else:
		return redirect('/login/')
