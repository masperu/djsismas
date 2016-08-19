# from django.conf.urls import url
# urlpatterns = [
#     # url(r'^$', "apps.adm.views.HomeView", name="home"),
#     # Administracion de Usuarios
#     url(r'^usuarios.usuario/listar/$', UsuarioListar, name='user_list'),
#     url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
#     url(r'^usuarios.usuario/editar/$', UsuarioEditar, name='user_edit'),
#     url(r'^usuarios.usuario/eliminar/$', UsuarioEliminar, name='user_delete'),
#     # Administracion de Modulos
#     url(r'^modulos.modulo/listar/$',ModuloListar, name='modulo_list'),
#     url(r'^modulos.modulo/crear/$',ModuloCrear, name='modulo_add'),
#     url(r'^modulos.modulo/editar/$', ModuloEditar, name='modulo_edit'),
#     url(r'^modulos.modulo/eliminar/$', ModuloEliminar, name='modulo_delete'),
#     url(r'^modulos.modulo/formulario/$', ModuloFormulario.as_view(), name='modulo_form'),
#     # Administracion de Menus
#     url(r'^menus.menu/listar/$', MenuListarInfo, name='menu_list_info'),
#     url(r'^menus.menumodulo/listar/$', MenuListarTodos, name='menu_list_all'),
#     url(r'^menus.menu/listar/(?P<idm>\d+)$', MenuListar, name='menu_list'),
#     url(r'^menus.menu/eliminar/$', MenuEliminar, name='menu_delete'),
#     url(r'^menus.menu/editar/$', MenuEditar, name='menu_editar'),
#     url(r'^menus.menu/crear/$', MenuCrear, name='menu_crear'),
#     #url(r'^menu/listar/(?P<id>\d+)$', "apps.adm.viewstotal.MenuListarInfo", name='menu_list'),
#     # Roles
#     url(r'^roles.rol/listar/$', RolListar, name='rol_list'),
#     url(r'^roles.rol/eliminar/$', RolEliminar, name='rol_delete'),
#     url(r'^roles.rol/crear/$', RolCrear, name='rol_add'),
#     url(r'^roles.rol/editar/$', RolEditar, name='rol_edit'),
#     # Accesos
#     url(r'^accesos.acceso/listar/(?P<idr>\d+)$', RolListarAccesos, name='rol_list_access'),
#     url(r'^accesos.acceso/editar/$', AccesosEditar, name='access_edit'),
#     # Roles x Usuario
#     url(r'^roles.rolusuario/listar/$', RolUsuarioListar, name='rol_user_list'),
#     url(r'^roles.rolusuario/editar/$', RolUsuarioEditar, name='rol_user_edit'),
#     url(r'^roles.rol/(?P<idr>\d+)/menus/$', RolListarMenus, name='rol_list_menus'),
#     # CatalogosUnidadesMedidas
#     url(r'^catalogosunidadesmedidas.catalogounidadmedida/listar/$', CatalogoUnidadMedidaListar, name='catalogo_unidad_medida_list'),
#     url(r'^catalogosunidadesmedidas.catalogounidadmedida/crear/$', CatalogoUnidadMedidaCrear, name='catalogounidadmedida_add'),
#     url(r'^catalogosunidadesmedidas.catalogounidadmedida/editar/$', CatalogoUnidadMedidaEditar, name='catalogounidadmedida_edit'),
#     url(r'^catalogosunidadesmedidas.catalogounidadmedida/eliminar/$', CatalogoUnidadMedidaEliminar, name='catalogounidadmedida_delete'),
#     # CatalogosUnidadesMedidas - MBrechas
#     url(r'^catalogosunidadesmedidas.mbrechas.catalogounidadmedidambrechas/listar/$', CatalogoUnidadMedidaMBrechasListar, name='catalogo_unidad_medida_mbrechas_list'),
#     url(r'^catalogosunidadesmedidas.mbrechas.catalogounidadmedidambrechas/editar/$', CatalogoUnidadMedidaMBrechasEditar, name='catalogo_unidad_medida_mbrechas_edit'),
#     url(r'^catalogosunidadesmedidas.mbrechas.catalogounidadmedidambrechas/listarmbrechas/$', CatalogoUnidadMedidaMBrechasListarExtension, name='catalogo_unidad_medida_mbrechas_edit'),

# ]