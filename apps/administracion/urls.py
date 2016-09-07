from django.conf.urls import url
from apps.administracion.views import *

urlpatterns = [
    url(r'^$', VistaInicio , name="home"),
    url(r'^login/$', Login , name="login"),
    url(r'^logout/$', Logout , name="logout"),
    url(r'^menu/$', ListaMenus , name="logout"),
    url(r'^menu-form/$', MenuAgregar , name="logout"),
    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]