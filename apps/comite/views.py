from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
import json
from .models import *
from .forms import *

import time

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def ListaNivelComite(request):
	if(request.session.get("idusuario", False)):
		nivelcomite = NivelComite.objects.all()
		paginator = Paginator(nivelcomite, 15) # Show 25 contacts per page

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
	pass