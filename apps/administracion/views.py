from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


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