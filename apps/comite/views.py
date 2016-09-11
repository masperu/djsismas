from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.deletion import ProtectedError
import json
from .models import *
from .forms import *

import time

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def ListaNivelComite(request):
	if(request.session.get("idusuario", False)):
		nivelcomite = NivelComite.objects.all()
		paginator = Paginator(nivelcomite, 10) # Show 25 contacts per page

		page = request.GET.get('page')
		try:
			nivelcomite = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			nivelcomite = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			nivelcomite = paginator.page(paginator.num_pages)
		return render(request, 'comite/nivelcomite.html',{'nivelcomite': nivelcomite})
	else:
		return redirect('/login/')


def NivelComiteAgregar(request):

	if(request.session.get("idusuario", False)):

		url = "/nivelcomite/agregar/"

		if request.method == 'POST':
			#time.sleep(100)
			# create a form instance and populate it with data from the request:
			form = NivelComiteForm(request.POST)

			if form.is_valid():

				# print(form)
				
				nivelcomite = form.save(commit=False)
				nivelcomite.save()
				form.cleaned_data
				#return redirect(ListaNivelComite)
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
				# return HttpResponseRedirect('.') 

			else :
				# print("formulario no valido")
				#form = NivelComiteForm()
				return render(request, 'comite/nivelcomite_form.html',{'form':form, 'url': url })
				#return HttpResponseRedirect('.') 

		else:
			form = NivelComiteForm()
			return render(request, 'comite/nivelcomite_form.html',{'form':form, 'url': url})
	
	else:
		return redirect('/login/')


