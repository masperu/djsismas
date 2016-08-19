from django.shortcuts import render

# Create your views here.


def VistaInicio(request):
	return render( request, 'login.html')
