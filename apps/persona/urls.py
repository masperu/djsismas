from django.conf.urls import url
from apps.persona.views import *

urlpatterns = [

    # ESTADOCIVIL
    url(r'^estadocivil/$', ListaEstadoCivil , name="lista_estadocivil"),
    url(r'^estadocivil/agregar/$', EstadoCivilAgregar , name="menu-agregar"),
    url(r'^estadocivil/eliminar/$', EstadoCivilEliminar , name="menu-eliminar"),
    url(r'^estadocivil/editar/$', EstadoCivilEditar , name="menu-editar"),
    # url(r'^menu/ajax/$', MenuAjax , name="menu-ajax"),
	# 

    # TIPOCALLE
    url(r'^tipocalle/$', ListaTipoCalle , name="lista_tipocalle"),
    url(r'^tipocalle/agregar/$', TipoCalleAgregar , name="tipocalle-agregar"),
    url(r'^tipocalle/eliminar/$', TipoCalleEliminar , name="tipocalle-eliminar"),
    url(r'^tipocalle/editar/$', TipoCalleEditar , name="tipocalle-editar"),
    # 

    # ACCESOS
 
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

    # USUARIOS
    # 
    # 
    # 
    # 
    #
    # 

]