from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def VistaInicio(request):
	return render( request, 'administracion/login.html')



def Login(request):
	if 50 > 20:
		return redirect('/home/')
	else:
		return redirect('/login/')
	

def VistaHome(request):
	return render( request, 'administracion/home.html')
