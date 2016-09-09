from django.conf.urls import url
from apps.comite.views import *

urlpatterns = [
    #url(r'^listar$', "apps.administracion.views.HomeView", name="home"),
    #url(r'^usuarios.usuario/listar/$', HomeView, name='user_list'),
    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),

    # NivelComite
    url(r'^nivelcomite/$', ListaNivelComite , name="lista_nivelcomite"),
    url(r'^nivelcomite/agregar/$', NivelComiteAgregar , name="nivelcomite-agregar"),
    url(r'^nivelcomite/eliminar/$', NivelComiteEliminar , name="nivelcomite-eliminar"),
    url(r'^nivelcomite/editar/$', NivelComiteEditar , name="nivelcomite-editar"),
	#
	# 

    # ROLES
    #url(r'^rol/$', ListaRol , name="lista_rol"),
    # 
    # 
    # 
    #
    # 

    # ACCESOS
 	#url(r'^acceso/$', ListaAccesos , name="lista_accesos"),
    # 
    # 
    # 
    #
    # 

    # PERFIL
 	#url(r'^perfil/$', ListaPerfil , name="lista_perfil"),    
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
]