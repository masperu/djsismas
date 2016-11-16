from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.deletion import ProtectedError
import json
from .models import *
from .forms import *
from django.db.models import Q
from apps.persona.models import Ubigeo, EstadoCivil

import time

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def ListaFichas(request):
	if(request.session.get("idusuario", False)):
		fichas = Ficha.objects.all()
		total = fichas.count()
		paginator = Paginator(fichas, 10)

		page = request.GET.get('page')
		try:
			fichas = paginator.page(page)
		except PageNotAnInteger:
			fichas = paginator.page(1)			
		except EmptyPage:
			fichas = paginator.page(paginator.num_pages)

		return render(request, 'ficha/ficha_grilla.html',{ 'fichas': fichas, 'total': total } )
	else:
		return redirect('/login/')


def FichasAgregar(request):

	if(request.session.get("idusuario", False)):

		url = "/fichas/agregar/"
		estadocivil = EstadoCivil.objects.all()

		if request.method == 'POST':
			form = FichaForm(request.POST)

			if form.is_valid():
				ficha = form.save(commit=False)
				ficha.save()
				form.cleaned_data
				msg = {"msg" : "Datos guardados correctamente"}
				return HttpResponse(
							json.dumps( msg ), 
							content_type="application/json"
						)
			else :
				return render(request, 'ficha/ficha_form.html',{'form':form, 'url': url, 'estadocivil': estadocivil })
		else:
			form = FichaForm()
			return render(request, 'ficha/ficha_form.html',{'form':form, 'url': url, 'estadocivil': estadocivil })
	
	else:
		return redirect('/login/')