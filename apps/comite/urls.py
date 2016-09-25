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
    url(r'^comite/nacional/ajax/$', ComiteNacionalAjax , name="nivelcomite-ajax"),

    # Nivel Cargo
    url(r'^nivelcargo/$', NivelCargoLista , name="lista_nivelcargo"),
    url(r'^nivelcargo/agregar/$', NivelCargoAgregar , name="nivelcargo-agregar"),
    url(r'^nivelcargo/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    url(r'^nivelcargo/guardar/$', NivelCargoGuardar , name="nivelcargo-guardar"),
    url(r'^nivelcargo/editar/$', NivelCargoEditar , name="nivelcargo-editar"),

    url(r'^comite/nacional/$', ComiteNacionalLista , name="lista_comitenacional"),
    url(r'^comite/nacional/agregar/$', ComiteNacionalAgregar , name="comitenacional-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    url(r'^comite/nacional/editar/$', ComiteNacionalEditar , name="comitenacional-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),


    url(r'^comite/regional/$', ComiteRegionalLista , name="lista_comiteregional"),
    url(r'^comite/regional/agregar/$', ComiteRegionalAgregar , name="comiteregional-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    url(r'^comite/regional/editar/$', ComiteRegionalEditar , name="comiteregional-editar"),
    url(r'^comite/ubigeo/regiones/ajax/$', ListaRegionesAjax , name="listaregiones-ajax"),

    url(r'^comite/provincial/$', ComiteProvincialLista , name="lista_comiteprovincial"),
    url(r'^comite/provincial/agregar/$', ComiteProvincialAgregar , name="comiteprovincial-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    url(r'^comite/regional/editar/$', ComiteRegionalEditar , name="comiteregional-editar"),
    url(r'^comite/ubigeo/provincias/ajax/$', ListaProvinciasAjax , name="listaregiones-ajax"),
    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),


    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),


    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

    # url(r'^comite/agregar/$', ComiteAgregar , name="comite-agregar"),
    # url(r'^comite/eliminar/$', ComiteEliminar , name="comite-eliminar"),
    # url(r'^comite/editar/$', ComiteEditar , name="comite-editar"),
    # url(r'^comite/ajax/$', ComiteAjax , name="nivelcomite-ajax"),

]