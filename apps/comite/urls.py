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

    # TipoCargo
    url(r'^tipocargo/$', ListaTipoCargo , name="lista_tipocargo"),
    url(r'^tipocargo/agregar/$', TipoCargoAgregar , name="tipocargo-agregar"),
    url(r'^tipocargo/eliminar/$', TipoCargoEliminar , name="tipocargo-eliminar"),
    url(r'^tipocargo/editar/$', TipoCargoEditar , name="tipocargo-editar"),
    #
    # 

    # Comité
    url(r'^comite/$', ComiteLista , name="lista_comite"),
    url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),
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