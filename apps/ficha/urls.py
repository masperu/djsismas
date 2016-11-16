from django.conf.urls import url
from apps.ficha.views import *

urlpatterns = [

    # Fichas
    url(r'^fichas/$', ListaFichas , name="lista-fichas"),
    url(r'^fichas/agregar/$', FichasAgregar , name="fichas-agregar"),
    # url(r'^nivelcomite/eliminar/$', NivelComiteEliminar , name="nivelcomite-eliminar"),
    # url(r'^nivelcomite/editar/$', NivelComiteEditar , name="nivelcomite-editar"),	
	#
]