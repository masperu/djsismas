from django.conf.urls import url
from apps.administracion.views import *

urlpatterns = [
    url(r'^$', VistaInicio , name="home"),
    url(r'^login/$', Login , name="login"),
    url(r'^logout/$', Logout , name="logout"),
    
    # MENUS
    url(r'^menu/$', ListaMenus , name="lista_menu"),
    url(r'^menu/agregar/$', MenuAgregar , name="menu-agregar"),
    url(r'^menu/eliminar/$', MenuEliminar , name="menu-eliminar"),
    url(r'^menu/editar/$', MenuEditar , name="menu-editar"),
    url(r'^menu/ajax/$', MenuAjax , name="menu-ajax"),
	url(r'^menu/listar/$', MenuListar , name="menu-listar"),

    # ROLES
    url(r'^rol/$', ListaRol , name="lista_rol"),
    url(r'^rol/agregar/$', RolAgregar , name="rol-agregar"),
    url(r'^rol/eliminar/$', RolEliminar , name="rol-eliminar"),
    url(r'^rol/editar/$', RolEditar , name="rol-editar"),
    url(r'^rol/accesomenu/$', RolMenuAccesoEditar , name="rol-editar"),
    # 

    # ACCESOS
 	url(r'^acceso/$', ListaAccesos , name="lista_accesos"),
    # 
    # 
    # 
    #
    # 

    # PERFIL
 	url(r'^perfil/$', ListaPerfil , name="lista_perfil"),    
    url(r'^perfilroles/listar/$', ListaPerfilRoles , name="lista_perfilrol"),  
    # 
    # 
    #
    # 

    # USUARIOS
    url(r'^usuario/$', ListaUsuarios , name="lista-usuario"),
    url(r'^usuario/agregar/$', UsuarioAgregar , name="agregar-usuario"),
    url(r'^usuario/editar/$', UsuarioEditar , name="editar-usuario"),
    url(r'^usuario/eliminar/$', UsuarioEliminar , name="eliminar-usuario"),
    #
    # 

    # USUARIOS
    url(r'^organizacion/$', ListaOrganizacion , name="lista_perfil"),   
    url(r'^organizacion/agregar/$', OrganizacionAgregar , name="organizacion-agregar"),
    url(r'^organizacion/eliminar/$', OrganizacionEliminar , name="organizacion-eliminar"),
    url(r'^organizacion/editar/$', OrganizacionEditar , name="organizacion-editar"),
    # 
    # 

    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]