from django.conf.urls import url
from apps.administracion.views import *

urlpatterns = [
    url(r'^$', VistaInicio , name="home"),
    url(r'^login/$', Login , name="login"),
    url(r'^logout/$', Logout , name="logout"),
    
    # MENUS
    url(r'^menu/$', ListaMenus , name="lista_menu"),
    url(r'^menu-form/$', MenuAgregar , name="menu-agregar"),
    url(r'^menu/eliminar/(?P<idmenu>[0-9]+)/$', MenuEliminar , name="menu-eliminar"),
    # 
	#
	# 

    # ROLES
    url(r'^rol/$', ListaRol , name="lista_rol"),
    # 
    # 
    # 
    #
    # 

    # ACCESOS
    # 
    # 
    # 
    # 
    #
    # 

    # PERFIL
    # 
    # 
    # 
    # 
    #
    # 

    # USUARIOS
    # 
    # 
    # 
    # 
    #
    # 

    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]