def NivelComiteEditar(request):
	if(request.session.get("idusuario", False)):

		

		idnivelcomite = request.GET.get('idnivelcomite')
		instance = get_object_or_404(NivelComite, id=idnivelcomite)

		url = "/nivelcomite/editar/?idnivelcomite=" + idnivelcomite

		form = NivelComiteForm(request.POST or None, instance=instance)

		if form.is_valid():
			# time.sleep(10)

			form.save()
			#return redirect(ListaNivelComite)
			msg = {"msg" : "Datos guardados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)

		else:

			# print("No se han guardado los cambios")
			# time.sleep(5)
			return render(request, 'comite/nivelcomite_form.html',{'form':form, 'url': url})		

		return render(request, 'comite/nivelcomite_form.html',{'form':form, 'url': url})

	else:
		return redirect('/login/')


def NivelComiteEliminar(request):
	if(request.session.get("idusuario", False)):
		idnivelcomite = request.GET.get('idnivelcomite')
		if idnivelcomite:
			try:
				nivelcomite = NivelComite.objects.get(id = idnivelcomite)
				nivelcomite.delete()
				
				# if nivelcomite:
				# 	return HttpResponseRedirect('/nivelcomite/')
				msg = {"success" : "Datos eliminados correctamente"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)

			except ProtectedError as e:
				# return HttpResponseRedirect('/menu/')
				msg = {"error" : "Error al eliminar datos"}
				# response_data = {"error": "No se puede eliminar este menu porque tiene hijos"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)

	else:
		return redirect('/login/')




def ListaTipoCargo(request):
	if(request.session.get("idusuario", False)):
		tipocargo = TipoCargo.objects.all()
		paginator = Paginator(tipocargo, 10)

		page = request.GET.get('page')
		try:
			tipocargo = paginator.page(page)
		except PageNotAnInteger:
			tipocargo = paginator.page(1)
		except EmptyPage:
			tipocargo = paginator.page(paginator.num_pages)
		return render(request, 'comite/tipocargo.html',{'tipocargo': tipocargo})
	else:
		return redirect('/login/')


def TipoCargoAgregar(request):

	if(request.session.get("idusuario", False)):
		url = "/tipocargo/agregar/"
		if request.method == 'POST':
			form = TipoCargoForm(request.POST)
			if form.is_valid():
				tipocargo = form.save(commit=False)
				tipocargo.save()
				form.cleaned_data
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else :
				return render(request, 'comite/tipocargo_form.html',{'form':form, 'url': url })
		else:
			form = TipoCargoForm()
			return render(request, 'comite/tipocargo_form.html',{'form':form, 'url': url})
	else:
		return redirect('/login/')


def TipoCargoEditar(request):
	if(request.session.get("idusuario", False)):
		idtipocargo = request.GET.get('idtipocargo')
		instance = get_object_or_404(TipoCargo, id=idtipocargo)
		url = "/tipocargo/editar/?idtipocargo=" + idtipocargo
		form = TipoCargoForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos guardados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		else:
			return render(request, 'comite/tipocargo_form.html',{'form':form, 'url': url})		
		return render(request, 'comite/tipocargo_form.html',{'form':form, 'url': url})
	else:
		return redirect('/login/')


def TipoCargoEliminar(request):
	if(request.session.get("idusuario", False)):
		idtipocargo = request.GET.get('idtipocargo')
		if idtipocargo:
			try:
				tipocargo = TipoCargo.objects.get(id = idtipocargo)
				tipocargo.delete()
				msg = {"success" : "Datos eliminados correctamente"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)
			except ProtectedError as e:
				msg = {"error" : "Error al eliminar datos"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)

	else:
		return redirect('/login/')



def ComiteLista(request):
	if(request.session.get("idusuario", False)):
		comite = Comite.objects.all()
		paginator = Paginator(comite, 10)

		page = request.GET.get('page')
		try:
			comite = paginator.page(page)
		except PageNotAnInteger:
			comite = paginator.page(1)
		except EmptyPage:
			comite = paginator.page(paginator.num_pages)
		return render(request, 'comite/comite.html',{'comite': comite})
	else:
		return redirect('/login/')

def ComiteAjax(request):
	if(request.session.get("idusuario", False)):
		comite = Comite.objects.filter(nombre__icontains = "" + request.GET.get('query') + "" )[:10]
		total = comite.count()
		return render(
			request,
			'comite/comite.json',
			{
				'comite': comite,
				'total':total
			},
			content_type="application/json",
		)
		#return render(request, 'comite/comite.html',{'comite': comite})
	else:
		return redirect('/login/')

def ComiteAgregar(request):
	if(request.session.get("idusuario", False)):
		url = "/comite/agregar/"
		nivelcomite = NivelComite.objects.all()
		comitepadre = None

		if request.method == 'POST':
			form = ComiteForm(request.POST)
			if form.is_valid():
				comite = form.save(commit=False)
				comite.save()
				form.cleaned_data
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else :
				return render(request, 'comite/comite_form.html', {'url': url, 'form':form, 'nivelcomite':nivelcomite, 'comitepadre':comitepadre })
		else:
			form = ComiteForm()
			return render(request, 'comite/comite_form.html',{'url': url, 'nivelcomite':nivelcomite, 'form':form, 'comitepadre':comitepadre })
	else:
		return redirect('/login/')


def ComiteEditar(request):
	if(request.session.get("idusuario", False)):
		idcomite = request.GET.get('idcomite')
		instance = get_object_or_404(Comite, id=idcomite)
		url = "/comite/editar/?idcomite=" + idcomite
		form = ComiteForm(request.POST or None, instance=instance)
		
		#Todos lo comites para la lista
		nivelcomite = NivelComite.objects.all()

		#ComitePadre
		try:
			comitepadre = Comite.objects.get(id=instance.comitepadre.id)
		except Exception as e:
			comitepadre = None


		if form.is_valid():
			form.save()
			msg = {"msg" : "Datos guardados correctamente"}
			return HttpResponse(
					json.dumps( msg ), 
					content_type="application/json"
				)
		else:
			return render(request, 'comite/comite_form.html',{'form':form, 'url': url, 'nivelcomite':nivelcomite, 'comitepadre': comitepadre })	

		return render(request, 'comite/comite_form.html',{'form':form, 'url': url, 'nivelcomite':nivelcomite, 'comitepadre': comitepadre })
	else:
		return redirect('/login/')


def ComiteEliminar(request):
	if(request.session.get("idusuario", False)):
		idcomite = request.GET.get('idcomite')
		if idcomite:
			try:
				comite = Comite.objects.get(id = idcomite)
				comite.delete()
				msg = {"success" : "Datos eliminados correctamente"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)
			except ProtectedError as e:
				msg = {"error" : "Error al eliminar datos"}
				return HttpResponse(
						json.dumps(msg),
						content_type="application/json"
					)

	else:
		return redirect('/login/')

