from django.conf.urls import url
from apps.administracion.views import *

urlpatterns = [
    url(r'^$', VistaInicio , name="home"),
    url(r'^login/$', Login , name="login"),
    url(r'^home/$', VistaHome , name="home"),
    #url(r'^usuarios.usuario/listar/$', HomeView, name='user_list'),
    #url(r'^usuarios.usuario/crear/$', UsuarioCrear, name='user_add'),
]