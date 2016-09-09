from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def ListaNivelComite(request):
	if(request.session.get("idusuario", False)):
		nivelcomite = NivelComite.objects.all()
		paginator = Paginator(nivelcomite, 2) # Show 25 contacts per page

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
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = NivelComiteForm(request.POST)

			if form.is_valid():

				# print(form)
				
				nivelcomite = form.save(commit=False)
				nivelcomite.save()
				form.cleaned_data
				return redirect(ListaNivelComite)
				# return HttpResponseRedirect('.') 

			else :
				# print("formulario no valido")
				form = NivelComiteForm()
				return render(request, 'comite/nivelcomite_form.html',{'form':form })
				#return HttpResponseRedirect('.') 

		else:
			form = NivelComiteForm()
			return render(request, 'comite/nivelcomite_form.html',{'form':form })
	
	else:
		return redirect('/login/')


def NivelComiteEditar(request):
	pass


def NivelComiteEliminar(request):
	pass